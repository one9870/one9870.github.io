---
title: "AWS EC2當機(因EBS卷吞吐量超限)的對應做法"
date: 2025-01-05 01:09:00
categories: ["AWS", "AWS教學30天上手", "EC2"]
tags: ["AWS", "AWS教學30天上手", "EC2"]
permalink: /posts/aws-ec2dang-ji-yin-ebsjuan-tun-tu-liang-chao-xian-de-dui-ying-zuo-fa/
---
 當 AWS EC2 實例發生當機，我方進行報修後得到以下相關回應：

1.原廠工程師檢查EC2實例，未發現底層主機有硬件故障和異常時間

- status check/狀態檢查均無異常

2.原廠工程師通過CloudWatch檢查3個EBS卷，沒有發現3個EBS個卷有異常事件產生，但發現該卷vol-xxxxxx吞吐量超限：

”指標” VolumeThroughputExceededCheck: 1 表明磁盤操作導致吞吐量超過該卷的上限。

綜合分析，EC2底層主機以及EBS均無發現有明顯異常事件，所見異常可能與根卷在特定時間段的大量讀取且導致吞吐量超限有關聯。

處理 EBS 卷吞吐量超限的根本方法是升級 EBS 卷的類型和性能，根據需求選擇合適的 EBS 卷類型（如 gp3、io1、io2），並確保 EC2 實例的性能能夠配合使用的存儲資源。如果吞吐量經常超限，還需要考慮優化應用程式的 I/O 操作，或將負載分散到多個磁碟卷中。本篇先針對EBS容量、EC2類型與設置警報來做說明。

1. 檢查並升級 EBS 卷類型

EBS 提供多種類型的磁碟，根據需求選擇合適的卷型可以避免吞吐量不足的問題。可以考慮升級現有的 EBS 卷類型，以提供更高的吞吐量。

一般用途 SSD（gp3）：提供相對較好的性價比，支持自訂吞吐量和 IOPS。可以升級現有卷為 gp3，並根據需要設置吞吐量。(此選項可自定義吞吐量)

預設性能 SSD（gp2）：吞吐量會受限於卷的大小，因此，卷太小可能無法達到足夠的吞吐量。

性能 SSD（io1/io2）：提供高吞吐量和低延遲，適合要求高吞吐量和高 IOPS 的工作負載。

[![](/assets/images/EBS-create.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgP4V3OIiqejWBluc9hWFmCTXIF2Y4bd-h3rPJSdvGFpoq_zj7IoK476n4EcCNnL5xrkPMqr0s4FnLTjvhwUQyngDJvUVLrvlIEm8WQb_Pmf7xj-Ey1wNhQdet5jQexrlaeSaEloH9Hi1xdRS6suaGaTDGrIwPzIhk3w7G5-mihiE0ucrmhKYypBM8fuPE/s791/EBS-create.jpg)

  

2. 增加 EBS 卷的容量

如果客戶使用的是 gp2 類型的 EBS 卷，吞吐量是與磁碟容量有關的。具體來說，增加磁碟容量可以提高吞吐量，避免瓶頸。另請注意：增加卷的容量（相關數值至少大於 10 GiB）。

3. 調整 EC2 實例的性能

確保 EC2 實例的大小和性能配置適合工作負載。如果使用的 EC2 實例本身的網絡性能或磁碟性能不夠強大，可能會對吞吐量設有限制。所以應根據需求進行升級 EC2 實例，選擇更高網絡性能和 I/O 性能的類型。

但此一修改須將EC2停機，才能修改實例類型，之後啟動實例還需要再確認性能是否改善。

[![](/assets/images/EC2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiw6quoDPyErYtuyTtWYxqfTuku2B1DpRH49A-lHSpoP0RS3eKObZEqZdE8aFIKOIcoDV1Hi8qdqdh17jjW0PEOTQ9YrKl7iMSsRCGa3K3GUcdlDSYkr3bCXFAvSHw1ikUByXWvin62w0k1TrNQAFH22kK78l45jV7UyVzE1YIUdbknc_617kbVOKErP10/s594/EC2.jpg)

4. 監控 EBS 性能並設置警報(避免狀況再發生的處置)

使用 AWS CloudWatch 監控 EBS 卷的性能，設置警報來提前識別吞吐量接近極限的情況。可設置警報以便當 EBS 卷的吞吐量達到一定閾值時，及時進行調整。

在CloudWatch操作介面可創建監控警報，選擇 EBS 卷的吞吐量（VolumeReadOps, VolumeWriteOps, VolumeThroughput 等指標），設定當吞吐量接近或超過閾值時觸發警報，並通過電子郵件或其他方式通知。

[![](/assets/images/cloudwatch.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyTgklU2ozmpJ9lJAPz6u_TM0TdIjqHzNiKOfczW4gLU37AUIjsEne1UW4izcbq7lNPsbu47d-lFIO-jrAIWB41_2FM3vnUZYdR0qKUcxyXHVB9_PaLJ305ldUy8qRbMD-IT36qq7QrW8u1K7jhj3GIUSBpJEcj_24vqUqVTwtch29dn0_JEj94irtdQM/s694/cloudwatch.jpg)

另外對Auto Scaling相關作法應可緩解相關異常狀況，以上資料供大家參考運用。

若要進一步針對操作系統層面檢視，原廠建議安裝atop等工具以收集相關指標與資訊，可參考下面的2個文章鏈接：

- 如何為執行 Amazon Linux、RHEL、CentOS 或 Ubuntu 的 EC2 執行個體設定 ATOP 監控和 SAR 監控工具？ 請參考網址4

- 如何使用 ATOP 工具和 atopsar 工具，取得 EC2 Linux 執行個體中程序的歷史使用情況統計資料？請參考網址5

參考網址：

1. [Request Amazon EBS volume modifications - Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/requesting-ebs-volume-modifications.html)

2. [Amazon EBS volume types - Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

3. [Amazon EC2 instance type changes - Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html)

4. [設定適用於 EC2 Linux 執行個體的監控工具 | AWS re:Post](https://repost.aws/zh-Hant/knowledge-center/ec2-linux-configure-monitoring-tools)

5. [使用 ATOP 工具在 EC2 Linux 執行個體上監控歷史資源使用情況 | AWS Re:Post | AWS re:Post](https://repost.aws/zh-Hant/knowledge-center/ec2-linux-monitor-stats-with-atop)