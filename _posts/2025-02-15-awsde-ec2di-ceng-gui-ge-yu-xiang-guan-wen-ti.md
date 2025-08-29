---
title: "AWS的EC2底層規格與相關問題"
date: 2025-02-15 00:25:00
categories: ["AWS", "AWS教學30天上手"]
tags: ["AWS", "AWS教學30天上手"]
permalink: /posts/awsde-ec2di-ceng-gui-ge-yu-xiang-guan-wen-ti/
---
 在AWS建立EC2時需要選定EBS 存儲選項，這些類型本身具有不同特性，會影響EC2效能，所以在選擇時應進行了解與審慎選定，以配合未來業務上的規劃與需求。

在 AWS EC2 中，gp2 和 gp3 是兩種不同的 SSD 類型的 EBS 卷（Elastic Block Store）。

    1.若客戶今日設定EC2運用的場景穩定，適合不需要太高配置，可以指定使用gp2。

    2.若設定EC2運用的場景，需要靈活的性能配置、高 IOPS 或高吞吐量的工作負載，  
       在設定初期就建議使用gp3。

而在客戶提問：如何將底層gp2 轉換成 gp3格式?

作業前須謹慎評量，並確認先數據備份，並於轉換時進行監控與調整，以應對相關風險。

在AWS EC2相關資訊中，點擊選定要進行變更的EC2，也要再次確認格式為gp2，然後利用Actions -> Modify volume來進行動作(如圖示)

[![](/assets/images/GP2-4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjO_BNw1q04bRyLbcqVPzx2cnWrjcpCMzPn9ePmvJbAV_uPJqqznOhFDgv3SWDORdTMb8TCzfqZDwntQlcL8Kae3vekwXTrzrQgvEVVfeg7Lc6-BHJXl2GAEyS4L2TuFhlzECU_QShtVz_cxf8494hkhVWJx-LhnZ_35UI-Z3vklKemSG7gN0ZdNYQoWkk/s825/GP2-4.png)

  

後續會繼續詢問相關規格(如圖)，依次輸入後即可Modify

[![](/assets/images/GP2-5.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8OmeORgAeQBwCfKBHF2Xenwli5sgaRJZxSWC-RnZVzRvs3qt7yZ22fw2dGkbzt-DtFbFp6LjS888xCfUyAzOe1_cQmGB9ZimSziJ11O5ZC276waC_3N3FkPim7evJ0Wybj1cPSseoMKuTSt4ZjEd978zrDKOAmnxX9cKNukD8FC7WSXUmGXSE-HgM0m4/s829/GP2-5.png)

  

後續完成動作後，相關設定可按照需求轉變。

另外，從 gp2 轉變(或稱為遷移)到 gp3 是一種簡單且經濟高效的升級。AWS甚至公告，其儲存成本降低了 20%，並且無需額外容量即可提高效能。可參考技術文件鏈結[2]；其他格式可參考技術文件鏈結[3]。以上資訊供大家參考運用。

參考文件

[1]將 Amazon EBS 磁碟區從 gp2 遷移至 gp3

https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-migrate-gp2-gp3.html

[2]https://aws.amazon.com/tw/blogs/storage/migrate-your-amazon-ebs-volumes-from-gp2-to-gp3-and-save-up-to-20-on-costs/

[3]https://aws.amazon.com/tw/ebs/volume-types/