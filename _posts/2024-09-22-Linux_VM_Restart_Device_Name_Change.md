---
title: "在 Linux VM 中，重新啟動或重新連結數據磁碟後，裝置名稱變更的問題如何解決?"
date: 2024-09-22 04:12:00
categories: ["Linux"]
tags: ["Linux", "VM", "重新啟動"]
permalink: /posts/linux-vm-restart-device-name-change/
---
### 問題徵兆：

1. VM 重啟後無法開機。
2. 重新連結數據磁碟時，磁碟裝置名稱變更。
3. 依賴裝置名稱的應用程式或腳本無法運行。

### 原因：

Linux 裝置名稱不保證每次重啟後保持一致，因為 SCSI 子系統會以異步方式掃描裝置，導致裝置路徑變更。

### 解決方案：

* 使用持續存在的裝置名稱（如：**UUID** 或 **文件系統標籤**）。
* 使用 **LVM** 的話，掛接時可用邏輯磁碟區名稱。
* 在 `fstab` 使用 `nofail` 或 `nobootwait` 參數，避免開機時磁碟無法掛接導致系統無法啟動。

這樣可以避免重啟後因為裝置名稱變更導致的問題。

**結論**：Linux VM 重新啟動或重新連結數據磁碟後，裝置名稱可能會變更，導致系統無法正常運行。要解決這個問題，可以使用持續存在的裝置名稱（如 UUID 或文件系統標籤），並在需要時修改 `fstab` 設定，確保 VM 能順利啟動並掛接磁碟。

參考連結:https://learn.microsoft.com/zh-tw/troubleshoot/azure/virtual-machines/linux/troubleshoot-device-names-problems