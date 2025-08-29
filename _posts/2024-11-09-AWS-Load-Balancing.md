---
title: "AWS 調整負載均衡"
date: 2024-11-09 12:34:00
categories: ["AWS"]
tags: ["AWS"]
permalink: /posts/aws-diao-zheng-fu-zai-jun-heng/
---
[![](/assets/images/1234.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFMVMW_buYdWbiRw4kAS1itnbU6-64HDmFIHyA3uwLXc9Ao1bRcd1hZtpXmvD8iTy4huKjzsYpK84i3jvwx2E6c6MH3ZSMiMbBtzn7ayuYL6bPYVlIKbebaGiQqkOL716U370NPLqfhz8fuMxWnH1Vk-I_bBQoOujuN6z72EIX-tc6LR8EUBoI1ATI5YZE/s713/1234.jpg)

  
  
  
  
  
  
  

先理解開啟與不開啟差異

1.不開啟跨區負載均衡：

流量優先發送到同可用區的目標

(ex：來自 C 的流量優先發送到 C Nginx )

2.開啟跨區負載均衡：

平均分配流量到所有目標

一. 先選區域->搜尋EC2->負載平衡，就可創建負載平衡器

[![](/assets/images/125.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiJAFqM9ClzHHEbucyN5DEtsH7i633sbDO0h5STjF2icLgdBqqCqX4EL193VmgShiAt-Kkv-_v7uCEdlxIVN5cSYTExVPruinWWs3ocrx2V1PU1RW9-1WskqOdkEjHMabB-Ij3XMYsZoR8SQl-HDNSbTo9iPKYq7W5lmYPg2X83c4ike5K3RoDmage-S4y/s1381/125.jpg)

  

二.創建完畢，屬性可看到(跨區域負載平衡)預設是關閉->右上角編輯

[![](/assets/images/1254.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjsKoqiuVnD4Br4Rv4Qa-aEIvefaVeDj0LjOlRzq_zY1KBllL-RJhs7XAQrffi-NZShXdTYhmSY7adkwlkzfPv__PMZWG2SJlNaDwLOhlcs6Qz-Pqp2UJu0Tw-tFE7y35apLRMqc8m3i7cKXKDFSgk4Udew5Hwdfiy0P6HGssZp9mOV21ZyTfd0cCJ4pP8t/s1228/1254.jpg)

  
  

三.進入編輯->選擇是否開啟->選擇完儲存

[![](/assets/images/1212.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8XGZCI3JC3BNtHkAOa2iZlGE29F_9X7ztb9mVAiTbmNWvZuvAbJ5EQMyKOW8d8qD__3t8Nnaq9ODlO-k2EzZLc4LYvIrGzo2yqQeXJYYwzlggGjZQ7kjFs1_02_vEeuFnVHY0Wt3bbgpjw9wYrgYZD8aHrG_zwxSkrsE8sAvFzRUinPtaEuZAB2arzrMY/s639/1212.jpg)

  
  
  

參考資料:

<https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html>