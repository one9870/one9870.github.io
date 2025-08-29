---
title: "如何在阿里雲中有效防護DDoS攻擊並阻擋大量流量"
date: 2025-01-06 10:03:00
categories: ["阿里雲", "阿里雲Alibaba Cloud", "阿里雲教學30天上手"]
tags: ["阿里雲", "阿里雲Alibaba Cloud", "阿里雲教學30天上手"]
permalink: /posts/ru-he-zai-a-li-yun-zhong-you-xiao-fang-hu-ddosgong-ji-bing-zu-dang-da-liang-liu-liang/
---
**前提條件:**

已購買DDoS高防（中國內地）實例或DDoS高防（非中國大陸）實例

DDoS高防（中國內地）實例或DDoS高防（非中國大陸）

**中國站vs.國際站 差別:**

DDoS高防（中國內地）:端口接入有應用層防護增強功能

DDoS高防（非中國大陸）:端口接入無應用層防護增強功能

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj0SEoz5iJqiMaZrXdqHMI9Eu5W6MGTDsP3e4Jsi_5HN1GUypiKypIBwsXAd0W5VcKAan7mMZWdgRJkUkx2TUfTEH7va_whgypyoZryd7sdZTM5xjWa0xaxBWn63kykiurU_yhpY2vzCzp3_Ot3GTdiGJin7j8UFX6rrod_bta-jB7R71bB1KDplc6X8GE=w640-h70)](https://blogger.googleusercontent.com/img/a/AVvXsEj0SEoz5iJqiMaZrXdqHMI9Eu5W6MGTDsP3e4Jsi_5HN1GUypiKypIBwsXAd0W5VcKAan7mMZWdgRJkUkx2TUfTEH7va_whgypyoZryd7sdZTM5xjWa0xaxBWn63kykiurU_yhpY2vzCzp3_Ot3GTdiGJin7j8UFX6rrod_bta-jB7R71bB1KDplc6X8GE)

### **什麼是新建連接數?併發連接數又是什麼?何謂正常值?攻擊?**

**新建連線數 (New Connections)**

定義：新建連線數指的是在某段時間內，系統可以接受的新的網路連線請求的最大數量。

用途：此指標通常用於衡量一個服務（例如負載平衡器、雲端伺服器等）能在單位時間內接受的最大連線數。對於需要高並發的服務，必須確保該數值足夠大，以避免連線被拒絕。

例如，設定為 5000 表示每秒最多可以接受 5000 個新的連線請求。

**並發連線數 (Concurrent Connections)**

定義：並發連接數指的是同時維持的連接數。在任意時刻，系統上所有處於「連線」狀態的用戶端和伺服器之間的連線總數。

用途：此指標主要衡量系統的連接負載能力。如果並發連線數過高，系統可能會出現效能瓶頸，導致服務的延遲和逾時。

例如，設定為 100,000 表示系統能夠同時支援最多 100,000 個活躍連線。

**正常值（Normal Traffic）**

同時連線數（Concurrent Connections）：指在某一時刻，客戶端與服務端之間維持的有效連線數量。正常業務中的波動範圍在可接受範圍內。

新連線數（New Connections）：指每單位時間內建立的新連線數量。正常業務中的新連線數是穩定且連續的，反映業務請求量的增長。

**攻擊（Attack Traffic）**

瞬時性（Burst Traffic）：攻擊流量通常在短時間內突然激增，這會對系統造成衝擊，並遠超過正常業務流量的波動範圍。

沒有規律（Irregular Pattern）：攻擊流量沒有明顯的規律或可預測的模式，可能會以不規則的方式湧入系統，而正常業務流量一般呈現較為規律的變化模式。

#### 

### 提高DDos高防有效阻擋攻擊的方法

### 1.開啟QPS

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhEOb87HxPW6sk-2JjU0Mjdv_Pc01bw204JHbTEPy8vtKbLmY66XViRwDhMEZvEsrRmCzBaafinSaa30vVwrsacuKyQFkOAVKhphGaXU8UKAF2eIiBP1EzkEOL_C0CU97tPJXZZVfqqo7mW0wP21JUd1tiAVsrKv9MRoJ6eQBmflr9ffXtnOJ0zNNKPfgE=w640-h224)

![上傳進度：已上傳 191047 個位元組 (共 191047 個位元組)。](/assets/images/transparent-1.gif)](https://blogger.googleusercontent.com/img/a/AVvXsEhEOb87HxPW6sk-2JjU0Mjdv_Pc01bw204JHbTEPy8vtKbLmY66XViRwDhMEZvEsrRmCzBaafinSaa30vVwrsacuKyQFkOAVKhphGaXU8UKAF2eIiBP1EzkEOL_C0CU97tPJXZZVfqqo7mW0wP21JUd1tiAVsrKv9MRoJ6eQBmflr9ffXtnOJ0zNNKPfgE)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgLyT9Ti5VP-bqkyyPRWyCft7ReUfBB_xHW67_36EJW1lAcYnCzkur0opq79HRBI-ckcSFistPOfal7vQi2nwuxwbVQmqdj1nct6THe8s_cDRjswdef8VnANSSUTnVV1LnHFBI-g4VvLhMuovcCSBj2LCC3NoSzHYmdP3dnIjgOtil0nvXqceeRZOolrjc=w640-h256)](https://blogger.googleusercontent.com/img/a/AVvXsEgLyT9Ti5VP-bqkyyPRWyCft7ReUfBB_xHW67_36EJW1lAcYnCzkur0opq79HRBI-ckcSFistPOfal7vQi2nwuxwbVQmqdj1nct6THe8s_cDRjswdef8VnANSSUTnVV1LnHFBI-g4VvLhMuovcCSBj2LCC3NoSzHYmdP3dnIjgOtil0nvXqceeRZOolrjc)

啟用QPS超過基本的QPS和連線數後才會產生費用，如果不想開啟彈性QPS，或是可以點選右側的升級，直接升級QPS和連線數，一般彈性QPS適用於偶爾流量的增加，直接升級QPS是業務一直都有增加

彈性QPS計費標準說明可參考：

https://www.alibabacloud.com/help/zh/anti-ddos/anti-ddos-pro-and-premium/product-overview/billing-of-the-burstable-qps-feature?spm=a2c63.p38356.0.i0

### **2.設置四層AI防護**

點選"防護設置"→"通用防護策略"→"非網站業務DDos防護"→"AI智能防護"點選設置

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiTdt-vvPcT3Z0bltkZU0ETn6iWJNsaAX7h-z-WfGcSGUudsgdxU1WdnIznakwH4rmbgI_df8kjfiD3IdhOsGe7DPGIA3-jBkoXl6p8o6RDb4cKpCKM7UD0VvR0M3FkPfbZqkfaM_HmJ0SqTdyPVVCsW5i-oZvNct_3d5mJ1_CwrvHMw7g4Yq4GIwXxlJk=w640-h328)](https://blogger.googleusercontent.com/img/a/AVvXsEiTdt-vvPcT3Z0bltkZU0ETn6iWJNsaAX7h-z-WfGcSGUudsgdxU1WdnIznakwH4rmbgI_df8kjfiD3IdhOsGe7DPGIA3-jBkoXl6p8o6RDb4cKpCKM7UD0VvR0M3FkPfbZqkfaM_HmJ0SqTdyPVVCsW5i-oZvNct_3d5mJ1_CwrvHMw7g4Yq4GIwXxlJk)

  
參考資料:

https://help.aliyun.com/zh/anti-ddos/anti-ddos-pro-and-premium/user-guide/configure-intelligent-protection?spm=a2c4g.11186623.0.preDoc.2530240f3t4vi5

### 3.對四層進行源限速和目的限速策略

點選"防護設置"→"通用防護策略"→"非網站業務DDos防護"，可進行源限速和目的限速。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiVKL2T6ikO0T8Gs-Hd1TU1oUvsl99Mml-l9I21hyyCvu1Z7_FnsQ4Q6MsPs9xF5Xgmt96fMRPkFHG1YiBm9HwDWJ_pm_DI0sXxCHCTvMFbI1q_4Mb8CUoqw-KCsNiLrosLBu--idz76emsz3-OijfLQHHisXuvsjax-10fa9CZwdr5NRw2EPxLc-1ZLVU=w640-h362)](https://blogger.googleusercontent.com/img/a/AVvXsEiVKL2T6ikO0T8Gs-Hd1TU1oUvsl99Mml-l9I21hyyCvu1Z7_FnsQ4Q6MsPs9xF5Xgmt96fMRPkFHG1YiBm9HwDWJ_pm_DI0sXxCHCTvMFbI1q_4Mb8CUoqw-KCsNiLrosLBu--idz76emsz3-OijfLQHHisXuvsjax-10fa9CZwdr5NRw2EPxLc-1ZLVU)

詳細設置可參考:

https://help.aliyun.com/zh/anti-ddos/anti-ddos-pro-and-premium/user-guide/create-an-anti-ddos-protection-policy?spm=a2c4g.11186623.0.nextDoc.7ee07c5cjsNuWL

### 4.針對部分IP進行黑名單，白名單設置

點選"防護設置"→"通用防護策略"→"基礎設施DDos防護"，進行黑名單及白名單設置。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEguryNxgSyoz9WWjabIKX3DEGknCfFGDVKapfGJ1xf6BT65G_qL1e12NwLVPT2yAOLTQZLErVmVRy_jXQ_VBDztZnUJr7iTNVZZ2_1SvNn4ZFhv8ARCs2YsUCQ3lBF5kjyXHFEg2DzdDPPwmjJEjw-utSYUhCnvnTVJdPMECxhqLTlN4Ghk3xiohzPm5bI=w640-h428)](https://blogger.googleusercontent.com/img/a/AVvXsEguryNxgSyoz9WWjabIKX3DEGknCfFGDVKapfGJ1xf6BT65G_qL1e12NwLVPT2yAOLTQZLErVmVRy_jXQ_VBDztZnUJr7iTNVZZ2_1SvNn4ZFhv8ARCs2YsUCQ3lBF5kjyXHFEg2DzdDPPwmjJEjw-utSYUhCnvnTVJdPMECxhqLTlN4Ghk3xiohzPm5bI)

黑名單：

自訂的黑名單：永久生效(目前黑名單最多封鎖7天，而非永久生效)。

智慧防禦演算法下發的黑名單：DDoS高防智慧防禦演算法標記的惡意IP，有效期限由智慧防禦演算法動態計算，最短5分鐘，最長1小時。如果惡意IP在有效期限內有持續的惡意攻擊行為，DDoS高防將自動延長有效期限。

白名單：僅支援自訂的白名單，永久生效。

參考資料:

https://help.aliyun.com/zh/anti-ddos/anti-ddos-pro-and-premium/user-guide/set-blacklist-and-whitelist-for-anti-ddos-pro-instance-ip?spm=a2c4g.11186623.0.i8