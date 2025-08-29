---
title: "Supermirco Server 做硬碟raid設置"
date: 2024-10-29 04:11:00
categories: []
tags: []
permalink: /posts/supermirco-server-zuo-ying-die-raidshe-zhi/
---
Supermirco Server 做硬碟raid設置

 

1.開啟伺服器進入到BIOS前會出現進入MegaRAID的提示，鍵盤按下「CTRL+R」即可進入MegaRAID模式進行相關RAID的設定。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEht2gwbUEjZNF0Rcg6Kw8vWh9ZYKckKt-aMRWhh3i1Ot8ZtDHx4dweXEcb5-MAU9pXpt250_v7lhx8I3SAV_2PXbxRoSCTJfURO_xSUJkmWXql1jhHVcymrVFfzQpi60MGiVeuXKKa1g0V_gkq5WV31-JnRbMazX-UaSM69HB8LHkulwEttyfrJxeWaoUvH=w560-h208)](https://blogger.googleusercontent.com/img/a/AVvXsEht2gwbUEjZNF0Rcg6Kw8vWh9ZYKckKt-aMRWhh3i1Ot8ZtDHx4dweXEcb5-MAU9pXpt250_v7lhx8I3SAV_2PXbxRoSCTJfURO_xSUJkmWXql1jhHVcymrVFfzQpi60MGiVeuXKKa1g0V_gkq5WV31-JnRbMazX-UaSM69HB8LHkulwEttyfrJxeWaoUvH)

  
  

2.進到MegaRAID模式之後，到「Foregin View」分頁，選擇AVAGO 3108 MegaRAID，按下「F2」，選擇「Clear」進行清除。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhqVBTr2DWhRnD3-E2ZakStrKZh5TPA7kCCeW2mvEadye-PgcPqPsPEuee7RNOgpKpRvrT3V2V1EKzK6O_bzvgROl2tZ3686OZoJNF8CnAatyE6Vxiax6s-a3Mt4aGaw0UiLwEmNK2H7j7J6tArbxlRagi1Pa9F0IYwRD6tN1NlH6VxD9mjMEysJTNwy5Uw=w556-h322)](https://blogger.googleusercontent.com/img/a/AVvXsEhqVBTr2DWhRnD3-E2ZakStrKZh5TPA7kCCeW2mvEadye-PgcPqPsPEuee7RNOgpKpRvrT3V2V1EKzK6O_bzvgROl2tZ3686OZoJNF8CnAatyE6Vxiax6s-a3Mt4aGaw0UiLwEmNK2H7j7J6tArbxlRagi1Pa9F0IYwRD6tN1NlH6VxD9mjMEysJTNwy5Uw)

  
  

3. 按下「OK」確認清除。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj-ZxuzeVdTHcqHTKQP2AK5c1g5wGSUbTVONC9BvWDdJWIBGMVLgmitIHc5RrvhVdqV2cmbcRb8axHwFE69U05W2atm9-2rifxMQ-LqS6vcLOB7L5XfcMD-d8LR2cEjpl1L3f3XtGa9ae-LqoG0WXyoYw3wjkYlesPmvwmZ57-o99pR8deitY6OSwQdK3fr=w556-h340)](https://blogger.googleusercontent.com/img/a/AVvXsEj-ZxuzeVdTHcqHTKQP2AK5c1g5wGSUbTVONC9BvWDdJWIBGMVLgmitIHc5RrvhVdqV2cmbcRb8axHwFE69U05W2atm9-2rifxMQ-LqS6vcLOB7L5XfcMD-d8LR2cEjpl1L3f3XtGa9ae-LqoG0WXyoYw3wjkYlesPmvwmZ57-o99pR8deitY6OSwQdK3fr)

  

4. 到「VD Mgmt」分頁，選擇AVAGO 3108 MegaRAID，按下「F2」，選擇「Create Virtual Drive」，開始建立Raid。

 

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj1KsBOldIqXSWHfXtAZOTvFyH_gArs7EihPC_VXbbAswLp3NLgsYP3ad3GdbLWJHRpHV9ixmx3A-F1FxhEnzQlF5FtQCR4qM8WbycMq5L_WyKuZwNLW5CBVMInDcSIXJKIePNgkcXpFwkecl67664-kjetxy0PrDRp6muPT_dILl2nSVS8PaqoNQqM1Y14=w559-h329)](https://blogger.googleusercontent.com/img/a/AVvXsEj1KsBOldIqXSWHfXtAZOTvFyH_gArs7EihPC_VXbbAswLp3NLgsYP3ad3GdbLWJHRpHV9ixmx3A-F1FxhEnzQlF5FtQCR4qM8WbycMq5L_WyKuZwNLW5CBVMInDcSIXJKIePNgkcXpFwkecl67664-kjetxy0PrDRp6muPT_dILl2nSVS8PaqoNQqM1Y14)

  

 

5. 這邊示範做RAID5為例，選擇「RAID-5」，下方按空白鍵選擇需要做RAID的硬碟。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEglM5kE89SjirshpL726CvIMw01f8osqk8l6NM3GCmQdVSvZLTzWR7Bt_1DXJY2zKjbFizzCObqa08Dp3jtr7i3m74phymxg4rkx4l__aeY4pHSXx5GJDITjTjDw0KWfuuJEJgIuWiI3iTzI-gp5_EuTd6LC90GlxP79yWfMDO6HBslue3VF-VkvOgzFIl3=w555-h313)](https://blogger.googleusercontent.com/img/a/AVvXsEglM5kE89SjirshpL726CvIMw01f8osqk8l6NM3GCmQdVSvZLTzWR7Bt_1DXJY2zKjbFizzCObqa08Dp3jtr7i3m74phymxg4rkx4l__aeY4pHSXx5GJDITjTjDw0KWfuuJEJgIuWiI3iTzI-gp5_EuTd6LC90GlxP79yWfMDO6HBslue3VF-VkvOgzFIl3)

  
  

6.相關進階設定可自行參考進行調整。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjrAakf2x0ZJ3vV_6OMUR79ZRtFN64Vz7T1sO6xq8cJQn6V3ZpRyKAWqGc1AweutbtHlDknb5FLkqKHy5xMaNSA0_Q4UbyyUdNdP-CWSY6rRikwrs901DXKdvhHzPiCLOOBEFM730NCGwX31355akk9yI8DnHRssGGCSIRXmTGUjb-R3BGEHD_f7rY1G1lx=w556-h304)](https://blogger.googleusercontent.com/img/a/AVvXsEjrAakf2x0ZJ3vV_6OMUR79ZRtFN64Vz7T1sO6xq8cJQn6V3ZpRyKAWqGc1AweutbtHlDknb5FLkqKHy5xMaNSA0_Q4UbyyUdNdP-CWSY6rRikwrs901DXKdvhHzPiCLOOBEFM730NCGwX31355akk9yI8DnHRssGGCSIRXmTGUjb-R3BGEHD_f7rY1G1lx)

  
  

7.設定完RAID5之後可以看到下方「Basic Settings」顯示的容量及可自定義的名稱，設置完成後，按下「OK」完成設定。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjND9XlUakmIK-ayyO7eMzXvxgCTuoN6aQIifVaPTScPSV9Zc-9UStyWrs701utGo-ZKybBp3X4oVyN7PRhR6XGodpSyo_CFNAJnD7MfJ2Y6hu6rO5fBSh6hYdorr9DtSbLFgp753Fe-Of8zw2gpfubeiNd4OoNQulyn4OljYOWP8vFoPAyNuMcgRgtbOwn=w562-h321)](https://blogger.googleusercontent.com/img/a/AVvXsEjND9XlUakmIK-ayyO7eMzXvxgCTuoN6aQIifVaPTScPSV9Zc-9UStyWrs701utGo-ZKybBp3X4oVyN7PRhR6XGodpSyo_CFNAJnD7MfJ2Y6hu6rO5fBSh6hYdorr9DtSbLFgp753Fe-Of8zw2gpfubeiNd4OoNQulyn4OljYOWP8vFoPAyNuMcgRgtbOwn)

  
  

 

什麼是RAID 5 ?

RAID 5
(Redundant Array of Independent Disks 5) 是一種磁碟陣列技術，結合了資料的**條帶化**和**奇偶校驗**，提供高效的存儲性能和資料冗餘。

主要特點如下：

1. **條帶化（Striping）**：資料會分散寫入多個磁碟，這樣可以提高讀寫速度，因為不同磁碟能夠同時讀寫不同部分的資料。
2. **奇偶校驗（Parity）**：RAID 5 在所有磁碟上均勻分佈存儲了奇偶校驗資訊。這些校驗資訊允許系統在一個磁碟失效的情況下重建丟失的資料。
3. **容錯能力**：RAID 5 允許一個磁碟發生故障而不會喪失資料。系統會根據剩餘的磁碟和奇偶校驗資料自動重建丟失的數據。
4. **最少磁碟數**：至少需要三個硬碟才能實現 RAID 5。
5. **空間利用率**：與 RAID 1 等鏡像技術相比，RAID
   5 提供更高的存儲空間效率。奇偶校驗資料佔用了相當於一個磁碟的空間，其餘磁碟的容量可用來存儲實際資料。

RAID 5 適合用於需要平衡性能、冗餘和存儲效率的應用場景，但如果有兩個磁碟同時損壞，資料就會無法恢復。

 

 

raid 5會損失多少的硬碟空間奇偶校驗數據?

在 **RAID 5** 中，奇偶校驗資料佔用了相當於**一個磁碟**的空間，不論陣列中有多少個磁碟。具體來說：

* 如果有 **N** 個硬碟，RAID 5 會使用其中的一個硬碟來存放校驗資料，因此有效存儲空間是
  **N - 1** 個硬碟的總容量。

**舉例：**

* **3** **個 1TB 硬碟**：RAID 5 總容量 = 3−1 \times 1TB = **2TB** 用於存放資料，1TB 用於校驗。
* **4** **個 2TB 硬碟**：RAID 5 總容量 = 4−1 \times 2TB = **6TB** 用於存放資料，2TB 用於校驗。