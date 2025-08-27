---
title: "AWS未使用RDS資源但收到通知的可能原因"
date: 2025-04-05 23:23:00
categories: ["AWS"]
tags: ["AWS"]
permalink: /posts/without-using-RDS/
---
當管理者收到錯誤通知「RDS Error: Access denied for user 'rdsadmin'@'localhost'」，而其他雲端人員表示未曾使用/開通相關服務時，可依以下列舉原因檢查：

1. **IAM 角色或權限設定問題**如果角色或策略配置不當，就會導致「Access Denied」錯誤。
2. **應用程式或自動化腳本錯誤**如果應用程式或自動化腳本錯誤地使用用戶身分訪問資料庫，並且該用戶的權限不正確，就會發生「Access Denied」錯誤。
3. **資料庫存取問題**  
   防火牆、VPC 安全組或 NACL 設置錯誤，可能會阻止用戶連接，從而導致訪問拒絕。
4. **服務設置時連帶啟動/啟用**  
   如果 EC2 實例、Lambda 函數或其他服務無意中引用了資料庫的資源，這些服務可能會使用RDS，且以用戶身份嘗試訪問資料庫。

### 檢視方法：

* **檢查 IAM 角色和策略**：確認與AWS服務相關的 IAM 角色和策略配置，確認用戶訪問權限。
* **檢查自動化腳本和應用程式**：確認自動化流程、Lambda 函數、EC2 實例等是否錯誤地使用 `rdsadmin` 用戶，並檢查資料庫連接設置。
* **檢視有無其他帳號使用者進行啟用程式而串聯啟用此類資源**：須檢視系統紀錄、系統通知與雲上資源，以確認或排除此可能性。

以上內容參考文章

[Amazon RDS 的身分和存取管理 - Amazon Relational Database Service](https://docs.aws.amazon.com/zh_tw/AmazonRDS/latest/UserGuide/UsingWithRDS.IAM.html)

[使用執行角色定義 Lambda 函數許可 - AWS Lambda](https://docs.aws.amazon.com/zh_tw/lambda/latest/dg/lambda-intro-execution-role.html)

[什麼是 Amazon CloudWatch Logs？ - Amazon CloudWatch Logs](https://docs.aws.amazon.com/zh_tw/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)  