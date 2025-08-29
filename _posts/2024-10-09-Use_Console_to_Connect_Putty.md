---
title: "如何使用Console連接交換機並使用putty測試"
date: 2024-10-09 10:15:00
categories: ["IT知識"]
tags: ["console", "putty", "連接", "交換機"]
permalink: /posts/use-console-to-connect-putty/
---
  

## 

目前需準備的材料有:電源線，實體設備使用Cisco 2960S做範本，準備一條能連接的console線，一條公頭轉USB線，一台電腦設備。

 

**1.首先，確認設備型號，這次使用的實體機器是Cisco 2960S，連接方式如下圖**

**需連接console纜線，另一端連接公頭，USB插上準備好的電腦設備。**

[![](/assets/images/15.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeodGjq1oggsCSFdzBrNLfaOS-GUUnxDgwECMS0rKacXfHb56L-cQghZ_ovFqWVLFtGrO9gsvt2A9bRVrVBxbIseMHRByB5pevBefzRnlUhgB_BU0Kxkb8F2wZMAFfVF_HCvmsGY2E94dujKVmquGUicqVG6E6JUmGZuRLujqoLrYqO1469kOGE30AYbiE/s946/15.jpg)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhuDfnRIagp9s4gp8zLOEuJEWPO8vjBkoW7kNobBjjM41l_g8dH9uYmXsI4zrdu5E2tnhJTw4YEUx9INi7MPH0JwoyfiIFpUoikt7YKXnuFr0dS_Xr3c_rjA1ELC-GWILRbEqHI7SlBtClWL_I0x3iZdI-uDykGH6f_Q_bXBWb6sq_WqmkD2OKhaevBlyHE=w570-h427)](https://blogger.googleusercontent.com/img/a/AVvXsEhuDfnRIagp9s4gp8zLOEuJEWPO8vjBkoW7kNobBjjM41l_g8dH9uYmXsI4zrdu5E2tnhJTw4YEUx9INi7MPH0JwoyfiIFpUoikt7YKXnuFr0dS_Xr3c_rjA1ELC-GWILRbEqHI7SlBtClWL_I0x3iZdI-uDykGH6f_Q_bXBWb6sq_WqmkD2OKhaevBlyHE)

  
  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEglFzGyfWpNuUNjPmsTWvWEdYMvbjJgyQajJJXdlFOQwx3rCCuh5-EVwpP23HzbvdA2fIPzHd_BNQxY9UVT_PYmIe_QITgSww2HBuJhfw-odJFNZw3ODyOGfdKutzmlYKtIh1xNWc74_L1XdFG81q8BjWof-5S287hvPJOWzYvM1AidRoAphCZsOSR2Y1Ti=w520-h390)](https://blogger.googleusercontent.com/img/a/AVvXsEglFzGyfWpNuUNjPmsTWvWEdYMvbjJgyQajJJXdlFOQwx3rCCuh5-EVwpP23HzbvdA2fIPzHd_BNQxY9UVT_PYmIe_QITgSww2HBuJhfw-odJFNZw3ODyOGfdKutzmlYKtIh1xNWc74_L1XdFG81q8BjWof-5S287hvPJOWzYvM1AidRoAphCZsOSR2Y1Ti)

  
  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhzRcdnfRRWoacSMfVSaw-Vn4EIGqgSwwl65VQS92BauhnjkyURdXYjA_Qr7piyf-iSo0XVcoC3RH0aQq9mtADGTKiW0PKTl14x3bCihhyFYfc59Xmub3w82fCMAzpEWrBkRdiA8ALi6IzQojXzmfnLXX3zD9wkoUk_uDRS0-x2j3kXrUapxu4apgZfySPh=w474-h405)](https://blogger.googleusercontent.com/img/a/AVvXsEhzRcdnfRRWoacSMfVSaw-Vn4EIGqgSwwl65VQS92BauhnjkyURdXYjA_Qr7piyf-iSo0XVcoC3RH0aQq9mtADGTKiW0PKTl14x3bCihhyFYfc59Xmub3w82fCMAzpEWrBkRdiA8ALi6IzQojXzmfnLXX3zD9wkoUk_uDRS0-x2j3kXrUapxu4apgZfySPh)

  
  

**2.設備都連接完成後，可到電腦設備確認機器連接的狀況，開啟裝置管理員**

**可以在通用序列匯流排控制器中找到實體設備連接的資訊，點擊它查看詳細資訊。**

  
[![](/assets/images/1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiItbUa7pwmnw2SAuLmPH9KFYD33i2bHVTY69KShqeWvWM68RCZvkvs03viElQ5YYhcm4Mfue7Xx-0Ik3K3J7CWw6VR_cHxSyyhF25YeI5uoC_i4MH9NLO9qVNKGXd1Zeb2BvtlUKvW_wpdNrDzd_uIEJ7wbv7HCdTGv5ZymStZ8kSM7fR1lkwseRoYICFe/s1165/1.jpg)  
  
  

**3.在位置上，確定你的電腦 com port 位置， 例如 com1 , com2 …還是Com5。**

**圖下確定是在com4的port位置上**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEidppcsgv4qF1HGSjj2jupm5BErMUbmgA6GIS-tcEdb1T0IQcm4djgQ8yF_3gXoKKdpeVnxmBF4g747KFIvQrXWEaXmeyYk11cBSZRqrMLNKAr3NY2sTe9aQrzfJjySJxSwitNdNa4LWNh9ffs-BHZJr6lFUu9zZNPggR6Nhq_f3aEkGi6vNmNwQ3JKPCSP=w487-h544)](https://blogger.googleusercontent.com/img/a/AVvXsEidppcsgv4qF1HGSjj2jupm5BErMUbmgA6GIS-tcEdb1T0IQcm4djgQ8yF_3gXoKKdpeVnxmBF4g747KFIvQrXWEaXmeyYk11cBSZRqrMLNKAr3NY2sTe9aQrzfJjySJxSwitNdNa4LWNh9ffs-BHZJr6lFUu9zZNPggR6Nhq_f3aEkGi6vNmNwQ3JKPCSP)

  
  

 

 

 

 

 

 

**接下來執行電腦 putty 程式，並根據設備面板顯示的數據填入 putty 相關欄位。**

**重要設定值參考:**

**\*每秒傳輸位元 –> 9600 或 115200 ，必須參照你的設備要求**

**(目前 Baud Rate(Speed) 的設定從 50 到 921600 都有，理論上 Baud Rate(Speed) 數值越高，傳輸資料時間越短(難度越高)，能傳輸的資料數量也更多(相當於頻寬增加了)。實際應用要設定多少 Baud Rate(Speed) 還是要看於設備的規格，比較常碰到的 Baud Rate(Speed) 大概就是 9600, 19200, 38400 跟 115200 這幾種。)**

**填入正確的 com port 位置後點選 “open” 按鈕。**

**4.這台設備的speed設定為9600，serial line位置為COM4，連線種類選擇Serial。**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj7HTh1qydB6mt1rYNYuAodPrR_PuKia9cN-uzA9ZSdQ09m3Qx3wpuUrrGWXnFKOh8xqzTPqscCJRbMuru4_H81gBgn2NBLFW2GWWUPW5oSAvsO4EiRg5EDt8nP6XbpXZ5vVoZgD7v7fhNNbkkIsgj273Pc1oKdqH4ArwvXZRHikNdGm8ef98tSy94iqJPa=w535-h533)](https://blogger.googleusercontent.com/img/a/AVvXsEj7HTh1qydB6mt1rYNYuAodPrR_PuKia9cN-uzA9ZSdQ09m3Qx3wpuUrrGWXnFKOh8xqzTPqscCJRbMuru4_H81gBgn2NBLFW2GWWUPW5oSAvsO4EiRg5EDt8nP6XbpXZ5vVoZgD7v7fhNNbkkIsgj273Pc1oKdqH4ArwvXZRHikNdGm8ef98tSy94iqJPa)

 

 

**還可以調整更多設定，如下圖。**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiXFMPWifT5y8qJq7IdHGhR2n-aKp9Q4FQuWLdJzsQRPN_SV7wMBVKVkPC9WwDFLr_FCFp-xmGv4S3bXJRcojGQ2MlVO34Em8dbPj5TxHpbkdBTI207Fa9m_R_tNKqmZVg_EYEceBQu-Ca-2GziG2GlgoSACPQe-cdLT0OqyrO0ygguH38kunqw3qbg7vCe=w525-h506)](https://blogger.googleusercontent.com/img/a/AVvXsEiXFMPWifT5y8qJq7IdHGhR2n-aKp9Q4FQuWLdJzsQRPN_SV7wMBVKVkPC9WwDFLr_FCFp-xmGv4S3bXJRcojGQ2MlVO34Em8dbPj5TxHpbkdBTI207Fa9m_R_tNKqmZVg_EYEceBQu-Ca-2GziG2GlgoSACPQe-cdLT0OqyrO0ygguH38kunqw3qbg7vCe)

  
  

 

 

 

 

 

 

 

 

 

 

 

**5.設置完成後就可點選open來確認是否成功連接。**

**成功後會顯示下圖，成功連接設備。**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg-PNoUmu1hQewOjpgQVNBo96BZEd6EoE0rhaxu6bNjhWmAHfp2ive4g6H72luUfVxt-ebjkrpSxqjxyyA-25IKPD5sshPwfX7cOOU7gKNEs5OgNvPRgzAEcDxIu4Fepxxcku5vOlhgOtZnmsm_r7-xbro8JDw78BwppzqvVtY4y392IwCEIk91Vk-LBkix=w613-h356)](https://blogger.googleusercontent.com/img/a/AVvXsEg-PNoUmu1hQewOjpgQVNBo96BZEd6EoE0rhaxu6bNjhWmAHfp2ive4g6H72luUfVxt-ebjkrpSxqjxyyA-25IKPD5sshPwfX7cOOU7gKNEs5OgNvPRgzAEcDxIu4Fepxxcku5vOlhgOtZnmsm_r7-xbro8JDw78BwppzqvVtY4y392IwCEIk91Vk-LBkix)

  
  

 

 

 

 

 

 

 

 

 

 

 

 

 

 

**6.接下來嘗試SSH，如下圖。**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgZsznxv17RAjMKKKM7Kjw5VP9sCmOzfA8aKVMd-fFn03xdfnJdOBhGKKx71B2uIbiYTthm1DXsVGRaRUKQ7LDRTvkAJ0oIdrHX0hgULUzIZmUdpiu_1S_9tTaupj9ogHR-0-Y2ifVCtaRxyDhr4ePfjbQsYp-dcZXf3tJAGyBLaeic-H7zaJs7eh12yB0v=w521-h519)](https://blogger.googleusercontent.com/img/a/AVvXsEgZsznxv17RAjMKKKM7Kjw5VP9sCmOzfA8aKVMd-fFn03xdfnJdOBhGKKx71B2uIbiYTthm1DXsVGRaRUKQ7LDRTvkAJ0oIdrHX0hgULUzIZmUdpiu_1S_9tTaupj9ogHR-0-Y2ifVCtaRxyDhr4ePfjbQsYp-dcZXf3tJAGyBLaeic-H7zaJs7eh12yB0v)

  
  

 

 

 

 

 

 

 

 

**7.成功畫面如下:**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh6yze0ev4k5puWvTCdvVgr__Zvf-fdqkxxGEk_eJU0lk54aC0azxbVnDkwgObik9jnedjR-M7RuysNcADslgW75QG-c_rYJFxqfUpYAw6aJIIobkiCs31ELVxmavkyYubDrk40r0dgpnNtFOis1ukvtZeHUXzh7TCUiLNqtXZ-t3sR8wRVDa8W5R1w1_Sh=w606-h381)](https://blogger.googleusercontent.com/img/a/AVvXsEh6yze0ev4k5puWvTCdvVgr__Zvf-fdqkxxGEk_eJU0lk54aC0azxbVnDkwgObik9jnedjR-M7RuysNcADslgW75QG-c_rYJFxqfUpYAw6aJIIobkiCs31ELVxmavkyYubDrk40r0dgpnNtFOis1ukvtZeHUXzh7TCUiLNqtXZ-t3sR8wRVDa8W5R1w1_Sh)

  
  

參考資料:

<https://vocus.cc/article/6544ff8efd89780001bba587>

<https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960/hardware/installation/guide_stack/2960SHIG/HGcliSET.html>

  
  