---
title: "GCP VM主機建置"
date: 2024-11-23 17:09:00
categories: ["GCP", "GCP教學30天上手"]
tags: ["GCP", "GCP教學30天上手"]
permalink: /posts/gcp-vmzhu-ji-jian-zhi/
---
在雲端服務中，**虛擬主機 (Virtual Machine, VM)** 是一種基礎且常用的技術。簡單來說，VM 就像是一台模擬的電腦，讓你可以在雲端環境中運行應用程式或服務。使用 **Google Cloud Platform (GCP)** 的 **Compute Engine**，你可以輕鬆建立一台屬於自己的 VM。以下我們會一步步介紹，如何在 Google Cloud 上建立 VM

1.在"所有產品"中選擇"運算"，並點選"Compute Engine"

[![](/assets/images/螢幕擷取畫面 2024-11-24 075611.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFWcd8YVMcTJCuX09-qyRdGqp0f0kWgLsRkmdoVGbQG1kQJd5mTmBGoQKdkmjDXCWOKRfTsWHqj1CSo2dQ9vrFZIXTSsw_SZ8WXUvEeI96X3uhjvz_hpEHtPXcwXxTY4Qy81mqb9eCaW2TacsEYCgYPbKOXl7Iaej-jzQq007HZCC7OEEXvEg4SSrjP10/s1006/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-24%20075611.png)

2.點選"啟用"

[![](/assets/images/螢幕擷取畫面 2024-11-24 081626.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7mZJ1EDOm_opZYTNet2JcuJoaAgkYgUOtMv2-Egdt4hdymuF08VrmWUmcOT0V-lSv5rsWoAo8zrswbhkK9XnZB0g60goibjYn2WIclsfiUAIYjuSyZyjQc_JLlbiICmgwPdB10zEtPumvhXk6EV35kuRk2-m0hP2ND1d9XNaBNMXjv-2t4LDI_p4KWAo/s600/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-24%20081626.png)

3.點選"VM執行個體"→"建立執行個體"  

[![](/assets/images/螢幕擷取畫面 2024-11-24 082007.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXwHhrqVy-9bb-9KWzkmrvSkz1IOj_e8VAbKQU18yGPeRzVB5vA1AF-tNbP6oFsplBLjVZrkYyvI28OKqZwgP2Js7wgR_L2BrgU-dUY3-iTwPaz0KaDvTUCJ7hM1yPxld7-yZOD2Sv31tmKDjYQkoCD2X7lwEfcqxc1XveN1VgcN9789_qV0404PjStrs/s992/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-24%20082007.png)

  

4. 依照需求選擇想建立的VM種類

[![](/assets/images/螢幕擷取畫面 2024-11-24 083002.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4wYJz_e32rWY9TyeuXboot9IQLZWkTEfVSr0FAWdU1QMCXXcgtFuQrUPk22-NunYHhJcJS-0GRO5fAEOqu55VBcVKJ8lUZDgnw1ChSfm5zWblm1D_zbm2wR-vpEiDqcmMwbOeI1S3naLFLiBC6YQHZM-L19SquPcey7Kw6mYbfIrmcjVo7DHmW5DmQGY/s378/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-24%20083002.png)

  
**以下為建立種類比較**

| 方法 | 彈性 | 快速性 | 使用前提 | 適用需求 |
| --- | --- | --- | --- | --- |
| **從頭建立 VM** | 高 | 低 | 無 | 完全自訂的環境 |
| **運用範本建立 VM** | 中 | 高 | 已建立範本 | 多台相似配置的 VM |
| **運用映像檔建立 VM** | 中 | 高 | 已建立機器映像檔 | 快速部署與現有環境相同的 VM |

5.依照需求設定主機名稱、選擇機器預計建立的國家&區域

[![](/assets/images/螢幕擷取畫面 2024-11-24 083346.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMHLaqj40-HxV6y58kDC6ixLaffRc9wlfr4zz8TSVpf7K-BX_CDFFWNVw53jCMUHOZK72x0_mDrW2Qyb8-QNzdFU7XstS5ueQ0Nx4RzPpAF0JC6nFytxog_qEeQhcHzqcPgUIYUOM2c3ofyexF_bVR_-w7FwfQanc_9FNGsQiIDaZbznNM2J2nFW2a3lA/s676/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-24%20083346.png)

  

6.選擇機器的規格，依照需求選擇的規格，可預估使用的價格

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgB5xe55_fGu_SzVXL-V7Q_OhoYcgXeyyaKKu0aISk9wi8a-mg4wU4q2nk3uSC9kyLp2sk6ZPiIe3oIKJzDjuj95y-F4N5Bj3l9ox2R0KI-j-VL5-52T7iGErY7YaSmQx7k4lRX0-mccvwIITKu0Og_RbU55na7vx2kBmmufFVkH0wvZNcsQ_TjdzMd1SU=w640-h334)](https://blogger.googleusercontent.com/img/a/AVvXsEgB5xe55_fGu_SzVXL-V7Q_OhoYcgXeyyaKKu0aISk9wi8a-mg4wU4q2nk3uSC9kyLp2sk6ZPiIe3oIKJzDjuj95y-F4N5Bj3l9ox2R0KI-j-VL5-52T7iGErY7YaSmQx7k4lRX0-mccvwIITKu0Og_RbU55na7vx2kBmmufFVkH0wvZNcsQ_TjdzMd1SU)

  
7.選擇好規格後，將下方的VM佈建模式進階設定選項拉開

此設定中提供VM 發生故障時，可自動重啟該執行個體，或因該區域實體層面設備故障時，可設定自動遷移主機是正常運行的可用區

[![](/assets/images/螢幕擷取畫面 2024-11-24 083942.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlTc4kuCkZG1jRrAfcKmWjtsTTO0y8ha1hphG6h-0PP3E9CqmNoTG_Z-3_8wIf8ZOAOqKy6F027pZzmlfax3yungXnSL_vq2_ebvgj9lemVnlfY_bIwzDbtmyENSNXrUYhnmtTkZv4fvUuwY7zZwRlWfuVFA8Do1CLWyWH_9Vn54lHOCEw-btObPyd_MM/s793/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-24%20083942.png)

8.於開機磁碟→點選"變更"

[![](/assets/images/螢幕擷取畫面 2024-11-24 084900.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLlEOONfGmjaM2p0gAQOW-Rt2JiKN3DiQH9I9OcFBvBfa5Mkgps1OvBl37asCUu6KxrgHoepXsDmq4E9QP2rhJ3acWqQAkyuE-Jg4hpDMzSKrFEDv0_9tz_Z9WnlLNIRpmnkxYtIluGzu-1ivcpBvg8lcWEAXAfEsgJb5Erot25dpctM1i2gLz6F5N7tg/s614/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-24%20084900.png)

9.可選擇要使用的作業系統、系統版本、開機磁碟類型及硬碟大小

[![](/assets/images/螢幕擷取畫面 2024-11-24 085250.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBQxYw9vJNObxvfK0xHJRpqln-76V74brGgQoHMOmJnrqHmJgXOtrOqU_-s5bdP_H5sxEhjWz_z1ZnpReDCaROgRjqCfRoxieNPVuJZJZCoZHUXN_u3EaOMPg1vRHuAsi62VX-bBNsi9iQvuWvAQFz8Mahe3XmfK336HOoxUO4lrrSVgtHgBF0tNDn9Hw/s678/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-24%20085250.png)

10.勾選防火牆設定 ，若想建立簡單的網頁伺服器，務必記得勾選 HTTP 及 HTTPS 流量，確保開啟相對應的通訊埠(port)得以讓使用者存取網頁。

[![](/assets/images/螢幕擷取畫面 2024-11-24 090038.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiI0JoMT4rnWk5zp0IgsHKnAo9tPjSywuaMdBXjdiXuz4mT_vrrQlfCfKm81MYpaiX6iSNxcTpvHr9ADEy0Jb6XxPsTsLeBCv_PuTPPCcawPH_ZSX37gMjpGQXK2iuqVL7OsgCI6Fwn_X_slAP5NKFThgBRbRpiYDlO2EglF2ZPDJQXtHtdz5-UnIjs5l8/s410/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-24%20090038.png)

11.進階選項中可額外進行設定

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh_iZxhXTohw_oUFt6FS1FnD00bAH_ZhDTeE0iKJHvWAYguU5PaDeCLiWagf5nab7srWBR2ptO0x2qgAmRaCZ5AsDavSBEXn2zofKuUnf5zcW6j_y2mRy8nTsGy96QFW2KoSzQwNnNU8gvxMeKkHWOHsNM6F8pUEYQdyu4vIA5lZXyet_RjaC60j2OCH2k=w640-h530)](https://blogger.googleusercontent.com/img/a/AVvXsEh_iZxhXTohw_oUFt6FS1FnD00bAH_ZhDTeE0iKJHvWAYguU5PaDeCLiWagf5nab7srWBR2ptO0x2qgAmRaCZ5AsDavSBEXn2zofKuUnf5zcW6j_y2mRy8nTsGy96QFW2KoSzQwNnNU8gvxMeKkHWOHsNM6F8pUEYQdyu4vIA5lZXyet_RjaC60j2OCH2k)

12.完成後，點選"建立"

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgJCmCSs3msLJwQbmPEuVmKqtbkaG86PNbdaoYKzLrbnpHXhGWskytFsfuL6zV6W0ejG2MvbnmYOZrFoMceDtlbAukL__KptCElhvSupbgTyi4MtMxtBpyT-RbaFHvHSkk9gmgb0lo7qpLn4lzCKCMTwGVeQP50dAS6wwNIkJpRPavn6BvkkEM5Wh10bJU=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEgJCmCSs3msLJwQbmPEuVmKqtbkaG86PNbdaoYKzLrbnpHXhGWskytFsfuL6zV6W0ejG2MvbnmYOZrFoMceDtlbAukL__KptCElhvSupbgTyi4MtMxtBpyT-RbaFHvHSkk9gmgb0lo7qpLn4lzCKCMTwGVeQP50dAS6wwNIkJpRPavn6BvkkEM5Wh10bJU)

13.建立完成

[![](/assets/images/螢幕擷取畫面 2024-11-24 090043.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTFRk4kcDJth1VzXmvqHSfc0sB_ItXwn5MSoyHQUxPLoSsmhbkwZ51eVhfDLFUwaw-AuBU1iJRam42dXG2lYKWGKkfm9fCcd015TpRpvenKe-oNc4VRoKajF5gf5XQ4-a-HVpzpxCiiB_4vsX3T-5kyCxUpj1GC0EYSUnUBTNbHgJuV7yumRYg1qhiROQ/s1384/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-24%20090043.png)