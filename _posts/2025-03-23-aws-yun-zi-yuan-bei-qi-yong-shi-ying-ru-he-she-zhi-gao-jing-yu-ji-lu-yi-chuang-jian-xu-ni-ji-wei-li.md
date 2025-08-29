---
title: "[AWS]雲資源被啟用時應如何設置告警與紀錄(以創建虛擬機為例)"
date: 2025-03-23 01:00:00
categories: ["AWS"]
tags: ["AWS"]
permalink: /posts/aws-yun-zi-yuan-bei-qi-yong-shi-ying-ru-he-she-zhi-gao-jing-yu-ji-lu-yi-chuang-jian-xu-ni-ji-wei-li/
---
當帳號下出現啟用AWS新資源的操作時，如何設置自動告警並發送通知，並記錄後續行為？以下將設定以"創建新虛擬機EC2 實例"來舉例說明：

1. 啟用 AWS CloudTrail 並將事件發送至 CloudWatch Logs

    使用 CloudTrail 進行的記錄可以被用來進行安全審計、合規性檢查、故障排除和事件回溯。其中具備每個事件詳細信息（如時間戳、來源 IP、執行的 API、請求的參數等），可實時監控並將事件資料儲存於系統日誌中，供爾後檢視資源被啟用後的相關操作。

[![](/assets/images/01-OK-CT-11-CW.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoMuVzEJ2t6OE2XsK_bw3VXXbKLCbQoubZOOe5bEJ-yOBUXcnV0-YQ2ESw0OJkkWtcZUaiPmVbwt-EnFh4VUQUDeZA18CYa_G0aD57AJ-BoDT2AGengwhjrvjGFw8-htuml44fHumnoO_subz5FiSfRKFGNOOi-B0iolxEQngws6Ph0ignuVluUVzEpXA/s1093/01-OK-CT-11-CW.jpg)

  
  

2.設定AWS SNS主題與發送通知

   SNS (Simple Notification Service) 主題可設置告警接收者信箱資訊，使狀況發生時系統即刻發信給指定人員。

[![](/assets/images/07-OK-SNS.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZSqVPO0OexBrS6rr8Rc9iCYXFE1V1bZuyCtbvBKzRCgW7yt34aQ31tDAvE0B2a9qyOxAWbJTEsMiCILtrRPXlwWy1BsIPRf9Q3bOxDqrJpz203KmQtrnFo5KaAXiE9d3mprNChbtZhUHdGwuLmgC0IklFabU9Ky0pt3WwtbVezp6rGh9Y0KGgQKITt3M/s1146/07-OK-SNS.jpg)  
  

3.創建 AWS EventBridge規則

   此規則將監控 EC2 Instance State-change Notification事件，這是創建新 EC2 實例的觸發事件。相關參數如：state: ["pending"] ，代表 EC2 實例正在創建的狀態。另外，EventBridge 偵測到資源   被創建的行為後，會將事件傳遞至 SNS，以便發送通知。

[![](/assets/images/02-OK-EB-R.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXPKAXXQXxk0ACs53ZZKybozx7FgFQKJiGoUvXEdfroWAvK28rJlRAERdjXQQqogOhY-tLPI_wSXr9AK1NmOX5bebY4rU4q1JUTDsgraG84GJJEbGB8Q9q3UHCxxcdNCRyoA4LiP3SVXO6FajBJ8MQd90Xz_6LBN_C2kgJodYpULBEKHxj6DAXtcG7qiU/s1106/02-OK-EB-R.jpg)

  

4.測試與確認：

在此帳號下創建新虛擬機，將觸發 CloudWatch Alarm：

[![](/assets/images/04-OK-newec2on.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2lE-pjGafQCMBii9JGn8bcZZDvr5J6MezZw7fuecHzO9y2d_HCN8NPTnHfG3SO2dxsyrQMxoH6BxOqBkuxxcMZSvMnNzuG-UKcad5NGntSRSw_yLi4OHNTS4WW3Zckwhtgd0KVaEBW8EvEk-SlvC1nR17-3379HSuiG6tptIJ4UQfgyQOiV-cjbtaLwQ/s1120/04-OK-newec2on.jpg)

  

收到信件即表示設定正確。

[![](/assets/images/06-OK-newec2on-SNS.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMV_MAdlU3OYhmt53TPj3UpjSOCxE4OO1GNfU1-M8iOVBhKESCGI688eujb4X3ICR0GoAUJLR60nQNOSW5kBE8oOheYW9qF6PUFHR12ES7QABfGCPhdNqsV-TdTon_ZrCgFaSFIfTjfW-pyUuGxbHTgh1qXsTQXvMI843Sp_s6YFaK4YvjTNHPl0CIq8g/s663/06-OK-newec2on-SNS.jpg)

以上相關設定是啟動了自動化告警，提高使用者對雲資源的管理效率，也能及時發現資源被啟用，以降低額外運營成本。

參考資料：

[使用 Amazon CloudWatch Logs 監控 CloudTrail 日誌檔案](https://docs.aws.amazon.com/zh_tw/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html)

[傳送事件到 CloudWatch Logs](https://docs.aws.amazon.com/zh_tw/awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.html)

[使用 Amazon CloudWatch Logs 監控 CloudTrail 日誌檔案](https://docs.aws.amazon.com/zh_tw/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html)

  
  