---
title: "[AZURE]如何應對 Azure 虛擬機器創建失敗與內網設置問題"
date: 2025-03-03 01:44:00
categories: ["AZURE"]
tags: ["AZURE"]
permalink: /posts/azure-ru-he-ying-dui-azure-xu-ni-ji-qi-chuang-jian-shi-bai-yu-nei-wang-she-zhi-wen-ti/
---
 當在選擇可用區和虛擬機器類型時，發現創建失敗並顯示錯誤訊息，這是怎麼一回事呢？

[![](/assets/images/X-FAILMES.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYzZhN9A9L4jGaQtCA39yqmuIQCZdoTaibLyhyJ9omAtnj9-WatsGPWg0xeJAh3QovvCzOvXYAlbTMzX6KiWcLND7NrbPrcQrLvBaGSJSgKgqnQ088b0H34It7PShDy09SOXtbtdhFvAubVrCl_kXp64kntSBC2g9xerp2dS_Cj_UMPsfXKmvZhOVv1y0/s847/X-FAILMES.jpg)

  

根據查詢的原廠技術文檔[1]，該錯誤訊息表示所選擇的Azure區域在當前部署時暫無足夠容量來分配虛擬機器。

但即使在狀況發生前，已經先動手刪除多台舊的虛擬機器資源，依然顯示此錯誤訊息，這是為什麼呢？

根據原廠技術文檔[2]，Azure的虛擬資源在刪除後會經過一段時間才會完全釋放，因此並不會立即被用來補充現有的資源，但會隨著時間逐步調整。此外，同一可用區內的其他用戶可能會爭用資源。

而關於內網互通的需求，只需在同一區域內，Azure會提供多個可用區（通常有兩個以上）以減少單一物理區域故障的風險。對於內網需求來說，不同可用區之間的資源是可以完全互通的。

例如：在東亞地區（Zone 1 和 Zone 2），這兩個區域內的虛擬機器可以互相連接，無論它們位於哪一個可用區，IP地址也會在同一VPC內。

又舉例例如：

虛擬機器位於Zone 1：IP 192.168.1.1

虛擬機器位於Zone 2：IP 192.168.1.2

這兩者在網路層級上屬於同一網路，因此不會影響網路的功能性。

假如目前需要將新創建的虛擬機器設置在較接近現有虛擬機器的位置，應該如何選擇較適合的設置？在創建虛擬機器時，若出現「可用性選項」，選擇「無需基礎結構冗餘」，或者改用其他類型的虛擬機器，都可以順利完成創建。

[![](/assets/images/兩圖片.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjH-sI5qYer9Zu4VqXMl9y9DXBzFwv1myf9uLYnjQMZlZhy4JHlVAt0A07inuuLjv2ewKji4LUn2STU96eLQuWfSiQdZURxcDrb8B-xcG4XxiDigeN7XzSClam3X0PT0YNVj49dVza0yFEEh-YNVebILHb0VGOAc6ZM3kDldk-SkyKo4-WtWUysYQ6zz_A/s1858/%E5%85%A9%E5%9C%96%E7%89%87.jpg)

  

以上架設經驗與各位分享。另外技術文件鏈結參考如下

https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/windows/allocation-failure

https://learn.microsoft.com/zh-tw/azure/backup/soft-delete-virtual-machines  