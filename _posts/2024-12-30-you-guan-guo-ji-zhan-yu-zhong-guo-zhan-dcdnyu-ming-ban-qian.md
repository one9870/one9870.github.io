---
title: "有關國際站與中國站DCDN域名搬遷"
date: 2024-12-30 22:56:00
categories: ["阿里雲"]
tags: ["阿里雲"]
permalink: /posts/you-guan-guo-ji-zhan-yu-zhong-guo-zhan-dcdnyu-ming-ban-qian/
---
# 有關國際站與中國站DCDN域名搬遷

DCDN遷移主要涉及域名和配置的遷移，而不是資料本身，因為DCDN是緩存在節點上的內容，以下將分為中國站與國際站來講解說明。

 

中國站

[![](/assets/images/中國版.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhskTd4XMNJcI5wYIO7R_BqltkZlft7tvwh7sg0UIO-KAVCTNnNVYnbAa1A8n9aQTbOZcb-M9WqD14Ktmhu53JKvstIB1WorIYexXDcRUS0GHqINUdlfsByzAkad6KRQ3uf_RAviVA2uwdFnSZB3aB8ka0w8lRma6glwG5bKw9yhD-ci_TW80ge31aQ98g/s1574/%E4%B8%AD%E5%9C%8B%E7%89%88.png)

//上圖為中國站介面

DCDN控制台提供了「域名遷入」功能，允許用戶自行將域名從一個帳號遷移到另一個帳號。

步驟簡述：

在新帳號的DCDN控制台選擇「域名遷入」。

進行域名歸屬驗證（通常是通過添加TXT記錄到DNS解析）。

驗證通過後，完成域名遷入。

理論上，在DCDN的管理域名上

 

 

國際站

  

//國際站如上圖，紅框位置為按鈕本該位置，目前是沒有的

理論上，官方文檔文字描述與中國站一致，應要可以在域名管理

頁面使用遷移域名服務。

但實際上因為近期介於 DCDN、ESA
產品接替，短時間官方對於國際站目前還是不會提供”遷移域名”按鈕在介面上。

 

目前可提繳工單，授權後台請其協助操作。

並在工單內部提供如下資訊:

國際站 DCDN 無域名搬遷按鈕可操作，授權給後台同學搬遷

舊阿里雲 UID：（填入）

需搬遷域名：（填入）

新阿里雲新 UID：（填入）

參考資料:

中國站DCDN域名遷入:

<https://help.aliyun.com/zh/edge-security-acceleration/dcdn/user-guide/migrate-dcdn-domain-names-across-accounts>

 

國際站DCDN域名遷入:

<https://www.alibabacloud.com/help/zh/edge-security-acceleration/dcdn/user-guide/migrate-dcdn-domain-names-across-accounts?spm=a2c63.m28257.0.i3>

  

[![](/assets/images/國際站改.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVudhFgP9qGONvZAHORermlG83HP1a9nQhGS7YMoqiah1nceyvMz0vCv7qaeBOsYkjvhTLBrOjlA2Qil9Z_jSeOz5nf0Gk0fYOK_kMHR89LdVEtAaZJO0lzj5Z0WIvGQQDuObgDH3DPcxawFxsj17AVkWwyBMoaV5RxRECQ1AGhy_V8xAQQPCA_kAQt_w/s1599/%E5%9C%8B%E9%9A%9B%E7%AB%99%E6%94%B9.png)

  