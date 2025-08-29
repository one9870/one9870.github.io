---
title: "[騰訊雲]管理者如何完成賦予使用者權限"
date: 2025-01-23 01:39:00
categories: ["腾讯云 Tencent"]
tags: ["腾讯云 Tencent"]
permalink: /posts/teng-xun-yun-guan-li-zhe-ru-he-wan-cheng-fu-yu-shi-yong-zhe-quan-xian/
---
此類設定需要帳號管理者登入騰訊雲端控制台，並進入 IAM 管理頁面。在控制台左上角的搜尋方塊中輸入「身分與存取管理」，或是點選「存取控制」選單來進入 IAM 管理頁面，接著即可進行相關操作。

以下介紹兩種常見的權限賦予方法：

以下提供兩種基本方式完成權限賦予的動作：

一、以“建立新使用者”方式創建並在建立期間增加權限：

帳號管理者在左側選單中選擇「使用者管理」，然後點擊右上角的「新增使用者」。

填寫使用者資訊（如使用者名稱、登入方式等），完成後點擊「確定」。

[![](/assets/images/創造新使用者.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrrP-NeSpyz6pwCTrekdvBofZeqwYFxzjBQSVwuNtgyLqCa3KjIROQ87Mve7clFPKhWl3IVepzDg59qUCIfbab0VOH1Loo-_zDycPSWSWPv6qFgfP4HGKBVuaEYEeHOWFPCwOetWmp84CEnh2KEb0nrun4b0z0VsIbemqouTJuTpAyZqQDTLNzleYBVbo/s902/%E5%89%B5%E9%80%A0%E6%96%B0%E4%BD%BF%E7%94%A8%E8%80%85.jpg)

2. 為新使用者設定權限策略

在使用者創建完畢後，帳號管理者返回使用者清單頁面，點擊剛建立的使用者。

進入使用者詳情頁面後，選擇「權限管理」選項卡，點選「新增權限」。可以選擇直接授予預定義策略，例如「管理員權限」、「唯讀權限」ReadOnlyAccess(如圖)等，或選擇建立自訂策略等。

[![](/assets/images/關連與指定使用者或群組.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhVniOPxaso4RAJw9VlYHOXSjoX8R9hIhDBequQoFyn3FBtKGS9BDSLi4s8BjrAhqCmAc2Oy6qm-5mdM-nIA2RJN5I0WgY1uKpZFgU9wXv90rwskz-6eQtf6bkVRI8OWdxKNqq-e2ueUlWxWNamDAYDM453yBFPoTTzLJdjIf4qwOuPtls8bsGqh9UNSE/s1316/%E9%97%9C%E9%80%A3%E8%88%87%E6%8C%87%E5%AE%9A%E4%BD%BF%E7%94%A8%E8%80%85%E6%88%96%E7%BE%A4%E7%B5%84.jpg)

3. 帳號管理者檢查並確保已根據需求配置了正確的權限，最後點選「確認」來完成配置。

4. 由新帳號使用者登入並測試權限。

二、以設定權限方式加入已存在的使用者帳號或整個使用者群組：

如圖，帳號管理者可建立客製化POLICY

[![](/assets/images/螢幕擷取畫面 2025-01-23 163743.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUgPSk0RKWonT40mXzdPnzD9PYyJRN5VlV_HZZPZ9vjmqUFC9xO63MgJyLY0me_NOW8x4EncA3vzN61TQrmh7xp2XP2vuauAyf-RVnvj-AqFOCQRCfd49z3PODampOObYxjwQZwH1OrJow3b-iArtKyPMzWcs1tjVe0p7JPsL01o-0TtWy4b0sEvidjPU/s1178/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202025-01-23%20163743.jpg)

1.建立新權限時，在完成編輯後，可將指定現有的帳號或群組加入，在此過程中，新增的權限將會套用到所選的帳號或群組上（如圖）。

[![](/assets/images/螢幕擷取畫面 2025-01-23 154102.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoBo1OZaByDOU1k0v7hQBOi_1UBdI3I7TPxeclzujru06vGWTe6IZ3RnrJEbxQpefC5wyk58D8phK3Kyx_DFAJJR_ZV527RI2ck9SHH3AuswmYae0jlpc9Un02_g_ZzbHJu7v2Y9DXzAlDxvkg4-OqPptRerMuWlMzrqVS2qD1XBfihLb0xaDekd8f6nI/s727/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202025-01-23%20154102.jpg)

2. 管理者確認修改後的權限設定沒有問題後，點選「完成Complete」儲存變更。

3. 請此帳號使用者進行登入測試。

另可參考以下原廠技術文章鏈結

https://cloud.tencent.com/document/product/1708/92952

https://www.tencentcloud.com/zh/document/product/598/40985