---
title: "AWS CloudTrail 介紹與如何將事件儲存至S3"
date: 2024-12-19 06:48:00
categories: ["AWS", "AWS教學30天上手"]
tags: ["AWS", "AWS教學30天上手"]
permalink: /posts/aws-cloudtrail-jie-shao-yu-ru-he-jiang-shi-jian-chu-cun-zhi-s3/
---
AWS CloudTrail AWS 服務 是可協助您啟用您的 AWS 帳戶. 使用者、角色或 AWS 服務所執行的動作並記錄當中的事件。事件包括在 AWS Management Console、 AWS Command Line Interface和中執行的 AWS SDKs動作APIs。

CloudTrail 提供三種記錄事件的方法：

### 1. **事件歷史記錄**

提供過去 90 天內 AWS 區域管理事件的可檢視、可搜尋、可下載且不可變的記錄。* **特點**：
可以篩選單個屬性搜尋事件。  
自動獲得存取權，無需額外設置。

### 2. **CloudTrail Lake**

受管理的資料湖，用於擷取、儲存、存取和分析使用者和 API 活動，主要用於 AWS 稽核和安全目的。* **特點**：  
  事件將轉換為 Apache ORC 格式，適用於快速資料擷取。  
  可建立事件資料存放區，保留時間最多 10 年（視定價選項而定）。  
  可將 S3 儲存桶中的現有 CloudTrail 日誌匯入事件資料存放區。  
  支援透過 AWS Organizations 跨帳戶設置。  
  提供儀表板視覺化熱門事件趨勢。

### 3. **追蹤 (Trail)**

用於擷取 AWS 活動記錄，並將這些事件交付至 Amazon S3 儲存桶，且可選擇傳送至 CloudWatch 日誌和 EventBridge。* **特點**：
支援單一或多個 AWS 帳戶，並可與 AWS Organizations 集成。  
可選擇將事件送至第三方安全監控解決方案，或使用如 Amazon Athena 進行搜尋和分析。  
可選擇記錄 Insights 事件 以分析 API 呼叫的異常行為和錯誤率。

費用比較

事件歷史記錄：免費。  
CloudTrail Lake：依據資料儲存和查詢量收費，會產生儲存和查詢費用。  
追蹤 (Trail)：免費將事件傳送至 S3，但 S3 儲存會產生費用。

#### CloudTrail 事件紀錄的保留時間

**CloudTrail 會自動記錄並儲存過去 90 天內的所有帳戶活動。**可以透過 CloudTrail 控制台查看、分析和下載這些紀錄。

如果需要查找**超過 90 天的紀錄，可以使用其他儲存選項來保存日誌資料。**

**如:S3****儲存桶****、CloudWatch Logs**

**S3儲存桶**  
可以透過設定 S3 儲存桶的 **儲存生命週期規則**，來管理日誌資料的保存與過期。這意味著，您可以設置規則來自動移除過期的日誌，或將其存放在更便宜的儲存類別中（例如 Glacier）。

CloudWatch Logs

**沒有預設的儲存時間限制。在預設情況下，日誌會無期限保存。**

保留時間管理：您可以隨時調整每個日誌群組的保留時間設定，以確保日誌資料根據業務需求或合規性要求保留。

### CloudTrail使用S3儲存桶進行存放說明

(可選擇進行**新建S3儲存桶**或**使用現有S3儲存桶**，此處已先建S3後設定的方式進行說明)

1.於AWS主控台中，搜索"S3儲存桶"，並"點選"

[![](/assets/images/001.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjGabmjnV8N5a0XZ0q2DSF2cjBXn9giGgJ82eEd6wnOJHaLGTzMY-xLKMQ7v9AqFXdErKeZ7Kpcu0kv2pGsBb3auywNcZZw6vjRlYmDzQltsUu1VRbDS9cgn1S5YisLhLZcIYNjaOjezhsCnhcxqpYOxTgfqywk1WLrZh4Qy9vJE2B2homocIYSal5gJs/s990/001.jpg)

  

2.選取"建立儲存貯體"

[![](/assets/images/002.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDxu4SKk9nNCjDLQFI-CmIRvurAnMM6VNXaCSevtn98M9AQxjyMqB6D10z0sg-KdEeT43H4G_UNHNllaXvOkElLaHbR6ltZP405qknAK9fWK2f1I5gI4YYHRlkxIRfCSGLHtUZTnwZbVi6kBZFAw0MnkVM3v9pWKPDc_GnK23hgwnnO0R8JTAu77UQ-dM/s1565/002.png)

3.依需求選擇後，點選建立  

[![](/assets/images/003.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZLC0ufoX6m1HFiWRYQXXRKDJ5sDqWqv7_57qOqrrFUTiFyYm2zWhNZzOoMCZd_L0ax590zscTkXryHiI_Hkfiv6HuNoJfxEq07uyHOZ1Qk7oO97NzqmZZDWgNrRg_4B-CCX9zbE-y34k8s4G_gMDfQ3c12F33l0dh-f441ixTsJnWNbkENO9LOqyMFhI/s1562/003.png)

  

4.建立完成後，於上方搜尋攔查找"CloudTrail"

[![](/assets/images/004.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTalfnYE4oaVawotNqUaaYMOSU6LIMapXXf1zLxnWeZvJC3YWMPA69xZUMpIY-yZo8_nMXDL1DEwgLaNPylWjNZg9kyEnpRX0XbD1t7L9qz5D95ktIe1Lo3dFa-LnY46QrZFPFme9NdFsruHcF1N7G1A6etUDPApTSjVxOiqS2NLA9gJT4Hy-FJeyLxiE/s1559/004.png)

  

5.於左側選項選擇"線索"→"建立線索"

[![](/assets/images/005.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPMTVrJjYKphA8WERJnfBSyzji3YtPXajrK7ymmFVLceDdL4CuUznPq0baL0AmBlgOIXr2o8FZkm6Up1-JXd15GtkyloTqLBXS8RfvwNZGTzIkpasqsaaJNgivCGiVgFBojyPdf-KTTDk06nm_i_FWQ5UkCdVocZYRXrbTwWKbFlZ5NQqzIhD3Ee-72yI/s1575/005.png)

  

6.依需求勾選設定，此處可選擇進行新建S3儲存桶或使用現有S3儲存桶，完成後點選"建立"

[![](/assets/images/006.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1P-a0k244iriVDJH8_Aqarrurj9focyvLdOVG5gc0ZK37ghN_rmsNG6J8nNvl9HkSqrPPjx8YfRboSreR1-IjNl35OisFKr4c89nCqqlURFS8r1vvA9Sdy0N5PC-W9iTcU_d_Wx3Wf3DhgToSgNP3fY_hs6ef7d-r8ztC2qohrhoiA0E04eaCe2ppnGc/s1560/006.png)

  

7.建立完成

[![](/assets/images/007.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_sc4wvaSlZqrS_R8Q4o0mn8-BlUmUNHPfK_EzsSvI9MKurd7taJrN5ICoBhuuGoD4WGeyiKOI5ZObA_uub9d1tKqE4I0quuu5Bvqsww3U93wY7D7cRqXcJfsnRDJiqKixv8U5txntDdbyl7gwx0Y_c3tHfW6E99cdn6eHPZDlaSg9p3jXuwH9HVlk3VM/s1568/007.png)