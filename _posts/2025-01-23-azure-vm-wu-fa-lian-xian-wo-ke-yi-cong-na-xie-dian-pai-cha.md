---
title: "Azure (VM)無法連線，我可以從哪些點排查?"
date: 2025-01-23 02:15:00
categories: ["AZURE"]
tags: ["AZURE"]
permalink: /posts/azure-vm-wu-fa-lian-xian-wo-ke-yi-cong-na-xie-dian-pai-cha/
---
**EX:如果我有一台正在使用的機器，突然無法正常遠端連線使用，我們能先做哪些判斷?**

### 步驟 1: 確認虛擬機器的基本狀態

1. **檢查 VM 狀態**：

* 登入 Azure 入口網站。
* 確認目標 VM 的運行狀態是否為 `Running`。
* 如果狀態為 `Stopped` 或 `Deallocated`，需要啟動虛擬機器後再進行遠端連線。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgWZ2DDDGImmNHrR9XIpfaKa48lNjkVjSXZNMe4PXbtTLu6zHxS3CXma5HdszvLmjk409sDKRewTM89U-_LGih2-F78DKwK9jAT2SU8x2xNsJUir0KXjBI8K0hzADNrSFhKe07iIGa1UEKNBKsMZ0Z7U4BTywmCmZEuUEkRlUL6lsepToLVj-wTYykMt4OO=w825-h441)](https://blogger.googleusercontent.com/img/a/AVvXsEgWZ2DDDGImmNHrR9XIpfaKa48lNjkVjSXZNMe4PXbtTLu6zHxS3CXma5HdszvLmjk409sDKRewTM89U-_LGih2-F78DKwK9jAT2SU8x2xNsJUir0KXjBI8K0hzADNrSFhKe07iIGa1UEKNBKsMZ0Z7U4BTywmCmZEuUEkRlUL6lsepToLVj-wTYykMt4OO)

### 步驟 2: 查看虛擬機器的效能監控

1. **檢查 VM 狀態**：

* **選擇虛擬機器**

  + 從虛擬機器列表中，選擇需要查看的 VM，例如「CDN-01」。
* **檢視概覽頁面**

  + 點擊左側功能選單的「**概覽 (Overview)**」。
  + 在此頁面中，查看虛擬機器的摘要資訊與效能監控數據。
* **查看效能與使用率 (Performance and utilization)**

+ 在概覽頁面中，你可以檢視以下指標：

- **CPU 使用率**
- **磁碟使用情況 (讀取/寫入位元組數)**
- **這些狀態可以判斷你的機器是否為正常運作中**

**[![](https://blogger.googleusercontent.com/img/a/AVvXsEgkAx6pI6gKGvXE-FUmIJQqXXDYUHi8jd4bR1oUHeubtGBjbJ4Q5VWhGA7WYyMK7wDvW4KQsTcMyLoK2H_C9IwnT7cC7xtDvaBtdRaVVqmXwW785CG3Jln4Sj-7qxirq4tSepwKdWdbk-0nnU94IuPll_aGIyw_prXt0Las_w2-QxXfrUuuTPCW_0WdVkzd=w807-h431)](https://blogger.googleusercontent.com/img/a/AVvXsEgkAx6pI6gKGvXE-FUmIJQqXXDYUHi8jd4bR1oUHeubtGBjbJ4Q5VWhGA7WYyMK7wDvW4KQsTcMyLoK2H_C9IwnT7cC7xtDvaBtdRaVVqmXwW785CG3Jln4Sj-7qxirq4tSepwKdWdbk-0nnU94IuPll_aGIyw_prXt0Las_w2-QxXfrUuuTPCW_0WdVkzd)**

### 步驟 3: 檢查與管理虛擬機器的網路安全群組規則 (NSG Rules)

### 1. **進入網路設定頁面** 2. 在虛擬機器左側功能選單中，點擊「**網路 (Networking)**」。 3. **檢視輸入連接埠規則** * 在「**輸入連接埠規則 (Inbound Port Rules)**」中，檢查當前允許的網路流量規則。 * 每條規則包含以下資訊： + **優先順序**：決定規則應用的先後順序，數字越小優先級越高。 + **名稱**：該規則的識別名稱。 + **連接埠**：該規則開啟的連接埠號，例如圖中顯示的 `22 (TCP)` 用於 SSH 連線。 + **來源**與**目的地**：定義網路流量的來源與目的。 + **動作**：規則是允許 (Allow) 或拒絕 (Deny) 連線。

### 步驟 4: 檢查虛擬機器的活動紀錄

### **可以查看的關鍵資訊**

### 1. **操作紀錄** * 確認最近是否有相關操作，比如： + 虛擬機器是否被 **停止 (Stopped)** 或 **解除配置 (Deallocated)**。 + 網路安全群組 (NSG) 的規則是否有變更。 + 連接埠是否被開啟或關閉。 2. **錯誤事件** * 查看是否有「失敗 (Failed)」的事件，這些通常會記錄操作過程中的問題，例如啟動失敗、配置更新錯誤。 3. **網路相關問題** * 如果有對網路接口 (NIC) 或網路安全群組 (NSG) 的更改，確認是否關閉了關鍵的連接埠（如 `22` 用於 SSH，`3389` 用於 RDP）。 4. **呼叫者** * 檢查最近是否有非授權的變更操作，例如其他用戶或系統更改了網路配置。 如果查詢以上狀態皆無異常，有可能是其他設定問題戶或者是網路相關問題導致無法連線，需直接開工單詢問。