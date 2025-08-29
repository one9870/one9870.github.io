---
title: "阿里雲RAM帳戶MFA綁定設備僅能綁定一台"
date: 2024-12-12 05:40:00
categories: ["阿里雲", "阿里雲Alibaba Cloud"]
tags: ["阿里雲", "阿里雲Alibaba Cloud"]
permalink: /posts/a-li-yun-ramzhang-hu-mfabang-ding-she-bei-jin-neng-bang-ding-yi-tai/
---
## 阿里雲RAM帳戶MFA綁定設備僅能綁定一台

 

阿里雲帳戶的**多因素認證（MFA）** 提供額外的保護層。

比較需要注意的一點是，**每個阿里雲RAM帳戶的 MFA 僅能綁定一台手機設備**，這確保您的賬戶安全性，避免多設備引發的風險。所以如要換綁定設備，需要先解除當前綁定的設備再進行重設。

//一个RAM用户只能绑定虚拟MFA和U2F安全密钥中的一种，不能同时绑定。

[![](/assets/images/圖表.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgypaLv4BUgS_5Otn8rk-igATmVvLBpNug_nAHn_kpsLa46kYa0zVXo2s-qGbizXKsFLFA-KWvySflPLjRDnSlfT9wIKVCETJY5rfKwMXxB-RoNQbU6HUrQ0lpVUVSTHwNAZIFFE7m_CBVLueQFHFIhTI9hH4RzjyAI6q0euVs3M_y_jUxn4msCyG1vZOQ/s1155/%E5%9C%96%E8%A1%A8.jpg)

  

**RAM** **用戶MFA 使用常見問題**

### 更換 RAM 用戶的 MFA 設備：

如果主帳戶允許 RAM 用戶自主管理 MFA 設備，RAM 用戶可自行進行以下操作：

解除綁定現有設備 >>> 重新綁定新設備。

若未授權 RAM 用戶自主管理，需聯繫主帳戶或 RAM 管理員處理。

綁定的 MFA 應用被誤刪：

如手機上的 MFA 應用被誤刪，RAM 用戶無法生成驗證碼。

需聯繫主帳戶或 RAM 管理員停用該用戶的 MFA
驗證，並重新配置設備。

 

 

 

資料來源:

 

RAM多因素认证（MFA）的使用限制。<https://www.alibabacloud.com/help/zh/ram/product-overview/limits?spm=a2c63.p38356.help-menu-28625.d_0_1_4.2d066b33MkxxPK>

多因素认证（MFA）常见问题

<https://www.alibabacloud.com/help/zh/ram/support/faq-about-mfa?spm=a2c63.p38356.0.i9#concept-2201542>

什麼是MFA

<https://www.alibabacloud.com/help/zh/ram/user-guide/what-is-multi-factor-authentication?spm=a2c63.p38356.help-menu-28625.d_2_7_4_0.65934bb4pwqYCQ>

 