---
title: "阿里雲設定日誌告警"
date: 2024-12-22 11:34:00
categories: ["阿里雲", "阿里雲教學30天上手"]
tags: ["阿里雲", "阿里雲教學30天上手"]
permalink: /posts/a-li-yun-she-ding-ri-zhi-gao-jing/
---
**1.** **配置通知對象**

左側導覽列中 ->警告中心頁面，例:設定使用者Bob。

**[![](/assets/images/01.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvVTR-nQd9Qkuz2g2UZCwm5zVVfz7_FYWWqmxbfjg3MqJBpCtGQ34IWaTLY9FRbBeVghXmnV0UyPxquj7Am1fDmNMZU4FqACaE8B_A5c38NdNQUPZQy7Ug5b_8KaRVdh-jgED4xtJlUeZw2MlnUshT6QQ5w3RXY9FUN8VtMO8Mm6ljdkivyMLysYBX-c_4/s968/01.png)**

**2.****建立使用者群組**

新增使用者群組對話方塊中，將Bob加入到test群組，按一下確認。

[![](/assets/images/02.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfn6kwZs7WgrnXKLshUHdBt2jdjAnq20bsBNiiVYv-OLyW4FGnkvb2Ik3_tV_CdFFdMqUlH8ve7nmaPvcp8HABVJiaXuKH4DNS9RiiPKck3bF2oFDCiG2FMxkrp_KygOj28jrbv9DaFnoDBqUiFTeYLXBtC4IDQ1mEyGKRWkOYTSHILhWsQ-Y_onDTrbzH/s973/02.png)

  
  

**3.** **配置告警规则**

1.警報中心
->警報規則頁籤 ->點選新建警報。

[![](/assets/images/03.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiONHemJSTY-2Xwwq1XJ9FEfpIQlgziu9WlOHS1m3AY81PoR7AxzWFFbYyIxNKkY_Tj4Mouzz1LmZIBVjoiBgcxh5b98-N14jcVEFw4CyZ6wPg3LOHVwwdyQEooSWhud_IDj38qhOPdzH3M6cnh8olEcK7nW9Lah4vmkX_zgOKoQilMvO08MFQ9hTMgXqO6/s433/03.png)

  
  

2. 在新警告面板中 ->設定查詢統計 ->按一下新增。

[![](/assets/images/04.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6GkD4xMTXw-UU6DUwj5r7qry85h0_d2jFo6WYTk2r55nIguY9FyTR7UMzwy3EXLNDEhQ7vrVcS2vLsqwBNCtUbZe9DLH6O5k3ybfbbcUKYBNa9KOtCIOG8ReMY3K9EQfXamui-twve-zKRNJYHZ2ycWyo6SmlJ4VmsqxSU5Oe-wwhk3uC8sGTzWCM71TM/s616/04.png)

  
  

3. 在查詢統計對話框中->目標日誌庫 ->預覽查看 ->確認。

[![](/assets/images/05.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDeLrGpa8H8IWapqCxc18kwvConrUFkedU1Yc0sk1u415mFVXw_Za_KV4NW5powBERyI30LjWDfYbpZFn98HLdFplvz7PKMbbMEiZtZtmfWyb7I-eer42YUD4KdM_5pxV4rop2jBpNJ5V62Tl7DHu-Og9GH2UjI1DPkyNTKsT4hshPxiZpzAG9_SRY5dIz/s858/05.png)

  
  

**4.** **配置觸發條件**

新建警報 ->觸發條件有資料時告警 ->嚴重(這裡選中)

[![](/assets/images/06.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFdhV95QLj4rCq7GHyEWDGzxHwVcCJOjZjgYqcnxKE4K1OR6rAXS292gWRB9y-FrwY5UEAX3p9pDDDUeHwjyCESkJ6QzvR2U1UWLrY7seotJaqY0nt3OrOW-zI3yxenZ21XkwaYHKp7eF8YxNiAAwIp3A-PGrLkBKyZ1aMe7c1TjwuR6GCf0b0hjNHZdkm/s827/06.png)

  
  

**5.** **配置通知策略**

警報中心 ->通知策略 ->內容模板頁籤 ->在操作列點選修改。

[![](/assets/images/07.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSM32wxEIw6uE5q52MWVlqvg__6ErQSr6ZqUZmGo7cAz6Jx08JCUX2R901k7cVSHIW3qng_U_OCNm2WeAki9-7XYdFZrOhI2qoPqgzZzncth9T2rhMIjEABaoLipnjuXUTplwbMca0RQaN9a705sq2ANmMAYRis_6ii423i_ZZKH3Buq0-bC7Bygr7Rl4-/s1017/07.png)

  
  

**6.** **配置信箱告警的發送內容**

**[![](/assets/images/08.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEim4h-1hnfKmStP-KlhHrj-livKgnFCDu-LhVPu5YiYNx_zEAxAVPgHMptokbDbo4fRbpJpKtuIGg3EWOF164YU2Mq3XNgCAlsTCdyz_RFSU8sJydYzhBfZUHPd9QlAQBXLzvvXFJ6SF_a4dPe0_PHpygmpDm8Dp-4MYOoluUVrXoBKhU9-rdfaYEpUzr_V/s827/08.png)**