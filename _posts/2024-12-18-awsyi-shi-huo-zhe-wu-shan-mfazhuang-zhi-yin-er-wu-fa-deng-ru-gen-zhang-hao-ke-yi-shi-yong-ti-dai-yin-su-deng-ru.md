---
title: "AWS遺失或者誤刪MFA裝置因而無法登入根帳號，可以使用替代因素登入"
date: 2024-12-18 01:12:00
categories: ["AWS"]
tags: ["AWS"]
permalink: /posts/awsyi-shi-huo-zhe-wu-shan-mfazhuang-zhi-yin-er-wu-fa-deng-ru-gen-zhang-hao-ke-yi-shi-yong-ti-dai-yin-su-deng-ru/
---
## 遺失或者誤刪MFA裝置因而無法登入根帳號，可以使用替代因素登入

l        開啟MFA一般登入，我們會在圖三的階段需要用設置好的驗證器進行驗證碼的輸入。但如果你不幸不小心將你的MFA驗證移除或者刪除，也仍可以選擇用其他方式進行二段式驗證。

[![](/assets/images/根1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGa-akv1HuYkyv4T2UlVSBzPHuxuVIgo2PK0urqxFF_KXBA_dtzFevy4U7OEotXr1foic7cvMSBPybAFGCgAK9ko5T230a-ux_d_AeQJQxWDD1v28lyhyphenhyphenO49FFCHOu11Ni2hoqHkp-cuhEjZoTs5SVjavtHUoP-5GVxG2iea-s6WrjCJuTLwaSrOp-AXQ/s1525/%E6%A0%B91.png)

  

[![](/assets/images/根2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5rK_BDaKyzSirLuj2QpIc4cBJ0eRFrk1yrud_udtINsTnxyZyaf4RdWgSH_NnxyFShYulZhCP0lrKkakfiIkczQHkgJkNuyP1VaRSba-_1tae3SLOuiRfUyCUUvCh3PICOmiC4uDqF9kZ5Lz9ugbLAKRsE8ZiOP1h0eIPm3Y6s6wP3KG9R693VfcWhsw/s1186/%E6%A0%B92.png)

  

l  
正常之下我們需要在圖三的階段輸入驗證碼，但因我們遺失了MFA，所以這時候我們可以點選下方的Troubleshoot MFA(排除MFA故障)

[![](/assets/images/根3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhy23JjTHzENCQWLCbanAlZs6U9AZkJWee6L7vpxZi1le8-btMgEv3dABiRa4peURwvn8rBCVWeII3K6QRfUhxmVqyBYKCsiLY2Ny1w_lfeWmjpVkeAQn4cf2yxaDu6zm728ZWQtQFT4NQgs29LDhZVtjmJ5fX5tsdj8F-Hrf3w4_HES7gsb_4ZPr9vB2U/s1162/%E6%A0%B93.png)

l  
點選後，我們會進到此頁面，點選第二項，使用替代因素登入。

//他會有兩道MFA驗證，一道是你的預設的電子信箱，另一道則是電話號碼。

[![](/assets/images/根4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqtDuGsnTv4evI6C8J0OBVEK_YLg3GYfBsTq1rnh-GRjQQPb8vt-M_RNXdSvE2XuxLuXCPGW3esdKpXccDUjIJrzcHOHbZXNgtE7oLjn8F3McBBoP8y8aHjKJluocpBuHph3_wtYG1385AYoWSk_uqXnLKg-eHT-cI5Y-NhTo6-v9kyYq8r3MlebpCVO0/s1437/%E6%A0%B94.png)

  

l  
我們點選下去，AWS會自動寄送出驗證信，請跟隨信件點選驗證上的確認電子信箱。接著我們會來到第二道關卡

[![](/assets/images/根5.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBpl84921XZdIJ-IrX33iv-P-xQwezUaJb4sbCfkxKbxsvS-V_jJRlzQoq7vEs-__IDWnViG5gA68fiudCcUMOeqLFY4OSAwSsOSbt-4VQ5axKBtplBQ2iKruvcelDzGEQ8_iFoX0taApjyJf7d7rnnWN6-qYxtErccnRY8T63iug4bz84sb3eC08WPFI/s1421/%E6%A0%B95.png)

  
[![](/assets/images/根6.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirnRJD5UK6ZHTa4g6z7F4c8hW0CttPOrq2INBsLhLzskcTkmwDISRA5hYXd5KyHlQmSYSC6BdhyNZqle3zmJGqx5-Sn9ZLXMRoNaURLPwqZt9jUDglkuvocW490ROdkLVfGHodIAjp-Qa5S8O0ID1_jTbgZ-RjfFzqN1cQ2Ybr7yJEkoMyaAL9TaBPFNI/s1315/%E6%A0%B96.png)

  
  

l  
按下
“call me now”後，AWS會自動撥打電話給你，這會是國際電話，所以請確保你的國際電話服務是有開通的。

  
  

[![](/assets/images/根7.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-73ZheC9jOwgSx_JC-X5th8wtTHH6k1-Nik6ZaF6xEc8BCTP1Y8-Br5FdnLtpPNCv9WDA-Tu85GFxzexD40T1Z_yw-hjOaSVhDDicUraZhq0DQoK0_i0aM4PyJCSytaYXCYf919AFEc5oXOyGIpvc033aSZvpeLIQBKyt4U5QBPnv8S-eN0wDpYcw2Yc/s1180/%E6%A0%B97.png)

  
  

l  
電話驗證階段:

電話會是純英文，但步驟與輸入的內容會是固定的，正確的驗證輸入順序如下。

* 先輸入 正常電話號碼(例如09xxxxxxxx or 02xxxxxxxx) >>> 再輸入網頁頁面上的驗證碼

[![](/assets/images/根8.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVJdxQJrssJpU5FevsLQMVo4TEFUYg1XXT633_9DQ8f4LbffYOUPi3IsVCHW5RHV3QQBQ6dSZqFcrHmtuoAQey9QH2NRk7Crpx6b_N_ykrKDTWHbgMaHY67VZ7H_0YX47BX1PTXTj9PWRzYcTdRz27Ae6pABX48K1TcFojfOMcJis8wrKxSeiueldB2-w/s1401/%E6%A0%B98.png)

  

 

l  
//額外提醒:無論驗證有無正常的接聽或撥打成功，AWS皆會計算你的驗證次數，通常在撥打至2-3通時的區間，他會封鎖你24小時不能再使用電話驗證，請務必注注意。

[![](/assets/images/根9(無法接通停用).png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2B87iKpyswDbaFSYF1v_4eVeudxEjfpXFvvmJJpOpdcVhxDeX4xVTkM03XKgUQc79V-HRmuSaz5_ciKGRkCDBTQUwVRwxanC_5uXG4u2KabYKO7U0f-9Xpf5xDKHCNgu2m0cpwfwpVvX05Af49RNx-Rs0bVWbhZkjKGl9dly-B7eqeaF25qPzBeqDsvQ/s1419/%E6%A0%B99(%E7%84%A1%E6%B3%95%E6%8E%A5%E9%80%9A%E5%81%9C%E7%94%A8).png)

  
設定預設的電話號碼  

l  
從控制台右上角的用戶名字切進帳戶選項

 

[![](/assets/images/設1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjA77D0GIXtrI2_7urO16PtRP8thAsEllVx5W1KoFaMIRt2uIarIv7KSapd0mhfDN19YGcRWaDhm4Gcz5cV1v4PBR9IZRsmGLozcrOsUlbb-KwJkqNsEYs5L7T4xXBKx6hNZ1vw2DqGRgPzAfkC7bn0CD9U8tl6xW8Q1bDUG5Y5qVRWEtDn2oNmMs0Dx20/s1579/%E8%A8%AD1.png)

  

 

l  
編輯聯絡資訊一欄

  

 

[![](/assets/images/設2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSsi3R1niJtjtDjCq0Yxe7NjV116z90-LMuXE89IwWXhj93C1ed1XvOAc2R7wteC-GFXr9CVLTG9t2LlirqQxJOfwFPzLMKFiSdkDcq-Yd0gIq6SBtm6Y6UGfuHR-QknWodMmjOYnjOIxL2ZHReonU4cyvgkNXMeJgHj5uM9QaTkfc6Jeni6uEl1Ivmxs/s1590/%E8%A8%AD2.png)

  

l  
修改聯或電話一欄保存即可

[![](/assets/images/設3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0gPhjqToHrLLiExOlgC9aSTPM9Q5jcuX7WquwcgbJY6_EPe47P0I_saJNjX88Rxmq5DmQ7txs8hhgzyPEpjCEWx31TMJshOQtG9dZZEeECjx2byx5EnOtPdemxfRj3aDUGo3bJiGO_byzFGKNcyOUYzWuAJWia9-p7Vbv0TyD3gUd-FX7U8_pHLj6dQ0/s1598/%E8%A8%AD3.png)

  
  

手機 : (加號)+國碼+區碼+空格+電話號碼

範例 : +886 9XXXXXXXX

電話 : (加號)+國碼+空格+區碼+市話電話

範例 : +886 2XXXXXXXX

//0需去除，因為被886替代掉了

 //請注意，MFA的設置選項只有主帳號才能夠查看

 

  
  
  
  