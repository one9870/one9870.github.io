---
title: "介紹IAM"
date: 2024-12-08 00:47:00
categories: ["AWS教學30天上手"]
tags: ["AWS教學30天上手"]
permalink: /posts/jie-shao-iam/
---
**介紹IAM**

**AWS IAM (****全稱:Identity and Access Management)**

l  
**用於允許多個用戶與應用程式同時在一隻AWS****帳戶底下的子帳號，透過可以設定精細的權限來進行靈活管理，以致可以實現”****最小權限原則”****。**

l  
**該服務為免費服務**

l   

[![](/assets/images/111.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIVLCzpI18REND4Dxfb0ZurC-YdSJge-nLAO2YIyvSe5gKAXC64LNKZS-9mEkqIprxb0O7Ax9iMPpZir6VdosHZuRXyEEm1OdOpM5nh9iUyF5ED79b6LpclSjcCvTXeRkG04qfsNKXUAyIuhw_Vhs4O4mcmtYPZkqZP1_PAee0tpEWeeeDcxc76GgDKgA/s578/111.png)

  
  
IAM 是以 RBAC(Role-Based Access Control)
去做設計，把 權限 (Policy) 給群組，而不是每個用戶。在用戶加入群組後，會自動繼承群組的權限，不用逐一去分配權限。

//要先透過E-mail向AWS申請頂級帳號，這帳號也就是我們所知道的Root Account。

//下圖概念與Linux OS用戶關係是一致的，Root帳號權限過大 >>> 透過IAM服務分割出用戶根群組權限。

**IAM****的核心組成可以用以下四個核心去看**

**1.****使用者 (Users)**

**意指使用者，可以是人，也可以是應用程式或者訪問 AWS** **資源的對象。**

**2.****群組 (Groups)**

**群組是使用者的集合。在群組中的使用者都會繼承該群組擁有的所有權限。這樣的設計方便組織和可以簡化權限分配。**

**3.****角色 (Roles)**

**角色的產生為用於職責分配所誕生，主要在於授予應用程序、服務或其他 AWS** **資源訪問權限。角色與使用者不同，沒有附帶固定憑證，而是動態被 AWS** **服務採用，我們舉個例子 :** **讓一個 Lambda** **函數訪問 S3** **資源。**

**4.****政策 (Policies)**

**政策是一種 JSON** **格式的配置文件，用於定義權限的細節。它詳細說明了誰（使用者、群組、角色）可以對哪些 AWS** **資源執行哪些操作（例如讀、寫、刪除）。政策是權限控制的核心機制。**

**AWS IAM****政策為JSON****格式的文件，政策就像規則清單，由它定義授權的詳細規則，這其中包含允許或拒絕等行為以及那些主體可以操作，還以條件約束，以下來拆分它具體的組成。**

**E**ffect

這是政策的核心，通常為兩種值，Allow(允許)與Deny(拒絕)，在預設的情況下，都是默認為"拒絕”的，如果希望特定使用者可以使用特定功能，就需要明確設置成”允許”。

**P**rincipal(主體)

**主體指是”****誰”****會受到政策的影響**

以下為受影響的常見值:

l   IAM 使用者（User）

l   IAM 群組（Group）

l   IAM 角色（Role）

l   外部 AWS 賬戶或特定 ARN（Amazon Resource Name）

**C**ondition(條件)

 

這是在政策中最靈活的一環，允許設定一些條件來進行限制訪問。比如說：
使用者必須從特定 IP 地址連接。
使用者必須啟用多重驗證（MFA）。
再比如，限制某些操作只能在特定時間內執行。

**A**ction(動作)

該政策主要是描述主體可以執行哪一些操作，比如說:

s3:GetObject：讀取 S3 存儲桶中的文件。

ec2:StartInstances：啟動 EC2 實例。

**R**esource(資源)

指的是允許什麼資源可以被進行操作。例如，允許使用者呼叫Amazom 储存貯體。

l   S3 存儲桶

l   EC2 實例

l   DynamoDB 表

IAM Role

I通過將 IAM Policy 綁定到特定實體（如 AWS 資源、應用程式或外部帳號）上，授予其對特定 AWS 資源的存取權限，而非針對一般的 IAM 使用者或群組設計。

IAM Role 的三種類型

IAM 角色（Role）是一種動態的權限分配方式，適用於各種複雜場景：

1. **AWS** **服務角色（Service Roles****）**  
   用於讓 AWS 服務（如 EC2、Lambda）代表你訪問其他資源，例如
   EC2 訪問 S3。
2. **跨賬戶角色（Cross-Account
   Roles****）**  
   允許多個 AWS 賬戶之間共享資源，避免多次授權。
3. **身份聯合角色（Federated
   Roles****）**  
   支持通過 SAML 等身份提供者的外部帳戶進行訪問，適用於企業內部與雲端系統整合​

IAM Security Token Service (STS)

介紹:提供臨時憑證，適合短期訪問需求。

特點:

憑證有效期短（15 分鐘到 36 小時）。

包含會話令牌、訪問密鑰 ID 和密鑰，無需使用靜態憑證。

通常與 IAM Role 搭配，用於臨時授權或跨帳戶訪問。

自動失效，無需手動撤銷;動態管理更靈活，無需建立固定身份。

API Access Key

介紹:適合程式化訪問 AWS 的工具（如 CLI、SDK）。

建議:

禁止將 Access Key 硬編碼進程式碼或存放於 EC2 實例中。

新的 Access Key 產生後，應立即廢止舊密鑰以減少風險。

  