---
title: "GCP手機app無法連線ssh排除方式"
date: 2024-11-18 00:35:00
categories: ["GCP"]
tags: ["GCP", "app", "ssh", "教學30天上手"]
permalink: /posts/gcp-app-ssh-disable/
---
 若使用GCP網頁版和App版嘗試連線，只有App版發生錯誤，就可能為App連線中經過的google跳板機IP進行更動，以下為排除方式 :

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhL31LnFQ8d9aMbWRY9bJzLrrb-XvRuGiHMPxY2ZRcn7l0N3N-3rNvPjjsPfhfaVSpsChxpMFoRwxJDpj8aRplJiTo2cXVHu_SOsfVobvemh241NZjEyR5TIDQ8s0eW6iabQbOJnqfb6r_gDNvsOgFXzQ5mMcmnXaeCZtop0bGSXRPaAB6s9bGdqMgB2_0=w332-h381)](https://blogger.googleusercontent.com/img/a/AVvXsEhL31LnFQ8d9aMbWRY9bJzLrrb-XvRuGiHMPxY2ZRcn7l0N3N-3rNvPjjsPfhfaVSpsChxpMFoRwxJDpj8aRplJiTo2cXVHu_SOsfVobvemh241NZjEyR5TIDQ8s0eW6iabQbOJnqfb6r_gDNvsOgFXzQ5mMcmnXaeCZtop0bGSXRPaAB6s9bGdqMgB2_0)

  

**1.****將22port設定為0.0.0.0**

如 Google 官方文件[[1]](https://cloud.google.com/compute/docs/ssh-in-browser?hl=zh-cn#supported_environments)說明，為了要使用 App的SSH 須將22 Port 設為0.0.0.0/0。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEipVrtzDpKvQ5LHJAEJAKWm_8ddASTml9TdPQox72EfPHkcTssJRDnhLK_YTWkRrEvDjkiw1hiSNskf-6UKCpwkPq5RQ-YB4GNwWjaKVu58DlzN8fjjCSrPJl2428hWmkhfgyLX43u151G4Jm_-BvdHy9gS5POo4z5tRhIQlXIe_uj7XPU8ascq-ARRU1s=w513-h242)](https://blogger.googleusercontent.com/img/a/AVvXsEipVrtzDpKvQ5LHJAEJAKWm_8ddASTml9TdPQox72EfPHkcTssJRDnhLK_YTWkRrEvDjkiw1hiSNskf-6UKCpwkPq5RQ-YB4GNwWjaKVu58DlzN8fjjCSrPJl2428hWmkhfgyLX43u151G4Jm_-BvdHy9gS5POo4z5tRhIQlXIe_uj7XPU8ascq-ARRU1s)

  

**(1)** **須將22 Port 設為0.0.0.0/0的原因**

主要的原因是在當透過 App 的 SSH 連線時，實際上會先連到一台 Google 準備的主機，可以視為跳板機，再由此台協助進入到 GCE 主機，但由於此跳板機並非固定 IP，因此需要將 22 Port 0.0.0.0/0 全開。

 

**(2)** **安全性問題**

從安全上來看，不論是跳板機為 Google 提供，App 連到此台跳板機再到 GCE 主機連線的過程中都是有經過加密連線，以及預設GCE主機都是必須要使用金鑰才能登入，皆可確保安全得以保證。

 

**2.****手動添加IP白名單**

若還是有資安上的疑慮，就只能自行將google提供的IP範圍加入白名單，google有時會更新IP位置範圍[[2]](https://support.google.com/a/answer/10026322?hl=en&sjid=7511185769558089459-EU)，若有需求再進入網站查詢。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgz7saIb7Vi5U1Bck6B9kh392ZDkDflLxYifbHqkI668tny7szm_PachXz3oMBrzRc2b3wNczlOJprAxbp6l2BRrChFbi8TQzQUomH92RwlVSWibnlmTMWlDmyofKQijIfzmW8XbdS8pJgCjcniNRS8dnUsXN_25K_bxJHRqS90ixTnHSM8jJ9hC487Dpw=w555-h223)](https://blogger.googleusercontent.com/img/a/AVvXsEgz7saIb7Vi5U1Bck6B9kh392ZDkDflLxYifbHqkI668tny7szm_PachXz3oMBrzRc2b3wNczlOJprAxbp6l2BRrChFbi8TQzQUomH92RwlVSWibnlmTMWlDmyofKQijIfzmW8XbdS8pJgCjcniNRS8dnUsXN_25K_bxJHRqS90ixTnHSM8jJ9hC487Dpw)

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgLrG80AJ8cBc_3VbM7c_5HJyO_kwJjY9p5_F506pamPL_F3XUJOH6n6vkxpYlVLmxS5ADu_WVf2_SeRASgAgOPy0WhFMxi0bjxEPvShWoE0pS27Kd2sFD_-XraX0CYRv4hK30uEE1zn8t6X9kIs3Z_yhp5-Zj6LXSClz6hzsfFymUb-ElzG4yQ0pMTbO4=w492-h192)](https://blogger.googleusercontent.com/img/a/AVvXsEgLrG80AJ8cBc_3VbM7c_5HJyO_kwJjY9p5_F506pamPL_F3XUJOH6n6vkxpYlVLmxS5ADu_WVf2_SeRASgAgOPy0WhFMxi0bjxEPvShWoE0pS27Kd2sFD_-XraX0CYRv4hK30uEE1zn8t6X9kIs3Z_yhp5-Zj6LXSClz6hzsfFymUb-ElzG4yQ0pMTbO4)

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhlDep2cQUNsYasIXhGtjrnAAg10-499z125DfpGR6yr1WDGhRGQ66mZLCrODqzCOKotUm6LIdAEeWvw91JK-Esq2uoo6W_0GSrs_G3eC0izqL88e2K4Jp_96D8Cd2uG1mbJRqyKSwCygHqlhj6A8NeWPhqgxHz-Tw3M78WHhQOJhdPIY5xUQ-otd7TcN8=w497-h211)](https://blogger.googleusercontent.com/img/a/AVvXsEhlDep2cQUNsYasIXhGtjrnAAg10-499z125DfpGR6yr1WDGhRGQ66mZLCrODqzCOKotUm6LIdAEeWvw91JK-Esq2uoo6W_0GSrs_G3eC0izqL88e2K4Jp_96D8Cd2uG1mbJRqyKSwCygHqlhj6A8NeWPhqgxHz-Tw3M78WHhQOJhdPIY5xUQ-otd7TcN8)

  

 

**參考文檔**

[1] <https://cloud.google.com/compute/docs/ssh-in-browser?hl=zh-cn#supported_environments>

[2] <https://support.google.com/a/answer/10026322?hl=en&sjid=7511185769558089459-EU>