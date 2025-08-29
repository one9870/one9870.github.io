---
title: "華為雲 如何建立ECS"
date: 2025-03-12 14:55:00
categories: ["華為雲"]
tags: ["華為雲"]
permalink: /posts/hua-wei-yun-ru-he-jian-li-ecs/
---
# 如何建立華為雲ECS，這裡使用linux做範本，購買linux彈性雲端伺服器

 

登入華為雲後，在所有服務中，計算列選擇
”彈性雲服務器（ECS）”

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhiNa4jergdwrkVQIizs7D5mr1pOsbDwyOQtsaWh4XxSd-7wozQjgQUn_ERm0ysP8M2l9Ln97L7LQtgsZ-24A99nyHWQRi0JXXSp0TaXZMyY2hhx8EKVkvDsfD-hWNt-mTGi9Ka_kxFDsiuPEW2hjnPPHNZLghfew595ExcJcBc4WYnml64Ee_tafN3UjFp=w651-h407)](https://blogger.googleusercontent.com/img/a/AVvXsEhiNa4jergdwrkVQIizs7D5mr1pOsbDwyOQtsaWh4XxSd-7wozQjgQUn_ERm0ysP8M2l9Ln97L7LQtgsZ-24A99nyHWQRi0JXXSp0TaXZMyY2hhx8EKVkvDsfD-hWNt-mTGi9Ka_kxFDsiuPEW2hjnPPHNZLghfew595ExcJcBc4WYnml64Ee_tafN3UjFp)

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

進入彈性雲服務器（ECS）後，點擊購買 ”彈性雲服務器 ”

[![](/assets/images/3.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpKCcLtyngRJBEYlTLAD2GQGXL20Qa8ARsOz994OtJdB9msmhGwxDOB-FS2bngnvcI16Af1XPiJM7GuNKtFyeKZuge7sjnVksKUJUt0BYtiZdXsYSQ9HH6_qHO7qAJ1V1yyVy-_Ta5S_StDM9yh4xmU1gMUigbNDHHrHhxnpauvrf0Q820dcmM14LyIw8_/s1552/3.jpg)

  

**計費模式**

* 選擇計費方式。

+ **包年/包月**：適合需要長期使用的伺服器，通常會有折扣。
+ **按需計費**：適合短期或靈活使用，按實際使用時間來計費。

**區域**

* 不同區域的伺服器之間默認情況下無法直接訪問，因此選擇接近業務的區域可以降低延遲並提升速度。

**可用區**

* 可用區是指在選擇區域之內，實際部署伺服器的具體位置。
* 可以選擇
  **隨機分配**（由系統自動分配可用區），或者手動選擇具體的 **可用區 1**、**2、3。**

以下範例選擇使用按需付費，區域為華北‧北京一，可用區為隨機分配

[![](/assets/images/4.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0ciYNKx5f9diGxvH0ySlsHEMYIJxm8fPhknuEr5YA3v6SKKUNwe2fvvWc-h8Fbgo1s6UZlZoSBxWcE7897EKyAvSPcJj-6lLRIwxjhSMHbzQBbMsqwqNrC6YGZiGiTLEtmg4Xla0fwIy9e1EtklmeDo9rs8YX14V4-Pjqkvj7lSgz8J5WdRKG6m3nbTUy/s1536/4.jpg)

  

 

**選擇規格**

* 根據需求選擇合適的
  **vCPU** 和 **內存** 配置
* 查看
  **CPU 型號** 和 **帶寬**，確保符合性能需求。

這裡使用 s3.large.2：2 vCPU、4GB
內存。

[![](/assets/images/5.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPOMaHUnLIL84JBzfmQ-f74ArDSQyeRdHFItr8NKpTG86rqBasjPiOs9QY4LXWLedKe1M6MusM-QhJTze70f3VUO3DNHvOIr7s3JGJQ4m-B7JzGPg8PzA2slbGBILhy_2tYKsCHJjh2yDG6DmDT_7f5KcxD9fGO5aLXpP6yb-_WMW7TVXcoxayRB93zJru/s1457/5.jpg)

**選擇鏡像**：在「鏡像」部分，選擇所需的作業系統鏡像。

**配置磁碟**：

**系統碟**：系統磁碟是存放操作系統和基本軟件的磁碟。

**數據盤**：如需額外的儲存空間，可新增資料盤，並選擇適當的磁碟類型和大小。

 

加密設置：若需要安全性更高的磁碟，可以選擇啟用加密功能來加密磁碟上的數據。

共享盤：這是一種允許多個 ECS 實例同時訪問的磁碟存儲方式，適用於需要多實例共享存儲資源的場景，如高可用性部署和分佈式應用。

 

以下範例:

鏡像選擇「公共鏡像」中的CentOS 7.2 64位元，系統碟選擇了 普通 I/O 類型，大小40GB，數據盤選擇了 普通 I/O 類型，大小60GB。

選取完成後，點選下一步網路配置

[![](/assets/images/6.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiEk0ibi6ZAtXva22P_2bernsTNdJWIU84FjWlg1qdvKd_nNcPARuolS69zuIPpgQvPuckAdN3zB9Ryq1xqyuA5qnVsUx4LBSm2nbPh6zJb53hA9Iqk4oeVkSKi0iiBZB45WcZ6b3akEjDhODkb1N-QWB9b1_lTPaN3uDNBGqla0cG6fWbLPeYsCrAqkzmU/s1570/6.jpg)

  

 

**安全組**

* **安全組（Security Group）** 是一組防火牆規則，用於控制 ECS 的入站和出站流量。
* **常見端口設置**：

+ **80****端口**（HTTP）：開啟後允許網站訪問。
+ **443****端口**（HTTPS）：啟用 SSL 加密的網頁服務。
+ **22****端口**（SSH）：遠程登錄 Linux 伺服器，建議開啟。
+ **3389****端口**（RDP）：適用於 Windows 遠程桌面連接。

若不開啟
**22 端口**，會無法透過 SSH 登錄伺服器。

**彈性公網 IP**

* **現在購買**：系統將為 ECS 伺服器分配一個新的公網 IP。
* **使用已有**：如果帳戶內已購買公網 IP，可直接綁定。
* **暫不購買**：適用於僅內網訪問的伺服器，不會提供公網連接。

**帶寬配置**

* **靜態 BGP / 全動態 BGP**：

+ BGP（邊界網關協議）用於提供高可用的網絡連接，**靜態 BGP** 適用於一般應用，**全動態 BGP** 適用於高流量、高可靠性場景。

* **獨享帶寬 / 共享帶寬**：

+ **獨享帶寬**：專門分配給該 ECS 伺服器，確保穩定性。
+ **共享帶寬**：多個 ECS 共享同一個帶寬，適合多台伺服器共同使用。

**帶寬調整**

* **可調整範圍**：可以通過滑桿或輸入數值來設定帶寬大小。
* **選擇建議**：

+ **小型網站 / 測試環境**：1-10 Mbps
+ **中型企業應用 / 電商網站**：10-100 Mbps
+ **視頻 / 直播 / 高流量應用**：100 Mbps 以上

以下範例
帶寬使用10 Mbps，22port默認開啟，設定完後點選下一步高級配置。

[![](/assets/images/7.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXfGWqhO8O1ixnnpO3vPksbKdVV5KWe1_ofhyphenhyphend17S8qTWNF-Ef5wO34j9acN9-A1Mt6kob5l2OnQf8F-N0HzicycjT-kWCbZCCzjTcF4vyIyTc-ecFhtfm2n6Q2YIFvTSvkqRMaNI0k12jqbtVd7pSkOr7JoIvlIBfhJ0odrr0SecCBeWEYyOiivGE0Vn9/s1467/7.jpg)

  

[![](/assets/images/8.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9gN1lnWM9n5UL6uzOXacoE-6Hg5kDwf5hvMpHm4RGvPDBna5JYMYfLD2njVKYuYkZxQ6bv2_RWEIaeeHyZwawjQl2yNWx3nVxmxk1QW5svwzQaV5QHHRtyRExeVYaJYfL8hzOIcDj44mrIOoi4H1qFV8TUo4jGZblYVkQqPIwR9izgpx2EhRzJzMJOypO/s1573/8.jpg)

  

**雲伺服器名稱**

* 可自定義
  **ECS 伺服器名稱**。
* **允許重名**：如果勾選，購買多台 ECS 時，系統會自動為每台伺服器追加數字後綴（如 ecs-0001、ecs-0002）。

**登錄驗證方式**

* **密碼驗證**：

+ 適用於
  **快速設置**，但需記住密碼以便後續登錄。

* **密鑰對驗證**：

+ 更
  **安全**，推薦用於 **雲端伺服器**。
+ 需先
  **創建密鑰對**，並妥善保管 .pem 私鑰文件，登錄時需使用 SSH -i 命令。

 

以下範例使用密碼登錄

[![](/assets/images/9.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_Bt5SUmaCgIpBh_tzO00vTNbyzFj1E0aPdAeylKglL-nNoTmQwii8dJ4QEIC7C83bGxfgkjCL6MFHAyzhYO0WHnzL3nwjGPnWGjdnEgIQ9qOqM9kLM6iRv_lIy1iSrP51fo_UtAI7ZIbVGRUOQChMzxjfVdPnr8GzqyWMRFXNPnoG1IWDg1RFrEDjD4eM/s1520/9.jpg)

  

 

 **雲備份**

* **自動備份 ECS 伺服器的數據**，防止數據遺失或系統故障時無法恢復。
* **選擇**：

+ **現在購買**：立即購買備份存儲庫，確保伺服器數據可備份與恢復。
+ **使用已有**：如果之前購買過備份存儲庫，可選擇現有存儲庫來存放備份數據。
+ **暫不購買**：不啟用備份（不建議生產環境這樣做）。

**備份存儲庫**

* **名稱**：可以自定義
  **雲備份存儲庫名稱**（如 vault-1217）。
* **容量**：可根據需求選擇存儲大小，**建議容量不小於伺服器磁碟空間**。

**備份策略**

* **預設策略（defaultPolicy）**：

+ 設定
  **自動備份時間**。
+ 可點擊「管理備份策略」來自定義
  **備份頻率、保留時長、恢復計劃** 等。

**高級選項**

* **現在配置**：可立即設置雲伺服器分組，以便更好地管理多台伺服器。

 

以下範例
雲備份使用 現在購買，高級選項使用現在配置，設定好網路設置後，就可點選下一步確認配置

[![](/assets/images/10.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjsxTGENWAPK3kknKrSPDZ3cyAEi67QcEkc2797udLKWnt75PT8Ar53jwTEgTIOJTDGv43UQEB5iLHAm8XCPJlFHPWSXZQnFapDpFkfemjfp6UScBLv02i2Sq_4Mq1E-lElfX5Y6AwgKyo7OelIkF4ZsSqXjEfQhvFIf0Ejmg9m8-R48t5BrtKKDlQIE_R4/s1576/10.jpg)

  

 

確認 ECS 配置並完成購買 的頁面，**確保所有設置正確**後進行提交。

購買數量

* **數量調整**：可選擇
  **創建多台 ECS 伺服器**，最多可創建 200 台。
* **申請大配額**：如果需要更多伺服器，可點擊
  **申請大配額** 來增加創建上限。

**3.** **最終確認**

* **勾選條款**：需勾選才能繼續購買。
* **點擊「立即購買」**：提交訂單，系統將根據所選配置
  **創建 ECS 實例**。

[![](/assets/images/11.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDImxdgGwaDGiWOTZpj0guSupawtGCr0-83RXkQLvIlxtKM0e5Ina-MNzll6oRWBpG7DCpOwj2w31vi_0eJx7vXoOYpoPl5fizFgXZkglQbh26YRKPAnP5OlbELgWD1lSEb-oOaH3Sg9w2O43Y4zDOU4FlYYEscZx2AEiPEKx8AR6R9J2q0lcWmSzGNkmw/s1563/11.jpg)

  

Loading完後，就可在彈性雲服務器裡找到創建好的ECS。

[![](/assets/images/12.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgW_qYzpY-McFtgmaS8eWdpw4SJ3RDegvnlCRY7G0Dw6_m7wLINa61uyeMwBFjY-yNGGOt1fwnQ6oEBvXVlzQMQq0Vn5qWFzqHLLu6-bTZkdWayBh_wDlknO3PIe33YRxiM1h_QiAdC1gwMMzc9Fb2hbp-B8Okor5DpfCtOwpNW2TqEvhxkSvUn2uQqXMvN/s1554/12.jpg)

  

參考資料:<https://support.huaweicloud.com/bestpractice-ecs/zh-cn_topic_0130995884.html>

 