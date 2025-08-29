---
title: "[AWS]如何將現有EC2完整資訊複製給新EC2使用?"
date: 2025-02-22 18:19:00
categories: ["AWS"]
tags: ["AWS"]
permalink: /posts/aws-ru-he-jiang-xian-you-ec2wan-zheng-zi-xun-fu-zhi-gei-xin-ec2shi-yong/
---
因業務擴展，將在現有AWS基礎上建立新EC2，並將原EC2資料複製給新EC2，以便參考與校正資訊。想確認要如何將舊機器裡的數據資料"完全的複製"到新機器上面去?

可以將舊EC2 在 EBS 快照功能裡，創建出一個新 EBS 卷，然後將這個卷附加到新 EC2 實例，這樣可以達到目的。步驟說明如下：

1. 創建 EBS 快照

首先，登錄到 AWS 管理控制台。進入 EC2 控制台，在左側會看到，選擇Elastic Block Store，點擊指定的EC2後選擇 Create Snapshot（創建快照）。填寫快照的描述，並確認創建。

[![](/assets/images/AWS-EBS-CS.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWWRRxdlK9H5iZ3SqrjjTkGNhKC5ihEVXQ_UoK35strhz6jdWfmMGTrk37OnqomiGQ3BxEeTehn8SIFUb-BT-PEK_8AZYGyX6UpjD-0c_XPktSMDbh1dPoTT5ccRbolnlGucOBJVTO_ybYa4EwRbb0XptLX_8AtQHtg_ZlcS7defMUaFRVzc0LFP_LoHE/s553/AWS-EBS-CS.jpg)

  
  

2. 從 EBS 快照創建新 EBS 卷

在左側Elastic Block Store點擊底下的Snapshot，勾選剛創建的這筆資料，並點擊右邊Actions，指定他選項中的”Create  volume from snapshot”

對話窗中出現volume的相關訊息，可以指定colume type類型，size大小，IOPS，可用區等資訊後，確定後按下”create volume”進行作業。

作業完成後將在左側Elastic Block Store的Volumes找到剛完成的volume。

[![](/assets/images/AWS-EBS-CVFS.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjGqPMot1mCFHsy4kCiCSS768bnHQjphfDY6XR6uvsSGSTspUUETT_1FKRleRY0zOY5rnslZkmx6Ea_bnUAAFzzE5o_3MhyE2jJy6yiqsRdWK_cWs0mgCB_aMbsmlsST4r5RrPcfyHbjuAmE59r4uk2LoZdyFrss2yimoR0HbajcZO-hJ2-gGLKuIXEkOU/s1286/AWS-EBS-CVFS.jpg)

  
  

3. 將新的 EBS 卷附加到新 EC2 實例

完成新 EBS 卷的創建後，你可以將它附加到新 EC2 實例。

在左側Elastic Block Store的Volumes（磁碟） 頁面中選擇剛創建的 EBS 卷。

點擊 Actions（操作），然後選擇 Attach Volume（附加卷）。

選擇要附加的 新 EC2 實例。

點擊 Attach（附加），將卷掛載到新 EC2 實例。

[![](/assets/images/AWS-EBS-AV-1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5fSNy1fDb1Wzr1HKFBsb_XiM1ucIQi0kmgzCfooIw3kvbI8o2VBaN9Kv-FhI5ORKnraUhy3rx0IEFKkl5gp3qUIFVBwOCeJ6P8RLo5FflfYgC49Ut-PZtLojqG8hSGkNq9E4VwY4XYojOjoclWvJ8oUJxEz5M1uOlnQZOelLFuiaar8FPbAKPAwP-Pt0/s782/AWS-EBS-AV-1.jpg)

  
  

4. 在新 EC2 實例上掛載新 EBS 卷

在新 EC2 上需要手動掛載該 EBS 卷，才能使其可用。以下以LINUX系統為示範：

(1)在使用SSH 登錄到新 EC2 實例後，運用指令 lsblk 或 fdisk -l 命令檢查新附加的 EBS 卷。通常會顯示為 /dev/xvdf 或 /dev/nvme1n1。

(2)在創建一個目標掛載點（例如 /mnt/data）：

sudo mkdir /mnt/data

(3)使用 mount 命令將 EBS 卷掛載到該目錄：

sudo mount /dev/xvdf1 /mnt/data

(4)如果這個 EBS 卷是用來存儲數據，則在掛載後可以開始使用它。

可參考資料

[Amazon EBS snapshots - Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html)

[Amazon EBS volumes - Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html)

[Make an Amazon EBS volume available for use - Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-using-volumes.html)