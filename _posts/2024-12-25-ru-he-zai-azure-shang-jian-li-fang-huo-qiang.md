---
title: "如何在 Azure 上建立防火牆?"
date: 2024-12-25 02:38:00
categories: ["AZURE", "AZURE教學30天上手"]
tags: ["AZURE", "AZURE教學30天上手"]
permalink: /posts/ru-he-zai-azure-shang-jian-li-fang-huo-qiang/
---
### Azure 提供強大的雲端資源，能夠讓企業輕鬆管理並保護其網路安全。防火牆是其中至關重要的一環，能夠幫助你保護網路免受未經授權的存取和網路攻擊。本文將教你如何在 Azure 上建立與設定防火牆。

---

#### 建立 Azure 防火牆的步驟

以下是逐步建立 Azure 防火牆的指南：

## 1. 登入 Azure 入口網站

首先，登入 [Azure 入口網站](https://portal.azure.com/)。確保你擁有訂閱權限，並且目標資源群組已準備就緒。

## 2. 建立虛擬網路 (VNet)

Azure 防火牆需要虛擬網路作為其基礎設施。

1. 在左側功能表中選擇 **"虛擬網路"**。
2. 點擊 **"建立"**，並填寫以下資訊：

   * **名稱**：為你的虛擬網路命名，例如 `MyVNet`。
   * **資源群組**：選擇或建立一個新的資源群組。
   * **位址空間**：定義 IP 範圍，例如 `10.0.0.0/16`。
   * **子網路**：新增至少兩個子網，例如 `AzureFirewallSubnet`（必須是 /26 或更大的範圍）和 `PublicSubnet`。
3. 點擊 **"檢閱並建立"**，然後確認設定。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgNkVkEXkWq-epLJ5VOnRKjkRBODFZ1NsHu4G6xqyp5JYYBAT3iWqKUb3Q4EWs3MPT6JDp-NryoMNSRTM_lyXv2CLAgyjQN0PcMEwIgKDn5T7lRoqiD5ZLFh_KcCDHu_Mzxly0OhcrkjJzZdCAOZFgt4YV1JQCsfHrxYeXfg9xP-cHVxM8Fc4iGPN5H_h3G=w599-h386)](https://blogger.googleusercontent.com/img/a/AVvXsEgNkVkEXkWq-epLJ5VOnRKjkRBODFZ1NsHu4G6xqyp5JYYBAT3iWqKUb3Q4EWs3MPT6JDp-NryoMNSRTM_lyXv2CLAgyjQN0PcMEwIgKDn5T7lRoqiD5ZLFh_KcCDHu_Mzxly0OhcrkjJzZdCAOZFgt4YV1JQCsfHrxYeXfg9xP-cHVxM8Fc4iGPN5H_h3G)  

## 3. 建立 Azure 防火牆

1. 在左側功能表中選擇 **"防火牆"**。
2. 點擊 **"建立"**，並依以下步驟進行：

   * **資源群組**：選擇剛剛建立的資源群組。
   * **名稱**：為防火牆命名，例如 `MyAzureFirewall`。
   * **區域**：選擇與虛擬網路相同的區域。
   * **虛擬網路**：選擇之前建立的虛擬網路。
   * **公用 IP 位址**：建立新的公用 IP 位址，並為其命名，例如 `MyFirewallIP`。

點擊 **"檢閱並建立"** 並完成部署

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg7EmpjUK3eCixUHvPn0QPERBNr6b0RMTZWA1zIl6xW6sdoU0GVchR37T3GskuRptj3pQygh8x7E9MtHERo18cnLzMWUV3iBgeI3yvNjN2mgIB-J_XxCeNVT-1oJ0CQjcbXnxsTXvkJfi6cCNAhD4bbGSWbHixcMibBSkjwIsigZhDRnf3ec66zSReOgKNr=w527-h343)](https://blogger.googleusercontent.com/img/a/AVvXsEg7EmpjUK3eCixUHvPn0QPERBNr6b0RMTZWA1zIl6xW6sdoU0GVchR37T3GskuRptj3pQygh8x7E9MtHERo18cnLzMWUV3iBgeI3yvNjN2mgIB-J_XxCeNVT-1oJ0CQjcbXnxsTXvkJfi6cCNAhD4bbGSWbHixcMibBSkjwIsigZhDRnf3ec66zSReOgKNr)  



## 4. 設定防火牆規則

Azure 防火牆支持應用程式規則和網路規則，以下是詳細步驟：

1. **應用程式規則**：

   * 適用於 HTTP/HTTPS 流量控制。
   * 在防火牆資源中，選擇 **"應用程式規則集合"**，點擊 **"新增規則"**。
   * 填寫以下資訊：

     + **名稱**：例如 `WebAccessRule`。
     + **優先順序**：例如 `100`（數字越小優先級越高）。
     + **目標 FQDN**：定義允許存取的網域，例如 `*.example.com`。
2. **網路規則**：

   * 控制基於 IP 的流量。
   * 在防火牆資源中，選擇 **"網路規則集合"**，點擊 **"新增規則"**。
   * 填寫以下資訊：

     + **名稱**：例如 `AllowSSH`。
     + **來源**：指定來源 IP 範圍，例如 `192.168.1.0/24`。
     + **目標**：指定目標 IP 範圍，例如 `10.0.2.0/24`。
     + **通訊協議與埠**：例如 `TCP` 和 `22`（SSH）。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiLD0N_Yi7mVpsA0-vgSBwW1Svt4Q2TwMkBpcQUCEVhGjryOtFV4tyJE___fnpklN90vhypnYdE16FAVfpTQmxm7tWwzy1M2aXMY7IilXcpCWL4S4Wo_xG7ss7rAiYFPtMImOhAKxYtNFeW2GQRY_S2UWZUvTi9RW_LLXx0cX_tiDt4jRNwWaVVREd3Z2B6=w795-h385)](https://blogger.googleusercontent.com/img/a/AVvXsEiLD0N_Yi7mVpsA0-vgSBwW1Svt4Q2TwMkBpcQUCEVhGjryOtFV4tyJE___fnpklN90vhypnYdE16FAVfpTQmxm7tWwzy1M2aXMY7IilXcpCWL4S4Wo_xG7ss7rAiYFPtMImOhAKxYtNFeW2GQRY_S2UWZUvTi9RW_LLXx0cX_tiDt4jRNwWaVVREd3Z2B6)  

## 5. 配置路由表

防火牆需要正確的路由來處理流量：

1. 在 Azure 入口網站中選擇 **"路由表"** 並建立新的路由表，例如 `MyFirewallRouteTable`。
2. 將路由表關聯到虛擬網路的子網。
3. 新增路由規則：

   * **名稱**：例如 `RouteToFirewall`。
   * **目標地址前綴**：例如 `0.0.0.0/0`。
   * **下一跳類型**：選擇 **"虛擬應用程式"**，並指定防火牆。

##### 6. 測試與驗證

1. 使用網路流量模擬工具，或者從受管制網段內進行連線測試。
2. 驗證流量是否符合設置的規則，並調整策略以確保最佳保護。

---

####