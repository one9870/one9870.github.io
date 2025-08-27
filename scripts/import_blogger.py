# ...existing code...
import os
import re
import sys
import requests
import urllib.parse
from markdownify import markdownify
from slugify import slugify
from datetime import datetime

IMG_RE = re.compile(r'<img[^>]+src="([^"]+)"', re.I)
PERMALINK_RE = re.compile(r'permalink:\s*(.+)', re.I)

def fetch_entries(blog_url, start=1, per=50, limit=None):
    entries = []
    while True:
        url = f"{blog_url.rstrip('/')}/feeds/posts/default?alt=json&start-index={start}&max-results={per}"
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        feed = r.json().get('feed', {})
        batch = feed.get('entry', [])
        if not batch:
            break
        entries.extend(batch)
        if limit and len(entries) >= limit:
            return entries[:limit]
        if len(batch) < per:
            break
        start += per
    # ensure newest first (Blogger feed may be newest first already)
    return sorted(entries, key=lambda e: get_field(e, 'published') or get_field(e, 'updated') or '', reverse=True)

def safe_filename(title, date_str):
    base = slugify(title) or "post"
    return f"{date_str}-{base}.md"

def download_image(src, images_dir):
    try:
        parsed = urllib.parse.urlparse(src)
        name = os.path.basename(parsed.path) or "image"
        name = urllib.parse.unquote(name)
        dest = os.path.join(images_dir, name)
        if os.path.exists(dest):
            base, ext = os.path.splitext(name)
            i = 1
            while True:
                candidate = f"{base}-{i}{ext}"
                dest = os.path.join(images_dir, candidate)
                if not os.path.exists(dest):
                    break
                i += 1
        resp = requests.get(src, stream=True, timeout=15)
        resp.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in resp.iter_content(1024):
                if chunk:
                    f.write(chunk)
        return dest.replace("\\", "/")
    except Exception:
        return None

def get_field(entry, key):
    v = entry.get(key)
    if isinstance(v, dict):
        return v.get('$t', "")
    return v or ""

def normalize_datetime(published):
    if not published:
        return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    try:
        date_part, time_part = published.split("T")
        time_part = time_part.split("+")[0].split("-")[0].split(".")[0]
        return f"{date_part} {time_part}"
    except Exception:
        return published

def entry_labels(entry):
    cats = []
    for c in entry.get('category', []):
        term = c.get('term')
        if term:
            cats.append(term)
    return cats

def existing_slugs_from_posts(posts_dir):
    slugs = set()
    if not os.path.isdir(posts_dir):
        return slugs
    for fname in os.listdir(posts_dir):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(posts_dir, fname)
        # filename-based slug: remove date prefix and extension
        m = re.match(r'^\d{4}-\d{2}-\d{2}-(.+)\.md$', fname)
        if m:
            slugs.add(m.group(1))
        # try to read permalink or title from front-matter
        try:
            with open(path, encoding="utf-8") as f:
                head = "".join([next(f) for _ in range(40)])
                pm = PERMALINK_RE.search(head)
                if pm:
                    slug = pm.group(1).strip().rstrip('/')
                    # if permalink like /posts/slug/ -> extract final part
                    slug_part = slug.split('/')[-1]
                    if slug_part:
                        slugs.add(slug_part)
        except Exception:
            continue
    return slugs

def write_post(jekyll_root, title, published, content_html, labels):
    posts_dir = os.path.join(jekyll_root, "_posts")
    images_dir = os.path.join(jekyll_root, "assets", "images")
    os.makedirs(posts_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)

    # download images and replace src
    imgs = IMG_RE.findall(content_html)
    for src in imgs:
        if src.startswith("http://") or src.startswith("https://"):
            local_path = download_image(src, images_dir)
            if local_path:
                rel = "/" + os.path.relpath(local_path, jekyll_root).replace("\\", "/")
                content_html = content_html.replace(src, rel)

    md_body = markdownify(content_html, heading_style="ATX")
    published_norm = normalize_datetime(published)
    date_part = published_norm.split(" ")[0]
    fname = safe_filename(title, date_part)
    filepath = os.path.join(posts_dir, fname)

    labels_list = "[]"
    if labels:
        labels_list = "[" + ", ".join(f'"{l}"' for l in labels) + "]"

    title_safe = title.replace('"', "'")
    permalink_slug = slugify(title)
    fm = [
        "---",
        f'title: "{title_safe}"',
        f"date: {published_norm}",
        f"categories: {labels_list}",
        f"tags: {labels_list}",
        f'permalink: /posts/{permalink_slug}/',
        "---",
        ""
    ]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(fm))
        f.write(md_body)
    return filepath

def main():
    if len(sys.argv) < 3:
        print("Usage: import_blogger.py BLOG_URL JEKYLL_ROOT [--limit N]")
        sys.exit(1)
    blog_url = sys.argv[1]
    jekyll_root = sys.argv[2].rstrip("\\/")

    limit = 5
    # parse optional args
    for i, a in enumerate(sys.argv[3:], start=3):
        if a in ("--limit", "-n") and i+1 < len(sys.argv):
            try:
                limit = int(sys.argv[i+1])
            except:
                pass

    posts_dir = os.path.join(jekyll_root, "_posts")
    os.makedirs(posts_dir, exist_ok=True)

    existing = existing_slugs_from_posts(posts_dir)
    print(f"Found {len(existing)} existing post slugs in _posts (will be excluded)")

    # fetch a larger batch to ensure skipping existing ones still yields enough
    batch_size = max(50, limit * 3)
    entries = fetch_entries(blog_url, per=batch_size)
    print(f"Fetched {len(entries)} entries from blog; selecting up to {limit} new ones")

    to_import = []
    for e in entries:
        title = get_field(e, "title").strip() or "untitled"
        slug = slugify(title)
        if slug in existing:
            continue
        to_import.append(e)
        if len(to_import) >= limit:
            break

    if not to_import:
        print("No new posts to import (all recent items already exist).")
        return

    for e in to_import:
        title = get_field(e, "title").strip() or "untitled"
        published = get_field(e, "published") or get_field(e, "updated")
        content_html = get_field(e, "content") or get_field(e, "summary") or ""
        labels = entry_labels(e)
        path = write_post(jekyll_root, title, published, content_html, labels)
        print("Wrote:", path)

if __name__ == "__main__":
    main()
# ...existing code...