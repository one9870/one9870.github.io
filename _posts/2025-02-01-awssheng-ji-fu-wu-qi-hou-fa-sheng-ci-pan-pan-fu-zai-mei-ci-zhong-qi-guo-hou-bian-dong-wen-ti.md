---
title: "AWS升級服務器後發生磁盤盤符在每次重啟過後變動問題"
date: 2025-02-01 13:53:00
categories: []
tags: []
permalink: /posts/awssheng-ji-fu-wu-qi-hou-fa-sheng-ci-pan-pan-fu-zai-mei-ci-zhong-qi-guo-hou-bian-dong-wen-ti/
---
 客戶詢問AWS升級服務器後，發生磁盤盤符在每次重啟過後會有變動的問題，後續卻又回覆說换uuid就恢復正常，就此狀況分析這個問題成因如下：

通常與磁碟識別和掛載的方式有關。根據描述，客戶升級了 AWS 服務器後，發現每次重啟後磁碟的盤符會變動，後來透過更換 UUID 恢復正常，這意味著問題可能與磁碟識別的持久性和操作系統如何管理磁碟的掛載方式有關。

[![](/assets/images/AWS-EC2-GP2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYOy9PcoNOVDHO1gGm4h4kh7rl5OvNXEM40mCMzEcliUmNfXEx2nU347upanzQGmlMVbqBbb8adahSMCDDnA98v0aR4W-eiljKQhQ6zuIZ1zOyYXTK6YkzdItgEUyv5EKwDq_yZo3SWcMKeXMA7EHAbCsNGOX_DPopKNtOKo828DIvHjhuFpK4M-VBzm4/s803/AWS-EC2-GP2.jpg)

原磁盤被前系統命名的名稱，舉例來說，通常使用 /dev/sdX 或 /dev/xvdX 的命名方式。這些名稱表示附加到實例的 EBS 卷。而在 AWS EC2 中，設備名稱通常會以 xvda, xvdb, xvdc 等形式顯示，其中 xvda 通常是根磁碟（Root Volume），也就是操作系統安裝所在的磁碟。

但UUID克避免此類問題因為是唯一編號，在 安裝Linux 系統的EC2 上檢視磁碟的 UUID：可以使用 blkid 命令來列出所有掛載的磁碟設備及其對應的 UUID。這會顯示每個磁碟和分區的 UUID。例如：

/dev/xvda1: UUID="1234-5678" TYPE="ext4"

/dev/xvdb1: UUID="8765-4321" TYPE="ext4"

所以此問題就是"前系統所認定的 /dev/sdX 或 /dev/xvdX" 不被新系統認定，而UUID不受影響。

以下是一些可能的原因和分析：

1. 磁碟識別方式的改變

在某些情況下，操作系統會依賴磁碟的 UUID (Universally Unique Identifier) 來識別和掛載磁碟。AWS 中的 EBS 升級或更換磁碟後，可能會導致原有的 UUID 改變，從而造成掛載失敗或盤符變動。

使用 UUID 來掛載磁碟能夠保證即使磁碟的設備名稱（如 /dev/sda）發生變化，操作系統仍然能夠正確識別磁碟並掛載。

2. 磁碟設備名稱變更

AWS 在啟動過程中可能會給 EBS 磁碟分配不同的設備名稱。例如，某次重啟後，磁碟可能被重新分配為 /dev/sdb 而非 /dev/sda。這會導致掛載點變動，尤其是在 /etc/fstab 文件中指定設備名稱的情況下。

如果使用了設備名稱（例如 /dev/sda）而非 UUID 或者 LVM 卷的掛載方式，那麼重啟後磁碟的設備名稱變化會導致掛載問題。

3. AWS 服務器啟動順序或自動掛載配置問題

在某些情況下，操作系統的啟動順序可能會影響磁碟的識別和掛載。特別是在多個磁碟或 EBS 卷的情況下，操作系統可能會錯誤地識別磁碟順序。

如果 /etc/fstab 中指定了磁碟的掛載方式，但磁碟的設備名稱不穩定，可能會導致盤符變動的問題。將掛載方式從設備名稱改為 UUID 或者 LVM 分區，能夠有效避免這些問題。

4. AWS 磁碟重新掛載的問題

在某些情況下，升級後可能會涉及磁碟的重新初始化，尤其是在更換了磁碟或修改了磁碟配置的情況下。這可能會導致某些磁碟的 UUID 更改或設備識別錯誤。

解決方案：

使用 UUID 或 LVM 挂载磁碟： 建議在 /etc/fstab 中使用 UUID 或 LVM 分區來掛載磁碟，而非依賴設備名稱（例如 /dev/sda）。這樣可以確保即使磁碟設備名稱發生變化，掛載仍然不會受到影響。

檢查磁碟 UUID： 使用 blkid 命令可以查看每個磁碟的 UUID。可以通過 lsblk -f 查看每個磁碟的掛載信息及 UUID，並將 /etc/fstab 中的設備名稱替換為對應的 UUID。

檢查 AWS 控制台設置： 確保在 AWS 控制台中，磁碟的配置正確，並且在啟動後沒有發生異常的掛載順序或識別錯誤。

總結來說，這個問題可能是由於升級後磁碟設備名稱的變動導致的識別錯誤，建議使用 UUID 來避免這個問題。