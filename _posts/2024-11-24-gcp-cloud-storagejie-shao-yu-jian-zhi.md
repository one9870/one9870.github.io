---
title: "GCP Cloud Storage介紹與建置"
date: 2024-11-24 15:21:00
categories: ["GCP", "GCP教學30天上手"]
tags: ["GCP", "GCP教學30天上手"]
permalink: /posts/gcp-cloud-storagejie-shao-yu-jian-zhi/
---
Google Cloud Storage 提供了**4 種儲存空間級別**，幫助您根據資料的**存取頻率**和**使用需求**，選擇最符合需求的方案。透過選擇適合的儲存級別，您可以在**性能**和**成本**之間取得平衡。

以下簡單介紹這 4 種儲存級別，了解它們的用途和差異：

### **標準存儲（Standard）**

* **特點**：快速存取、低延遲，適合頻繁使用。
* **適用場合**：需要隨時存取的資料，例如：
  + 網站靜態檔案（圖片、影片）。
  + 即時應用程式的數據。
  + 數據分析資料。
* **存取頻率**：**高頻率存取**。

  ### **近線存儲（Nearline）**

+ **特點**：存儲成本較低，但設計用於每月存取一次的資料。
+ **適用場合**：備份或偶爾需要的資料，例如：
  - 公司每月的報表檔案。
  - 備份和災難恢復的資料。
+ **存取頻率**：**每月存取 1 次**。

### **冷線存儲（Coldline）**

* **特點**：成本更低，適合每年存取 1 次的資料。
* **適用場合**：需要長期保存，但不常用的資料，例如：
  + 歷史記錄或資料歸檔。
  + 長期備份，例如季度或年度的數據存檔。
* **存取頻率**：**每年存取 1 次**。

### **存檔存儲（Archive）**

* **特點**：成本最低，設計用於幾乎不存取的資料。
* **適用場合**：需要保存多年的資料，例如：
  + 法律文件。
  + 長期保存的醫療紀錄或研究數據。
* **存取頻率**：**極少存取（例如每幾年一次）**。

比較圖

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg5PT0p0Ddiyw0SEKPqdcBGMjwBbfwve9CTXPxy4r7PYSqyty1xEgSQiK5LJAeUfqj7jbJLpGCHu0GK5ka4MvolI18pspECtlntbvKgq9PJkbxekfWZzo2XRQ2tCdhu0V06bKV2b8oN5LiyodeLM6whhvptlidrjnivANmlsJhePYeN3ipWQOdpY95uKD8=w640-h181)](https://blogger.googleusercontent.com/img/a/AVvXsEg5PT0p0Ddiyw0SEKPqdcBGMjwBbfwve9CTXPxy4r7PYSqyty1xEgSQiK5LJAeUfqj7jbJLpGCHu0GK5ka4MvolI18pspECtlntbvKgq9PJkbxekfWZzo2XRQ2tCdhu0V06bKV2b8oN5LiyodeLM6whhvptlidrjnivANmlsJhePYeN3ipWQOdpY95uKD8)

## Cloud Storage 教學：儲存級別設定

1.查找GCP "Cloud Storag"後點選進入介面

[![](/assets/images/螢幕擷取畫面 2024-11-25 064827.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHMu3Lv9pD4iL1BT0rWMC7epBZaPqEzkuMSQHCyeGUm0d5gvT-ldKWDfMUS_nlB_kca_Hs9zwXNpv4n-nLqya78ZH5LvX18NNIINjPo9JnSimLPvrBNkzVhKF2Hyfew3xGsdvAK1Fxnu1qeOrX4sTdcHP0ut4ZCKlLr9xTLGycBCZMeL8pZUf8inQ38kQ/s759/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-25%20064827.png)

2.選擇"存儲桶"後→點選"創建"

[![](/assets/images/螢幕擷取畫面 2024-11-25 065605.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgymZKH-otWsSC9gjgCsHUQaxTeJ03NrODbPHEUQxGJyoA9qR_RYDxCURkkAGUdc-D4U7CNeR68iEu-DSlAfTYu4hACzlPruNqMGRw-6bcUdjyz1eYh6aDAdTtnGu98n26p-D_7mwc8Lk4A2jGkGESOzi8Yt6IVDxkApVUDMNCokGcYOxcoZK4Izpr1s8c/s964/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-25%20065605.png)

3.選擇一個全域的永久性名稱，每個名稱不可相同，如果取的名稱已存在，Cloud Storage 會出現報錯（如下圖）。其他關於命名的規則，可參考 GCP [官方文件](https://cloud.google.com/storage/docs/naming-buckets?_gac=1.11323904.1594361871.EAIaIQobChMIm_Xn4oTC6gIVCXkqCh1SwwonEAAYASAAEgI3VPD_BwE&_ga=2.13074743.-1048318368.1571714493)，完成後點選"繼續"  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgA0rTv5yYqngFqpml6dD5k16LixAQjvAED8ndpkf6mpk43SkNkAQd2-x7BRBHRaKc_clJfOs4ujJthgzw5iXHoHfahtpX6oB0o355NNSVGPzgrOPAlO72jIXMm68rvrQNsvYwNVq09zNsTnzK3C5gWj2Z6U4KUj0JPaIq5cyFkoiQUPt2tgTDHXjix8TA=w640-h184)](https://blogger.googleusercontent.com/img/a/AVvXsEgA0rTv5yYqngFqpml6dD5k16LixAQjvAED8ndpkf6mpk43SkNkAQd2-x7BRBHRaKc_clJfOs4ujJthgzw5iXHoHfahtpX6oB0o355NNSVGPzgrOPAlO72jIXMm68rvrQNsvYwNVq09zNsTnzK3C5gWj2Z6U4KUj0JPaIq5cyFkoiQUPt2tgTDHXjix8TA)

4.依需求選擇資料儲存預計建立的國家&區域，完成後點選"繼續"

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiiEaWTsu3fQZyyd1fJW28n6PPPMbgJ6HKjzuBGnZai5WsX3BPKGMNhr5lbwFCYcV2dvOSrwm-vtu08nhZdNSFzBpf-UdrMSVwzAvWX3Uri3yHdMc457QCllmONN5rl-VYMB7ynx4Cofo22EHHIUNULJt5_BE5WbEDZoPYA3KyczNOG4KqwljO5VDzEpV4=w640-h482)](https://blogger.googleusercontent.com/img/a/AVvXsEiiEaWTsu3fQZyyd1fJW28n6PPPMbgJ6HKjzuBGnZai5WsX3BPKGMNhr5lbwFCYcV2dvOSrwm-vtu08nhZdNSFzBpf-UdrMSVwzAvWX3Uri3yHdMc457QCllmONN5rl-VYMB7ynx4Cofo22EHHIUNULJt5_BE5WbEDZoPYA3KyczNOG4KqwljO5VDzEpV4)

  
5.依需求選擇儲存類別，完成後點選"繼續"

[![](/assets/images/螢幕擷取畫面 2024-11-25 070726.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgK9MmKHYJv7seSv2RwFx15WMb6g_CgumwTGOzAsY3PtcNWyNom2PS8MkT0WoFOEXLdUAMTZQVNbyuFskkvYSgb4WxLzRjo6lZr9Vefwsr9oBMeOfHZbkjYiWCignWhIpCXSrnFzqzRip6iWxyYyUKpNyBQux-1jw59CoG5Bjh94c5ClSSyroazIrhgzeI/s580/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-25%20070726.png)

  

6.選擇是否公開此Storage，可進行設定特定的存取權限，完成後點選"繼續"

[![](/assets/images/螢幕擷取畫面 2024-11-25 070849.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZBhQUlgoE9SYGoG42XBh1IM6u2YC3r-Iy8-bCIZ-PtYIBIgW6FJAWXbeuBx8quf5uzLoSd9qwpjbDLz7u6uPgNPKKpF-KigCLyeghb6TPAmMFDYiC9-1YO2p3UeTyRoK4oioQKB9JXp3j3XwLJqR2cEruD4-kyqgA_O24gvK-NIOek5AuxnBV_6DZvBw/s588/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-25%20070849.png)

  
7.選擇附加資料保護選項，以實現額外的保護。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgKK2uU9awbjg5Z5cxV4e40_I8nPsYsicljTDstJayPouXiPS-9vmvT3-pu0Ixe_zjpRNKZGvHub1dWdM3J0O94G6_3Gh_uQwiOof-nuNqXtQ3MOijf7KNyhbx23ramYn-aoJTcN6bDUuWYvq4AOnOE5hdHaNNoAwrUreXkexB2d_BJLmYklWcaWzqrnCo=w640-h509)](https://blogger.googleusercontent.com/img/a/AVvXsEgKK2uU9awbjg5Z5cxV4e40_I8nPsYsicljTDstJayPouXiPS-9vmvT3-pu0Ixe_zjpRNKZGvHub1dWdM3J0O94G6_3Gh_uQwiOof-nuNqXtQ3MOijf7KNyhbx23ramYn-aoJTcN6bDUuWYvq4AOnOE5hdHaNNoAwrUreXkexB2d_BJLmYklWcaWzqrnCo)

  
8.完成後可查看預估費用

[![](/assets/images/螢幕擷取畫面 2024-11-25 071333.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtHzSZz9EjNm7DrQ7XbZluD9_OFk3qUsMcZJDudQGcIaIK4jeICgeUVb8Uo8_ChyRGQNQSWqBJDPn5Lv9AoaUc4gyJGAoCbACIIacFNSlynhL0-Ie1ifn1MPNuYwbSpt20nTQLDvVulh0grkrZ878VoKky581d-tVF2qEvx6sv0tYRBIV0R7Z5psAvITI/s564/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-25%20071333.png)

9.完成後點選畫面最下方"創建"

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgbo_KCgnhUGVuYzam7Zu3ufEXXeFqkBq_sjebt5Khc34kPTqA8LlkvXsFd1iRx4kT_p7AL04-0_NlSJQfWTx-vcXtvA4PYw4kNT_FMESn8BkwoMbr7TbH4UO4PstUWL4vKsDbHTcavW_0H-hnSvqfIiY80GIya1k1aiqHo8-RBdWeGiOrPrMUUfvLvnkk=w640-h170)](https://blogger.googleusercontent.com/img/a/AVvXsEgbo_KCgnhUGVuYzam7Zu3ufEXXeFqkBq_sjebt5Khc34kPTqA8LlkvXsFd1iRx4kT_p7AL04-0_NlSJQfWTx-vcXtvA4PYw4kNT_FMESn8BkwoMbr7TbH4UO4PstUWL4vKsDbHTcavW_0H-hnSvqfIiY80GIya1k1aiqHo8-RBdWeGiOrPrMUUfvLvnkk)

  
10.創建完成

[![](/assets/images/螢幕擷取畫面 2024-11-25 071955.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggkd02K4M42fHW13m9IRNrTlKXJkFRBl12VD1QfsiJH0ugxvlMnbwHPxy6Bt0a71xelDcjAfrEZiU1Z6dA0RhoKLmmW3ChPyaQgZ03v04fWa7HpRLH5kuHCeifeHwHy-xFppo7IWfOdOrj3OfqZCN0Dq-N4R0wwma7nZvRbBjTl6LsPSsCmAvwyrx6vMs/s1563/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-25%20071955.png)

  