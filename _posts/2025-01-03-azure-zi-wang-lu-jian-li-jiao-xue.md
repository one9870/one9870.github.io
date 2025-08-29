---
title: "Azure 子網路建立教學"
date: 2025-01-03 04:29:00
categories: ["AZURE", "AZURE教學30天上手"]
tags: ["AZURE", "AZURE教學30天上手"]
permalink: /posts/azure-zi-wang-lu-jian-li-jiao-xue/
---
 Azure 平台中的子網路（Subnet）是虛擬網路（Virtual Network，VNet）中的一部分，它允許用戶將虛擬網路劃分為更小的區域，以便進行網路隔離和更精細的流量管理。本教學將詳細介紹如何在 Azure 入口網站中建立子網路，過程簡單易懂，適合初學者。

---

### **前置條件**

1. 已有 Azure 訂閱。
2. 在 Azure 中建立了一個虛擬網路（VNet）。若未建立虛擬網路，請先參考 [Azure 虛擬網路建立教學](https://learn.microsoft.com/zh-tw/azure/virtual-network/quick-create-portal)。
3. 已登入 [Azure 入口網站](https://portal.azure.com/)。

---

### **建立子網路的步驟**

#### **步驟一：進入虛擬網路設定**

選擇基本資料，可調整訂閱帳戶以及資源群組，並填寫虛擬網路名稱

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiU3skhqFnXNVqJlgoAeIkqbj_lsurzp-4Nv-te9efTpwKquhB5rVGszVRwUVSxDDS5i6u55WzmV5olnfPD8TXGqFITfol1jIyHwVOO114WuEhMJI46sU7rE6Nnaq_VIoFM3Yhp6YjnD5cc3zLOK90n3UfVZ-9iq-mcgVGR6-uD9yTUwPfl4y9odCtUEftM=w580-h564)](https://blogger.googleusercontent.com/img/a/AVvXsEiU3skhqFnXNVqJlgoAeIkqbj_lsurzp-4Nv-te9efTpwKquhB5rVGszVRwUVSxDDS5i6u55WzmV5olnfPD8TXGqFITfol1jIyHwVOO114WuEhMJI46sU7rE6Nnaq_VIoFM3Yhp6YjnD5cc3zLOK90n3UfVZ-9iq-mcgVGR6-uD9yTUwPfl4y9odCtUEftM)

  

#### **步驟二：安全性**

這裡可以選擇啟用防火牆防護，若尚未設定防火牆，可以參考上一篇文章，另也可以選擇Azure DDoS 網路保護，不過這是要付費的，請自行斟酌

[![](https://blogger.googleusercontent.com/img/a/AVvXsEie6GnHo5kG9M1h0TVUDg5sPwbM4QwOaX3bGgb_XaM_fIty7OYZ15wzBHmqlbze4NaX2dOEUss737sMGsPvrna5ZR6RZ-rLvWpN1l8_qnDSIaK8pCONZXiy3-i4Z9AQJYtiFdQKrZwPp2X-tUHPUKSLFgMatyS6MSG92G_-O_BH71qDtz1RMtwFIaUpRACi=w666-h647)](https://blogger.googleusercontent.com/img/a/AVvXsEie6GnHo5kG9M1h0TVUDg5sPwbM4QwOaX3bGgb_XaM_fIty7OYZ15wzBHmqlbze4NaX2dOEUss737sMGsPvrna5ZR6RZ-rLvWpN1l8_qnDSIaK8pCONZXiy3-i4Z9AQJYtiFdQKrZwPp2X-tUHPUKSLFgMatyS6MSG92G_-O_BH71qDtz1RMtwFIaUpRACi)  

#### **步驟三：設定子網路資訊**

1. **名稱**（Name）  
   為子網路命名，例如 `Subnet-01`。
2. **地址範圍**（Address range (CIDR block)）  
   指定子網路的 IP 地址範圍，格式為 CIDR，例如 `10.0.1.0/24`。地址範圍需位於虛擬網路的範圍內，且不能與其他子網路重疊。
3. （選填）**服務端點**（Service endpoints）  
   若需支援特定 Azure 服務（如存儲或 SQL 資料庫），可以啟用服務端點。
4. （選填）**委派**（Delegation）  
   若子網路需支援特定服務（如 Azure Kubernetes Service），可以進行委派設定。
5. （選填）**網路安全群組（NSG）**  
   可將現有的網路安全群組（Network Security Group）關聯到子網路中，以管理進出子網路的流量。
6. （選填）**路由表**  
   若有自訂路由需求，可關聯現有的路由表。

#### 

  

#### **步驟四：儲存設定**

確認所有設定無誤後，點擊「**建立**」（Save）。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjdmXJkObggEClEbefUk3C-_wATwlb5wLAe4t8S8EdLXE8Q97udIyw_jWhpEc9nCYfNkKa20mfoaGL3FtiFwPdnQXL1e3YHW4CgAs3N_oXiL4ZXNLNe76xBGRyTH1TSy8wRc6-oHUXAxXCY4UIxhguJsMj_EamWYuHC59w5aHBGqC3CAfJuaYPqdKJjyefd=w596-h578)](https://blogger.googleusercontent.com/img/a/AVvXsEjdmXJkObggEClEbefUk3C-_wATwlb5wLAe4t8S8EdLXE8Q97udIyw_jWhpEc9nCYfNkKa20mfoaGL3FtiFwPdnQXL1e3YHW4CgAs3N_oXiL4ZXNLNe76xBGRyTH1TSy8wRc6-oHUXAxXCY4UIxhguJsMj_EamWYuHC59w5aHBGqC3CAfJuaYPqdKJjyefd)

  
  
  

---

### **驗證子網路是否建立成功**

1. 返回虛擬網路的「子網路」頁面。
2. 檢查是否出現剛剛建立的子網路名稱及其地址範圍。
3. 子網路成功建立後，您即可在該子網路中部署虛擬機（VM）或其他資源。

---

### **小提示**

1. **子網路大小規劃**  
   在設定地址範圍時，請根據需要容納的資源數量合理規劃地址大小，避免浪費 IP 資源。
2. **安全性設定**  
   建議為子網路配置網路安全群組（NSG），以防止未授權的流量進入。
3. **命名規範**  
   使用有意義的名稱，便於日後管理，例如根據功能或用途命名：`Web-Subnet`、`DB-Subnet` 等。

---

### **結語**

子網路是 Azure 虛擬網路的重要組成部分，能夠幫助用戶實現更高效的網路管理與隔離。本教學已涵蓋子網路建立的詳細步驟，您可以根據需求靈活配置子網路，提升雲端架構的靈活性與安全性。

如有其他疑問，歡迎隨時提出！