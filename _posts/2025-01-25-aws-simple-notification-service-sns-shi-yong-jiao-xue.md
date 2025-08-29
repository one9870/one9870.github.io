---
title: "AWS Simple Notification Service (SNS) 使用教學"
date: 2025-01-25 08:10:00
categories: ["AWS", "AWS教學30天上手"]
tags: ["AWS", "AWS教學30天上手"]
permalink: /posts/aws-simple-notification-service-sns-shi-yong-jiao-xue/
---
### AWS Simple Notification Service (SNS) 使用教學

---

## **什麼是 AWS SNS？**

AWS SNS 的主要功能是將消息從發佈者傳遞到訂閱者。這可以用於各種通知場景，例如：

1. 監控警報（如 EC2 實例的健康檢查失敗）。
2. 實現微服務之間的消息傳遞。
3. 用於多渠道用戶通知（電子郵件、簡訊等）。

SNS 運作的核心是 **Topic（主題）** 與 **Subscription（訂閱）**：

* **Topic**：消息的發佈點。
* **Subscription**：接收通知的端點（如電子郵件、SQS、Lambda 等）。

---

## **使用 AWS SNS 的步驟**

以下將介紹如何設置並使用 AWS SNS：

### **步驟 1：創建 SNS 主題**

1. 登入 [AWS 管理控制台](https://aws.amazon.com/)。
2. 搜尋 "SNS"，進入 Simple Notification Service 主頁。
3. 點擊 **Create topic**。
4. 選擇主題類型：

   * **Standard**：適用於大多數應用，支持最多一次交付。
   * **FIFO**：適用於需要消息順序和確保唯一交付的場景。
5. 填寫主題名稱，例如：`MyTopic`。
6. 點擊 **Create topic** 完成創建。

[![](/assets/images/Snipaste_2025-01-25_23-49-44.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiF_1DvkZQlsLZUPUSwDFThUMPSdkLwbKrUPdGB_F_OizVhPlVVxl3rxWWaWA4EAMcjpQLrRpqQE0wQRQUA3e0G8fAlBP9xYvKB2BZnU57cKGhcwNH-d9N7ESpNqiv6OCO-75Wdk88IXpaaCg_5VuZ80AjWp197sP1ypClLIlJxmitw03o9EStzUoh1xZE5/s1741/Snipaste_2025-01-25_23-49-44.png)

  

1. ### **FIFO跟**標準是什麼，他們差在哪?

   ### **FIFO（先進先出）**

   * **重順序、精準性**：消息一定按順序來，不會亂掉，也不會重複。
   * **適合**：像銀行交易、庫存管理這種需要「一條一條，不能亂」的場景。

   ### **標準**

   * **重速度、大量發送**：消息送得快，但可能順序亂，偶爾會有重複。
   * **適合**：像促銷通知、警報這種需要快速發送、對順序沒要求的場景。

   總結：  
   FIFO 就是「一步一步來，順序最重要」。  
   標準就是「效率優先，快就對了」。

[![](/assets/images/Snipaste_2025-01-25_23-50-20.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFU61JfOkAbQmYzrBf2Bg3ZP1xCbxNJd1_u3gK3VsRLDPKQIDOIu2G2CCjDrNUkdOXFcO7N9nptdMmpcYX_6kGzEBZI4WFEw4eIpo7AlpCLQpyhiaMPdQXsvu1M30J4b-rJIxryc2Bm_0gQ0jewiLXvYKsh-AHMZ1wkWvL70lM68lpGooL69K-AAe5gjoY/s1741/Snipaste_2025-01-25_23-50-20.png)

---

### **步驟 2：新增訂閱者（Subscription）**

1. 在剛剛創建的主題頁面中，點擊 **Create subscription**。
2. 選擇協議（Protocol）：

   * **Email**：將消息發送到電子郵件。
   * **SMS**：發送簡訊。
   * **AWS Lambda**：觸發 Lambda 函數。
   * **Amazon SQS**：將消息發送到 SQS 隊列。
3. 根據選擇的協議填寫目標終端。例如，若選擇 Email，請輸入接收通知的電子郵件地址。
4. 點擊 **Create subscription**。
5. 如果選擇 Email 協議，請到郵箱查收確認信並點擊確認連結完成訂閱。

[![](/assets/images/Snipaste_2025-01-25_23-56-36.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjv81Yx3GTYvL3CkFSU5KPNsVf4Eg5Kr_Ak12I-uKfrwASZPQMqQsJIAV35Qei-QNL2kXGCXuspcdPzJBFJUigtj4cuLbgrGfI3xJD4c_4AxQWonTMSaetMlEcitoHSjghs-bS_TZ9Q299pUaD8HzN5Ue5sqaKzR2y7HnkeCifybErJoo67YKNP9MCH2_EO/s1741/Snipaste_2025-01-25_23-56-36.png)

  

---

### **步驟 3：發佈消息**

1. 返回 SNS 主題頁面，點擊 **Publish message**。
2. 填寫消息內容：

   * **Subject**：消息的主題（僅限 Email 使用）。
   * **Message**：消息的內容。
3. 點擊 **Publish message**，訂閱的用戶或終端將接收到消息。

[![](/assets/images/Snipaste_2025-01-26_00-04-07.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmAXxWAd7O6L2TvFncxEsYDPT72in6iXXImW5dxh2fYTfXkhBgICjpyNsX66LHCIyoAgU5NHMKqvnXf3D5WYvGz1_24Y9bD9_WCSZddDF06rE_i16sWmOXK62uJKsIKxfznLZ5a1I34VUF0lXInvmx_dTMebcI4Zp86ozN5Bm17BfBViIlawTb8OGWiNpL/s1741/Snipaste_2025-01-26_00-04-07.png)

  

---

## **進階功能**

### **1. 整合其他 AWS 服務**

SNS 可以與許多 AWS 服務整合，例如：

* **CloudWatch 警報通知**：當 CloudWatch 監控檢測到警報條件時，自動發送 SNS 通知。
* **AWS Lambda**：使用 SNS 作為事件源，觸發 Lambda 函數執行處理邏輯。
* **SQS 隊列**：將 SNS 消息發送到 SQS 隊列，實現消息的緩存或延遲處理。

### **2. 設定過濾策略**

SNS 支援基於消息屬性的過濾訂閱。例如，僅當消息中包含某個屬性時，才向特定訂閱發送通知。

#### 操作步驟：

1. 在訂閱設定中，新增過濾策略（Filter Policy）。
2. 例如，若您發佈的消息中包含屬性 `type`，值為 `error`，則可以設置過濾策略如下：

   ```
   {
       "type": ["error"]
   }
   ```

---

## **最佳實踐**

1. **使用 CloudWatch Logs 監控 SNS 消息發佈情況**：確保消息發佈與接收的成功率。
2. **採用 Dead Letter Queue (DLQ)**：處理無法送達的消息。
3. **設置加密**：使用 AWS KMS（Key Management Service）加密 SNS 消息，確保數據安全。
4. **設置速率限制與重試策略**：避免過載訂閱終端。

---

## **常見問題**

### **1. 為什麼電子郵件收不到通知？**

* 確保電子郵件訂閱已確認。
* 檢查垃圾郵件文件夾。
* 若使用沙箱環境，請將電子郵件地址添加到允許列表。

### **2. SNS 的定價如何計算？**

SNS 的費用包括以下部分：

* **消息發佈費用**：根據發佈消息的次數計費。
* **傳送費用**：根據選擇的協議（SMS、Email 等）計費。

詳細價格可參考 [AWS SNS 價格頁面](https://aws.amazon.com/sns/pricing/)。

---

透過以上步驟與功能介紹，您應該能夠輕鬆開始使用 AWS SNS 實現高效的通知與消息傳遞！如果有其他問題或需要深入討論特定場景，歡迎告訴我！