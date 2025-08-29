---
title: "如何查看GCP線路的BGP工作階段狀態和 Cloud Router 工作監控圖"
date: 2024-11-25 22:56:00
categories: ["GCP", "GCP教學30天上手"]
tags: ["GCP", "GCP教學30天上手"]
permalink: /posts/ru-he-cha-kan-gcpxian-lu-de-bgpgong-zuo-jie-duan-zhuang-tai-he-cloud-router-gong-zuo-jian-kong-tu/
---
1. 首先選取要查看線路的專案，然後點選左邊列表的網路連線中的互聯網路

   [![](/assets/images/image001.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj16XpR93qJSyFb7wil27jUkDly8TpyXxtDqtS4VY0F-9K5_q75VyIrokCXrfW30995GZ7465ZA9TsghAAfpdP8yRwzzfKQ7K7BY7jRKsZvVzAW0bkEunAFaikL_qrRmuF6vtdN68MgDpMzcbVdipxfeU4AzLcSwrN5DNup5ceRTC0Nt-scOcaFo0gALaI/s1585/image001.png)
2. 確認要查看的線路名稱，再點擊右邊的查看VLAN連結詳細資料

   [![](/assets/images/image003.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjy7rP28gbJAW76vsnn2DCDHSY53HtmzeOb3DujDwlrOg8Eww8ClDbGL8qobTVaKc6RVWdYwEcnIWSTPMN2QF2OaFN7eWTo0KNOSq7lP0VHuQgx7d2IDbMxt0mW0c1wf8oxHaoGBdiGZ8-Pj-nPkkVWrDQD8mlzGeQvMCo0Gbc5rCiXTnqFwb_a5o3Uc_Y/s1581/image003.png)
3. 或是直接點擊線路名稱，再選監控

   [![](/assets/images/image005.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivEXRgYK3Sh4WHRW-OHMVswUOhugj8OJWNeC6iYSmBzQ__LtS-qS1SHmbjJqSkaPZtY8_V_HnidqHACx4dk2iY3kZkopRZEmO-mWbN6E1o-uhfur-Fdfsaq-tOGdlYf5bsvmiZRlYqfquJrnMHT_M6iyl5EHN-V7j6GvhxdK0C2OA-J2-rLTRcCkv_-8M/s1580/image005.png)

   [![](/assets/images/image007.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-QPoaq_RjM2o6fJf1liALFUAifTldX42EyFj2s6tB7xJA_FzACE7D6q4mgQLBU38_KcTxf7RmXvBOGyAgNPUE4hlXNOmtdrsjkejgvgYlx0CCgFUYTh_IlMWSLvZ1Y4kr_xzTgooshyphenhyphenxkgCZGuvkSkPl7ynzd38pdBkkrcdtAP0lOXKDAjENr67tZp1g/s1594/image007.png)
4. 即可查看線路狀況

   [![](/assets/images/image009.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpBAmhdAXz6OXmYxXnG4Msvrpv42KXenqXxEiiySY6CYEMbBPATuAeNOyWdJ7OPwr-GmYhdUdAMgwSq7pLT4bbuLYnaWsOt6d-EA9g_aa7VGdI0e3SgM9M2a_IhPxBoNpFDD3kj2GfwlkQAv5Egcaes9FliR6g4BFTJEmAlqfRPJThcoAhKq53x2hPt2c/s1591/image009.png)
5. 其中BGP工作階段狀態和Cloud Router工作圖表，會顯示線路是否正常運作，若如下圖波折起伏不定，就代表線路異常。

   [![](/assets/images/image011.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrW5BJlTQgktNRKJW33L8KB3ehX3geI3ljsrwke3r92nl2zXqFzBEeDvVj3dlHUccRnO6GT1-d662XKLC0itgws9iZ0dUNItuTkm4_VNHogaejiEtyrcDoUyFvogUfGQMOTCBS1yK_WcHn8K6RFIfdY8EFZvS8Vwk2Tf_NFp_y8Pk-CB_IVwXlSAoJ024/s653/image011.png)
6. 正常運作的線路，狀態值應如下圖一樣維持在1

   [![](/assets/images/image013.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYjg09P-Rr5-HUggdONHXXtmRd3q8Eo15dGDiC9YNCdfviSUjXYYKAx-CxoRZ-tT_708E3Wv8lOh07M5QTOBjHDaxhh6RmBtqOs4yn6TptSyDxOfF8zhn5_ztIlCjkiwGkCct1eRNw-z8CT9YGNdxQBBv8Molhqjlblwayf-0mpxpti8x3_dXuHzrMQGc/s639/image013.png)