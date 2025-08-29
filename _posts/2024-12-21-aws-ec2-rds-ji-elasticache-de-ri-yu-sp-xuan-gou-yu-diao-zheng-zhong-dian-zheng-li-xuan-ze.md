---
title: "AWS EC2、RDS 及 Elasticache 的 RI 與 SP 選購與調整重點整理選擇"
date: 2024-12-21 01:28:00
categories: ["AWS"]
tags: ["AWS"]
permalink: /posts/aws-ec2-rds-ji-elasticache-de-ri-yu-sp-xuan-gou-yu-diao-zheng-zhong-dian-zheng-li-xuan-ze/
---
### EC2 的 Reserved Instances（RI）與 Savings Plans（SP）

標準RI

特點

l   僅能在同一實例係列中調整可用區（AZ）和實例大小。

l   無法跨系列或變更區域（Region）。

可轉換RI

特點:

l   支援同一實例係列內的AZ、實例大小及實例係列調整。

l   折扣比標準RI低，但更靈活，適合有調整需求的使用者。

 

Savings Plans

特點

l   Compute Savings Plans：支援跨Region、AZ，並能調整實例大小與系列，非常靈活。

l   EC2 Instance Savings Plans：僅支援同一執行個體系列內的AZ和執行個體大小調整。

// **建議**：若需要更高靈活性，**Compute
Savings Plans**是首選。

 

2.RDS Reserved Instances（RI）

特點

l   目前無Savings Plans選項，僅支援RI綁定。

l   RI綁定到特定**資料庫引擎（如****MySQL****、PostgreSQL****）**、**實例規格（如****db.t3.medium****）**、**部署類型（單區****/****多區）和區域**。

l   實例大小彈性：支援在相同資料庫執行個別係列中自動調整，但不支援跨系列調整。

**升降配置限制**

* 若需更改規格或區域，需購買新的RI覆蓋新配置，原RI繼續生效但僅適用於原條件。
* **可轉換****RI**允許在等值或更高成本下更改實例規格或區域，但靈活性較有限。

**建議**：固定負載使用RI以節約成本；動態負載可結合按需實例或其他方式靈活管理。

3️.Elasticache Reserved Nodes（RI）

特點

**綁定機制與限制**

l   Elasticache RI綁定到特定的節點類型（如cache.m5.large）和區域。

l   **升降配置限制**：

1.  不支援直接更改節點規格，若需更改，需購買新的RI覆蓋新節點配置，原RI繼續生效但僅適用於原節點類型。

2.  無Savings Plans選項，Elasticache RI只能通過手動規劃來優化成本。

**建議**：可以根據節點規模需求規劃RI購買，動態需求可考慮按需模式。

 

//備註重點

如果經常性有需要調整執行個體的配置，Compute Savings Plans會是EC2實例比更好的選擇。

而由於RDS和Elasticache，因它們沒有Savings Plans，因此會需要在規劃時仔細評估RI的使用情況，確保未來的靈活性需求。

標準RI適合使用穩定且無頻繁調整需求的場景；可轉換RI則較適合需要一定彈性的使用者。

 

參考資料:

EC2 Instance Savings Plans:仅可调整AZ套用至同系列实例

<https://aws.amazon.com/tw/ec2/pricing/reserved-instances/>

RDS: 现有的 RDS RI自动套用至使用相同资料库引擎的资料库执行个体系列

<https://aws.amazon.com/tw/about-aws/whats-new/2017/10/amazon-rds-reserved-instances-offer-instance-size-flexibility/>

Elasticache 可包含同系列节点调整

<https://aws.amazon.com/tw/blogs/database/new-size-flexibility-for-amazon-elasticache-reserved-nodes/>