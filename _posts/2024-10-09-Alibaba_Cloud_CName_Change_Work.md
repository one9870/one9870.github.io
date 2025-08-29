---
title: "如何確認阿里雲域名cname更新後是否已生效"
date: 2024-10-09 09:13:00
categories: ["阿里雲"]
tags: ["阿里雲"]
permalink: /posts/ru-he-que-ren-a-li-yun-yu-ming-cnamegeng-xin-hou-shi-fou-yi-sheng-xiao/
---
有時阿里雲的托管域名在更改 cname 後無法正常訪問，這時可利用【nslookup -type=CNAME <托管域名>】指令查看目前該域名的 cname，再跟阿里雲控制台比對是否相同。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhLYU8Xb1uAtqMIgfw3fUvCKnm-vYLwAapPjStOBpeftw3b096twc9m1xnP4kk4Wq4W2mUpKo_T1dIFwj44JF4FWzMzibzzGFSmq_pnrDzVbn18TkOrgXIS1PLnclAWGdDDcsLFpgFDN1Y4Cu-iaAq8rlnqhIusHhiBJ18IRDvt_-z4eYcnZAFPe6yCKAcR=w747-h322)](https://blogger.googleusercontent.com/img/a/AVvXsEhLYU8Xb1uAtqMIgfw3fUvCKnm-vYLwAapPjStOBpeftw3b096twc9m1xnP4kk4Wq4W2mUpKo_T1dIFwj44JF4FWzMzibzzGFSmq_pnrDzVbn18TkOrgXIS1PLnclAWGdDDcsLFpgFDN1Y4Cu-iaAq8rlnqhIusHhiBJ18IRDvt_-z4eYcnZAFPe6yCKAcR)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgN_mujI-d1uZLoetmAC9hmPHE8a4-BIyV7nrFd2erILcBOh7_anmwIsNoOCMQj1VKk6HEbQfAoEhrcP1frNUnPJGhsbk-IppfOJZ646ef4byZ3sRkU1kslVN-w-Nyyrt6trY7MksU4aADN6FutIXTx1pFEc4SHAo5cy04woIik79Pg1AoDvhHuZd8OF_ox=w745-h354)](https://blogger.googleusercontent.com/img/a/AVvXsEgN_mujI-d1uZLoetmAC9hmPHE8a4-BIyV7nrFd2erILcBOh7_anmwIsNoOCMQj1VKk6HEbQfAoEhrcP1frNUnPJGhsbk-IppfOJZ646ef4byZ3sRkU1kslVN-w-Nyyrt6trY7MksU4aADN6FutIXTx1pFEc4SHAo5cy04woIik79Pg1AoDvhHuZd8OF_ox)

  
若不一樣則表示有可能是阿里雲控制台尚未獲取到更改後的 cname；另可配合阿里雲文檔內提到的 “刷新預熱”功能去刷新 URL 的緩存。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgK0vrIiqulgmSt4lN6xwdM_BmPDHCBX56_P6Y2i3mJcvAZmg0pyz7I8twWLskWvfBhx3pabjw0H2dMaNSDgIgr2jyYIfKxeeJeXW-c_EsZmyiZjeB6tZxOB1P54bNvWLRh2CyvNkaTI6VZeS4f61nBiJ1xMCM_gnqC0gWdHJ0ajW6IzxIeGNiLAAZdpLzh=w851-h353)](https://blogger.googleusercontent.com/img/a/AVvXsEgK0vrIiqulgmSt4lN6xwdM_BmPDHCBX56_P6Y2i3mJcvAZmg0pyz7I8twWLskWvfBhx3pabjw0H2dMaNSDgIgr2jyYIfKxeeJeXW-c_EsZmyiZjeB6tZxOB1P54bNvWLRh2CyvNkaTI6VZeS4f61nBiJ1xMCM_gnqC0gWdHJ0ajW6IzxIeGNiLAAZdpLzh)

  
  

 

在阿里雲上配置 CNAME 步驟如下：

 

### 1. 確認 CDN 分配的 CNAME 地址

- 登錄到阿里雲的 CDN 控制台，找到需要配置 CNAME 的域名。

- 在 CDN 設置頁面，找到該域名所對應的 CNAME 地址。

 

### 2. 到 DNS 設置中添加 CNAME 記錄

- 登錄到您使用的域名註冊商或者 DNS 解析提供商的控制台（例如阿里雲的 DNS，或其他第三方提供商）。

- 找到您的域名並進入 DNS 解析頁面。

- 添加一條新的 \*\*CNAME 記錄\*\*：

  - \*\*主機記錄\*\*：填寫需要解析的子域名，比如 `www`，或者直接填寫根域名的 `@`。

  - \*\*記錄類型\*\*：選擇 `CNAME`。

  - \*\*記錄值\*\*：填寫阿里雲 CDN 分配的
CNAME 地址（從第一步中獲得）。

  - \*\*TTL\*\*：保持默認值即可（通常是 10 分鐘或 1 小時）。

 

### 3. 等待 DNS 生效

- 新增或修改 CNAME 記錄後，通常需要幾分鐘到 24 小時來等待全球的 DNS 伺服器同步生效。

 

### 4. 驗證 CNAME 配置是否正確

- 您可以使用一些網絡工具（如 nslookup 或 `dig`），或直接通過阿里雲的 CDN 控制台驗證是否已經將域名正確解析到 CDN 提供的 CNAME 地址。

 

### 5. 測試 HTTPS 是否正常

- 當 CNAME 配置生效後，您可以打開您的網站並檢查 HTTPS 連接是否正常。如果沒有問題，瀏覽器應顯示一個有效的 SSL 憑證。

 

 

 

參考資料：

验证CNAME配置是否生效

<https://www.alibabacloud.com/help/zh/dcdn/getting-started/add-a-cname-record-for-a-domain-name#d7eaef2662cve>

 

刷新预热

<https://www.alibabacloud.com/help/zh/dcdn/user-guide/refresh-and-prefetch-resources#section-wdh-o0c-cwb>

 