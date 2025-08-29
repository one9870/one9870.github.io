---
title: "如何在 Azure AD 中建立用戶?"
date: 2025-01-17 03:32:00
categories: ["AZURE", "AZURE教學30天上手"]
tags: ["AZURE", "AZURE教學30天上手"]
permalink: /posts/ru-he-zai-azure-ad-zhong-jian-li-yong-hu/
---
## Azure Active Directory（Azure AD） Azure Active Directory，也稱 ( Microsoft Entra ID ) 是一種雲端式的身份和存取管理服務，可以幫助企業安全地管理用戶、應用程式及資源的存取權限。在管理使用者時，經常需要將具有相似需求的用戶集合成群組，以簡化存取控制的配

## Q1.那這樣Microsoft Entra ID是什麼? 跟他有什麼差別?A1. Microsoft Entra ID 是 Azure AD 改名後的名稱，功能幾乎完全相同，依然負責身份驗證和存取控制。這只是品牌上的調整，方便它整合進 Microsoft Entra 的身份管理解決方案。對用戶來說，實際操作和功能並沒有變化。 Q2. 為什麼我一定要建立Azure AD? 不能直接使用嗎? A2.  Azure AD是否需要建立才能使用？ 一般來說，Azure AD 並不需要你額外「建立」，因為它是 Microsoft 雲端服務的一部分，當你使用 Microsoft 365 或 Azure 訂閱時，就會自動包含在內。 Q: 我已經有 Microsoft 帳號，為什麼還需要 Azure AD？ A: 如果你只需要個人帳戶的基本功能（例如登入或存取個人 OneDrive），就不需要額外建立 Azure AD。 簡而言之，**Azure AD 本身不需要你手動建立**，但若你需要進一步的企業級管理和自訂功能，可能需要先擁有對應的 Azure AD 管理權限或目錄。

## **建立 Azure AD 的步驟**

### **1. 登入 Azure 入口網站**

## 1. 前往 [Azure 入口網站](https://portal.azure.com)。 2. 使用您的 Microsoft 帳戶進行登入。如果沒有帳戶，請先[註冊一個免費帳戶](https://azure.microsoft.com/free/)。

### **2. 建立 Azure AD 租戶**

## 1. 登入後，在左側選單中選擇 **Azure Active Directory(**Microsoft Entra識別碼)。 2. 點擊 加入>>**建立新的使用者**。 4. * **組織名稱**：輸入租戶的名稱，例如「MyCompany Directory」。 * **初始網域名稱**：這將是您的租戶唯一識別名稱，例如 `mycompany.onmicrosoft.com`。 * **國家或地區**：選擇您的組織所在地。 5. 確認輸入內容後，點擊 **建立**。 **提示**：建立完成後，可能需要幾分鐘來處理租戶的初始化。 ---

### **3. 添加使用者到 Azure AD**

## 1. 進入剛建立的 Azure AD 租戶。 2. 在左側選單中選擇 **使用者**，然後點擊 **+ 新增使用者**。 3. 填寫以下內容： * **使用者名稱**：為使用者指定一個唯一名稱，例如 `john.doe@mycompany.onmicrosoft.com`。 * **姓名**：輸入使用者的全名。 * **角色**：選擇使用者的角色，例如 **使用者** 或 **全域管理員**。 4. 點擊 **建立** 完成操作。 ---

### **4. 配置應用程式整合**

## 1. 在 Azure AD 主頁，選擇 **企業應用程式**。 2. 點擊 **+ 新增應用程式**，然後選擇： * **內建應用程式**：從清單中選擇常見的應用程式，例如 Microsoft 365。 * **自訂應用程式**：為自家開發的應用程式建立連接。 3. 根據應用程式要求，配置 SSO 或其他存取規則。 ---

### **5. 啟用條件式存取（選用）**

## 1. 前往 **安全性 > 條件式存取**。 2. 點擊 **+ 新增策略**，設置安全性條件，例如： * 只允許特定 IP 範圍登入。 * 啟用多因素驗證（MFA）。 3. 定義完成後，啟用策略。

###### 