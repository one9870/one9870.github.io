import os
import re
import sys
import requests
import urllib.parse
from markdownify import markdownify
from slugify import slugify
from datetime import datetime

def fetch_entries(blog_url, start=1, per=50, limit=None):
    entries = []
    while True:
        url = f"{blog_url.rstrip('/')}/feeds/posts/default?alt=json&start-index={start}&max-results={per}"
        r = requests.get(url)
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
    return entries if not limit else entries[:limit]

def safe_filename(title, date_str):
    base = slugify(title, lowercase=False) or "post"
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
                f.write(chunk)
        return dest.replace("\\", "/")
    except Exception:
        return None

def get_field(entry, key):
    v = entry.get(key)
    if isinstance(v, dict):
        return v.get('$t',"")
    return ""

def normalize_datetime(published):
    if not published:
        return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    # example: 2025-08-21T02:00:00.000+08:00
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

def main():
    if len(sys.argv) < 3:
        print("Usage: import_blogger.py BLOG_URL JEKYLL_ROOT [--limit N]")
        sys.exit(1)
    blog_url = sys.argv[1]
    jekyll_root = sys.argv[2].rstrip("\\/")

    limit = None
    if len(sys.argv) >= 5 and sys.argv[3] == "--limit":
        try:
            limit = int(sys.argv[4])
        except:
            pass
    elif len(sys.argv) >= 4 and sys.argv[3].isdigit():
        limit = int(sys.argv[3])

    posts_dir = os.path.join(jekyll_root, "_posts")
    images_dir = os.path.join(jekyll_root, "assets", "images")
    os.makedirs(posts_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)

    entries = fetch_entries(blog_url, limit=limit)
    print(f"Found {len(entries)} entries (limit={limit})")

    img_pattern = re.compile(r'<img[^>]+src="([^"]+)"', re.I)

    for e in entries:
        title = get_field(e, "title").strip() or "untitled"
        title_safe = title.replace('"', "'")
        published_raw = get_field(e, "published") or get_field(e, "updated")
        published = normalize_datetime(published_raw)
        date_part = published.split(" ")[0]
        fname = safe_filename(title, date_part)
        filepath = os.path.join(posts_dir, fname)
        if os.path.exists(filepath):
            print("Skipped (exists):", filepath)
            continue

        content_html = get_field(e, "content") or get_field(e, "summary") or ""
        imgs = img_pattern.findall(content_html)
        for src in imgs:
            if src.startswith("http://") or src.startswith("https://"):
                local_path = download_image(src, images_dir)
                if local_path:
                    rel = "/" + os.path.relpath(local_path, jekyll_root).replace("\\", "/")
                    content_html = content_html.replace(src, rel)

        md = markdownify(content_html, heading_style="ATX")
        labels = entry_labels(e)
        if not labels:
            labels_list = "[]"
        else:
            # YAML inline list
            labels_list = "[" + ", ".join(f'"{l}"' for l in labels) + "]"

        fm = [
            "---",
            f'title: "{title_safe}"',
            f"date: {published}",
            f"categories: {labels_list}",
            f"tags: {labels_list}",
            f'permalink: /posts/{slugify(title)}/',
            "---",
            ""
        ]
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(fm))
            f.write(md)
        print("Wrote", filepath)

if __name__ == "__main__":
    main()