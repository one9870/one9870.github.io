---
title: "Azure雲端服務模型介紹"
date: 2024-11-25 01:58:00
categories: ["AZURE", "AZURE教學30天上手"]
tags: ["AZURE", "AZURE教學30天上手"]
permalink: /posts/azureyun-duan-fu-wu-mo-xing-jie-shao/
---
**Azure****雲端服務模型介紹**

**[![](/assets/images/圖片1-3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4Kt4sSqikZ__pc0Kjnzavhj_L_GrlZSqE7O68hNidlM9xwAUqx5u8MQbZgC1YjxaAXr-HrXYRWzd1CtVznci_E6ENT9lCczyW2yHrS0t6L1W-hu9UX13KHH8yVHrTgJAD-xpBs-7E1q0KQl9qusw25bqPhksBBwrALPV1LkvTDSPJmJJ6vGoV7dsKLnjJ/s554/%E5%9C%96%E7%89%871.png)**

**一. IaaS (Infrastructure as a Service)**

IaaS
提供基礎的計算資源，包括虛擬機、儲存空間、網路和操作系統，讓用戶可以自由管理並部署應用程式。

主要功能和特性：

1.虛擬機（Virtual Machines）：Azure 提供可自訂的虛擬機，用於部署和管理應用。

2.虛擬網路（Virtual Network, VNet）：提供安全的網路架構來連接 Azure 資源。

3.儲存服務（Storage Services）：

-Blob Storage：非結構化資料儲存。

-Disk Storage：適用於虛擬機的高效能磁碟儲存。

4.負載均衡（Load Balancer）：分散流量，提升應用可靠性。

5.自動擴展（Autoscaling）：根據需求自動調整資源使用。

6.高靈活性和控制：用戶可以自行選擇操作系統、網路配置及應用程式部署。

適用場景：

* 自行開發和管理的應用。
* 減少實體伺服器需求的基礎設施代管。
* 測試和開發環境。

 

**二. PaaS (Platform as a Service)**

PaaS
提供一個整合的開發和部署環境，讓開發者專注於程式碼，而無需管理基礎設施。

主要功能和特性：

1.App Service：用於快速部署 Web 應用和 API，支援多語言（.NET、Java、Node.js 等）。

2.Azure Functions：無伺服器運算，根據事件自動執行程式碼。

3.Azure SQL Database：完全管理的 SQL 資料庫服務。

4.開發工具整合：支援 Visual Studio、GitHub、CI/CD 等工具。

5.應用程式監控（Application Insights）：即時監控應用效能。

6.高可用性和自動擴展：平滑應對流量高峰，保證穩定性。

適用場景：

* 快速開發和測試應用程式。
* 架構現代化應用，例如微服務。
* 使用人工智慧、機器學習或分析的應用。

 

**三. SaaS (Software as a Service)**

SaaS
提供即開即用的應用程式，通常由 Azure 全面管理。用戶只需專注於使用服務。

主要功能和特性：

1.Azure Dynamics 365：整合 CRM 和 ERP 解決方案。

2.Microsoft 365（前 Office 365）：提供雲端生產力工具（Word、Excel、Teams 等）。

3.Azure DevOps：開發人員工具和協作服務。

4.Power BI：資料分析和可視化工具。

5.全面管理：Azure 負責基礎設施、更新和安全性。

6.即用即付模式：用戶只需為實際使用的功能付費。

適用場景：

* 中小型企業需要即開即用的解決方案。
* 無需自行開發的商業應用需求。
* 團隊協作和遠端工作。

**對比總結：IaaS、PaaS、SaaS 的差異**

**一. 控制權的差異**

* **IaaS**  
  可以自由選擇運行的操作系統（例如
  Linux、Windows），並全面控制虛擬網路的配置。
* **PaaS**  
  開發者只需專注於應用程式的開發邏輯，伺服器的維護和軟體更新都由平台負責處理。
* **SaaS**  
  使用者直接登入使用服務，例如 Microsoft Teams，無需關注任何基礎設施細節。

**二. 靈活性與客製化能力的差異**

* **IaaS**  
  可以在虛擬機上部署自訂的應用程式，例如大型資料處理或其他高需求工作負載。
* **PaaS**  
  適合快速部署 Web 應用，例如利用 Azure App Service，還能自動處理高流量的擴展。
* **SaaS**  
  雖然可以直接使用服務（如 Power BI 生成報表），但無法自訂其內部運作邏輯。

**三. 管理需求的差異**

* **IaaS**  
  用戶需要自行管理伺服器，例如修補操作系統漏洞及定期升級軟體。
* **PaaS**  
  伺服器升級由平台（例如 Azure）自動處理，用戶只需確保應用程式運行正常即可。
* **SaaS**  
  平台負責維持服務可用性，用戶只需專注於操作，登入即可使用功能。

 

[![](/assets/images/圖片2-2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgE3WZ53m0Nu7Hme_htbG4NNDPl3-xB6jwNZSF5zq0x12ZH9wUnSusbCtSvKrguu6sbjZV4raravzNCjzQYI3u-J0U5kFmjoWWi4BiSVQMJsJSq4lOFMHncqgCfg_PF3T32nGYIdTm7trqd4CgYSs58dyFjpQezBSgLcqfQYWnanOqxykm_hWJUq50q99jl/s506/%E5%9C%96%E7%89%872.png)

  

**四. 成本結構與彈性付費模式的差異**

* **IaaS**  
  適合短期內需要大量計算資源的項目，例如數據分析或影像處理。
* **PaaS**  
  適合長期開發且希望減少基礎設施管理的項目，例如企業內部系統。
* **SaaS**  
  非常適合日常業務需求，例如團隊溝通或自動生成報表等。

 

使用者管理與Azure管理

|  |  |  |  |
| --- | --- | --- | --- |
| 層級 | IaaS | PaaS | SaaS |
| 應用（Application） | 使用者管理 | 使用者管理 | Azure 管理 |
| 資料（Data） | 使用者管理 | 使用者管理 | Azure 管理 |
| 運行時（Runtime） | 使用者管理 | Azure 管理 | Azure 管理 |
| 中間件（Middleware） | 使用者管理 | Azure 管理 | Azure 管理 |
| 操作系統（OS） | 使用者管理 | Azure 管理 | Azure 管理 |
| 虛擬化（Virtualization） | Azure 管理 | Azure 管理 | Azure 管理 |
| 伺服器硬體（Servers） | Azure 管理 | Azure 管理 | Azure 管理 |
| 網路與存儲（Networking） | Azure 管理 | Azure 管理 | Azure 管理 |