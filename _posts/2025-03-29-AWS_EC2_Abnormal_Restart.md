---
title: "若出現AWS EC2'數據不足'且異常重啟，應如何檢視與處置"
date: 2025-03-29 00:19:00
categories: ["AWS"]
tags: ["AWS"]
permalink: /posts/ec2-abnormal-restart/
---
            [![](/assets/images/FIRST0.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcHqexFh0RLgEFZlnrzhBcXHEzF1JYlmn8G3e43lGHv-xRcM4DB97wN5sbvxIivbiueuMoDwY4gRxcFnmaqTzIGZ6jHn_Ywy8yMqNi8geWFaUaNnFiiqiWNwKzrqcOdYqQji4Ovs-sP2VawsCfHUVTzKkCesEag34_qZtvZfgM4QVHkskUAyyOoXYrUDk/s1071/FIRST0.jpg)  
  

    當AWS EC2實例本身出現數據不足（例如存儲、內存或網絡資源不足）時，且因此發生重啟，通常是因為EC2內部資源分配或使用達到極限，導致實例無法正常運行，進而觸發重啟或宕機。可依序檢視EC2以下功能是否正常：

1. 檢查 EC2 實例的 CPU、內存和磁碟使用情況

    如下圖，在EC2檢視時選取並檢視項目如CPU、內存、磁碟與網路，會即刻呈現使用情形：

[![](/assets/images/EC2-statuVIEWCOMB.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXwwmcRa5Q93C2lIddJwWgBFf23RFU_3BtDE9AUlhuF0b2D8QEaGw3H2JITTqGR-fSa8SvUdhyaU4sveNirfjHzgWZzMm1hnG9VXTnXXBG5hANXZzzWkiipkw5eQzNpCXMrhq_gl_6A2uyX-sWh5_Nq9RK7mJfZgpTt7tH16rOaiWecJELoFS9KAN6kZA/s1251/EC2-statuVIEWCOMB.jpg)  

2. 查看 CloudWatch Logs

(1)查看EC2系統日誌：檢查 EC2 系統日誌，了解是否有硬體或系統錯誤的記錄。

(2)查看CloudWatch監控指標：在 CloudWatch 中查看 EC2 的 CPU 使用率、記憶體使用率、磁碟 I/O 等指標。這些指標能幫助確認資源過載的時間與資訊。

[![](/assets/images/LOG-CW.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgD1UyiC52NXVH7pBO6Fr2ZHJwUpZZJsse3clKfBgvE9d-22d8qXpiUdDsjXSvCmITRtacI8ayDs6Xv8wMsEO_89o5spZWChcIxkWuLzVQWWL1O5A-ESIDRB3ARxa5dYamVfBPf0l2993H5jx2rKVbPntYJPHwpsNA_Lzwh7feDS0ZZUYITPrPYk7ZWeDc/s938/LOG-CW.jpg)

[![](/assets/images/CW-EC2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxKTIvi-QC7s9BYb21Kxa_LvtgLeo4cqfZ9z79qnPzc_TXguk9ua6MD36gK4U3X8kxz0ygKrZf8Fwn2cLGziLQDZmIvxrCvkL7ExUtFDARi1tDvyfQSKOymxP9cVVtLMkfIdg2HyKuB98wrWaM4le9fEeyVZ6AEibZHyq92nbonaKVYq_pmJ8gMz3RWR0/s1308/CW-EC2.jpg)

3. 查看 AWS Health Dashboard

    有時 AWS 本身的基礎設施問題（如區域內的硬體故障）會導致實例異常重啟。可以查看 AWS Health Dashboard 以查看是否有任何影響你的區域或服務的問題。

[![](/assets/images/EC2-statu2-health.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlKgZRFhAph1alOJa6Q6IeEt8l-MZI4JU-XXKre6Ylkpq8CirpZAGRNoq6yZytHKuBU3TD4wE71A57xa7mdFy736w9K-5Ii8rKAE3tDjkeiqdlQLUcZl8O4QrYlB035cWkVK3gziDZWkvgGIp_WM57CsIF5334BZST0p4kw0Y_dgAI0b2ozEBi_kQJTtM/s1280/EC2-statu2-health.jpg)

常見的故障排除方法：

1.重啟實例：如果實例的狀態檢查未通過，首先重啟實例可能會解決許多暫時性問題。

2.停止並啟動實例：如果重啟無效，可以停止並重新啟動實例，這樣會將實例移動到新的物理主機上。

3.更換實例類型：若實例仍處於過載狀態，可以考慮升級實例類型(提升規格等)，並協助調整所需設定。

4.若異常發生當下有排程工作，應確認應用程式方面有無錯誤，是否有程式衝突/資源瓶頸

以下技術文技可供參考

[監控 Amazon EC2 資源 - Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/zh_tw/AWSEC2/latest/UserGuide/monitoring_ec2.html)  
  
[您的帳戶運作狀態 | AWS Health Dashboard | Global](https://health.console.aws.amazon.com/health/home#/account/dashboard/open-issues)

[CloudWatch 中的基本監控和詳細監控 - Amazon CloudWatch](https://docs.aws.amazon.com/zh_tw/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-basic-detailed.html)

  
  
  
  
  
  
  