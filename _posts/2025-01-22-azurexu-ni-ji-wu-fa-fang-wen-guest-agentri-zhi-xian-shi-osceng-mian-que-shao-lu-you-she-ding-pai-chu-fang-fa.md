---
title: "Azure虛擬機無法訪問，Guest Agent日誌顯示OS層面缺少路由設定排除方法"
date: 2025-01-22 06:23:00
categories: ["AZURE", "AZURE教學30天上手"]
tags: ["AZURE", "AZURE教學30天上手"]
permalink: /posts/azurexu-ni-ji-wu-fa-fang-wen-guest-agentri-zhi-xian-shi-osceng-mian-que-shao-lu-you-she-ding-pai-chu-fang-fa/
---
若虛擬機為CentOS 7.9，且出現無法訪問，並且在Guest Agent日誌裏出現了以下記錄，顯示在OS層面未找到route來訪問網路。

2025-01-01T00:00:00 WARNING Daemon Daemon Could not determine primary interface, please ensure /proc/net/route is correct

2025-01-01T00:00:00 WARNING Daemon Daemon Primary interface examination will retry silently
2025-01-01T00:00:00 ERROR Daemon Daemon /proc/net/route contains no routes

2025-01-01T00:00:00 ERROR Daemon Daemon /proc/net/route contains no routes

2025-01-01T00:00:00 ERROR Daemon Daemon /proc/net/route contains no routes

2025-01-01T00:00:00 ERROR Daemon Daemon /proc/net/route contains no routes

2025-01-01T00:00:00 ERROR Daemon Daemon /proc/net/route contains no routes

潛在原因可能為：

1.在 Linux Guest OS 內的網路設定檔中使用靜態 的IP 位址。

（根據目前獲取的資料來看，可先排除。）

2.VM作業系統內可能mask或者移除了networking/clout-init/wicked/waagent 服務或其依賴服務。

(這也會造成虛擬機器無法取得 IP 位址的問題。)

3.VM的網路設定檔因其他原因而損壞。

緩解辦法：

1.可以先透過“序列主控臺”登入VM：

[![](/assets/images/20250120-0.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiofgTSdXzZ3BQNZyh-SLaGERzr5xtL423GvC63AQ57LdR15ebDoTyc-yT203nVJmryglDrMM2O35qqueC2mzDk0xJlxJPJI4-_AMgDIgkn3n1cAnm4ZJpxDrHMv-r62ojAi0xhPMWCrRwwZ5GofWpj3WRKilF7S33VGCeaSam-XH0cLCToZLNBPhkaBT0/s777/20250120-0.png)

![](/assets/images/transparent.gif)

2.運行以下指令來重新獲取IP，然後嘗試檢查連接是否恢復。

sudo dhclient -v

[![](/assets/images/20250120-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYgFCs0GCw2PS8s4-4fY9hEHaMhQ69edO4q3cBvltRwrZJWHrgAoCjHoQoe-D3W0OAOidfbMDvexwqp-wwOwjnbtOwLevb1s2ZTWqjKMdIIKxOEy4Wb4d10EY-hNAwwuGGoUQPosEIz3UBzVzVpAgjMUzwh9gTaHGjQSgB_a8IKOVa_xF7wpAPcKlQ_zA/s1075/20250120-1.png)

如果網路設定檔已損壞，即便dhclient後恢復了網路訪問，也建議採取以下步驟重置網路介面NIC。

[重設 Azure Linux VM 的網路介面 - Virtual Machines | Microsoft Learn](https://learn.microsoft.com/zh-tw/troubleshoot/azure/virtual-machines/linux/reset-network-interface-azure-linux-vm?tabs=azure-portal)

1. 前往 [Azure 入口網站](https://portal.azure.com/)。
2. 選取受影響的虛擬機器。
3. 選取 [ **網絡****]** ，然後選取 VM 的網絡介面。

   [![](/assets/images/20250120-2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-0U6CX6ckXtUDlvAcc_QRWI_albB-8Ou0yqxWucelqexVuDAGP9LKFSkweWdafVbl0JGozxfJG2rgAEvYnjPUMPSSFP7PZ8qkztREVR82raJhPc3jfGgNL_0ZSAUqITJOx-THxUeE6C3qjVo7JEzu0_8pFqjBrs7_Kt11ChcEekOvDVRZw67k1PPl0Q4/s469/20250120-2.png)

4. 選取 [IP 設定]。
5. 選取IP。
6. 如果未將 **[****私人****IP****設定** ] 設定為 **[****靜態**]，請將它變更為 **靜態**。

   [![](/assets/images/20250120-3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkpu79aBCRc_WQSBxXe1F4SlymYWYXyRaFCH7-rMVkea_e2VSFSaiMEcCQ4K8xu1cDwXAaQRHh1ybpZhWSZMCxfQsR_F0zWOvQ9-ho0w8emYYU2n3r46Vij4sN3eImBjLogwcIOAMGukjUXIJxlT0ILlxjYavrgTwNtT65AIu7PQBx8gAdIneCBrV0gVo/s573/20250120-3.png)
7. 將 **IP****位址** 變更為子網中可用的另一個IP位址。
8. 虛擬機會重新啟動，以將新的 NIC 初始化至系統。
9. 嘗試使用SSH登入。 如果成功，您可以視需要將私人IP位元址變更回原始位址。 否則，您可以保留它。

參考資料:[CentOS 生命週期結束 (EOL) 指引 - Azure Virtual Machines | Microsoft Learn](https://learn.microsoft.com/zh-tw/azure/virtual-machines/workloads/centos/centos-end-of-life)