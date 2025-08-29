---
title: "AWS ADS 和 MGN遷移應用"
date: 2025-01-03 00:40:00
categories: ["AWS"]
tags: ["AWS"]
permalink: /posts/aws-ads-he-mgnqian-yi-ying-yong/
---
AWS ADS 和 MGN遷移應用 

在進行地端伺服器（on-premises servers）遷移到 AWS 雲端的過程中，AWS 提供了多種工具來協助遷移工作，兩個常見的選擇是
**AWS Application Discovery Service (ADS)** 和 **AWS Application Migration Service (MGN)**。這兩者適合於不同的遷移需求，以下是它們的介紹和使用方式：

**AWS Application Discovery Service (ADS)**

* 功能：用於自動化地端伺服器的資料蒐集和分析，幫助你了解當前的 IT 環境和應用程式相依性，為遷移到 AWS 提供必要的資訊。使用 ADS，你可以獲取以下資訊：

+ 伺服器規格
  (CPU, Memory, Disk)
+ 應用程式相依性和流量模式
+ 效能使用情況
+ 網路架構

* 優點：

+ 自動化資料蒐集，無需手動分析現有環境。
+ 提供詳細的應用程式依賴性和資源使用情況，協助制定最佳的遷移策略。
+ 支援代理程式安裝及網路流量方式進行資料蒐集。

**使用 AWS ADS** **的步驟**：

1. **安裝
   Discovery Agent**：將 AWS Discovery Agent 安裝在需要遷移的地端伺服器上，它會自動蒐集系統性能和使用數據。
2. **使用
   Network-based Discovery**：如果不想安裝代理程式，可以使用網路式的資料蒐集，它通過分析網路流量來獲取系統資訊。
3. **查看分析結果**：在 AWS 控制台中查看 ADS
   蒐集到的資料，進行依賴性映射，瞭解哪些應用程式和伺服器之間有相互依賴。
4. **規劃遷移策略**：根據 ADS 提供的報告和建議，規劃伺服器和應用程式的雲端部署架構。

   [![](/assets/images/00001.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjVthlf_FBdkXnjMLUeYq1QUfVxV-U7WUj5eqxLonvsibJ9o5R_98gjJhvO11NJpR7SFoDc1c_GVsuWfjk1EWlDfpc6cFPQABLl4-bJ37BgcIZ_AnUZuVzsg9-pfWMSyCjWZG6MaN9Kl1p3Y52HgPcTynlHHg-tmhp09DeCq4CXqa8_1FKixNdiQy2VdI/s554/00001.png)

     

   **適用場景：**

   * 在進行伺服器遷移之前，想先深入分析現有 IT 環境、應用程式依賴性和網路架構的情況。

   **---**

   **AWS Application Migration Service (MGN)**

   * 功能：提供自動化的伺服器遷移服務，將地端物理或虛擬伺服器的工作負載遷移到 AWS 雲端，無需重新架構應用程式。
   * 用途：連續複製伺服器資料並自動化轉換，進行測試後可最小化停機時間，順利切換到 AWS。
   * 優點：
   + 持續的資料同步確保遷移過程中數據完整性。
   + 支援測試遷移，避免遷移後應用程式運行異常。
   + 遷移過程簡單，無需更改現有應用程式架構。

   **適用場景：**

   * 希望快速自動化地將伺服器遷移到 AWS，並且遷移過程需要保持最小停機時間的情況。

   **---**

   **AWS MGN** **的使用步驟：**

1. **設置遷移源和目標：**

* 在 AWS 控制台中啟動
  MGN，並添加需要遷移的地端伺服器。
* 配置目標伺服器的設置，包括 EC2 實例類型、VPC 網路設置等。

2. **安裝 MGN** **代理：**

* 在地端伺服器上安裝
  AWS MGN 代理程式。這將允許持續的資料同步，將地端伺服器的內容複製到 AWS。

3. **進行遷移測試：**

* 在實際遷移之前，可以啟動目標伺服器進行測試，確保應用程式和伺服器在 AWS 上能正常運行。

4. **最終遷移和切換：**

* 當所有測試完成並且一切準備就緒時，可以進行最終遷移切換。MGN 會將流量切換到 AWS 雲端伺服器，並最小化停機時間。

5. **關閉地端伺服器：**

* 一旦切換完成，地端的伺服器可以停機，並將所有操作轉移到 AWS 上。

[![](/assets/images/00002.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqaFZNZTeY1czLka_iBaaStxsMv8EatvfxvVo0S_WBFMD9TgzxpMjaDtzG-aOsNRaBb5x6t6W7mQfe_rVr8c-6v3G1D7RTuc1JZoP_yAHTfcdNw6BKOEF3h_KTycQJCJqyxUjBjp0yfhdv4U__uSKpa5ys29qY6lPFUWq9Dk7CjYI5Jo6Fb8mYcnhviwU/s415/00002.jpg)

**總結：**

* ADS 更適合在遷移之前進行環境的分析和規劃，了解系統架構和應用依賴性。
* MGN 則專注於實際的遷移過程，提供連續資料複製和最小停機時間的遷移服務，幫助企業順利完成遷移。