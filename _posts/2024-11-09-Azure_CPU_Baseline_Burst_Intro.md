---
title: "Azure  CPU的Baseline & Burst介紹"
date: 2024-11-09 17:19:00
categories: ["Azure"]
tags: ["Azure", "CPU", "baseline", "burst"]
permalink: /posts/azure-cpu-baseline-burst-intro/
---
一、高載效能執行個體 (Burstable performance instances)  
  
傳統的 Amazon EC2 執行個體類型提供固定CPU資源，而高載效能執行個體 (Burstable performance instances)則提供Baseline CPU使用率，並且能夠將CPU使用率提升到基準層級以上。這可確保只需為基準CPU加上任何額外的突發CPU用量付費，從而降低運算成本。

**Baseline（基線）**：虛擬機在正常負載下可持續提供的 CPU 性能。

**Burst（突發）**：在高需求時，虛擬機可短時間超出基線，提供額外的 CPU 性能，適用於 B 系列 VM 這種支援**累積 CPU 積分**的實例。

從下圖的曲線(CPU使用率)來看，可以發現在A區大多時間CPU使用率並不高，平均CPU使用率是低於Baseline，但是到了某些尖峰時段，因工作量變大導致CPU使用率超過了Baseline。

[![](/assets/images/Burst.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUFf1JQbbJkXqPkGGy9mfx76cyDydaJN3yOzOF5TObFxbO29txw4r-gt2s6KQVjyxwSu_QhZklW95_O9ZrPs61QhGsqmvMVb241x8goL6DM3QlAe5on0Zh1U6b8kwTYwxcO1JaehoevzwvW6SVJPSZxyGpRcOpohvFaQPScf1HrnOiDhkSZRbXbNdu/s1768/Burst.jpg)

二、Burst Value的上限? 累積CPU積分是甚麼?   
  
1.Burst Value的上限以及累計CPU的積分會因為執行個體類型的選擇有所不同。  

2.在上面Burst的解釋有寫到**累積****CPU積分**，用個簡單的例子來說明(可配著上圖一起看)，**Burst Value的上限**就是公寓水塔的總容量 ;如何**累積CPU積分**就像是節約用水，可加快水塔的儲水速度(水塔有一直在補水的情況下) ; 使用的水量就是**CPU使用率**。  
  
在平常時段洗手、上廁所不會超過Baseline，使用水量小於補水量，這段時間就是在累積CPU積分**。**  
某個時段剛好大量用水，使用水量大於補水量，會開始消耗水塔內的儲水，這段時間就是消耗先前累積的CPU積分**。**

以上就是高載效能執行個體(Burstable performance instances)的大致概念。

參考資料:<https://docs.aws.amazon.com/zh_tw/AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.html#baseline_performance>

  
  
  