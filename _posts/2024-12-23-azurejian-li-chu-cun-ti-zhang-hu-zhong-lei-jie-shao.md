---
title: "Azure建立儲存體帳戶種類介紹"
date: 2024-12-23 09:17:00
categories: ["AZURE", "AZURE教學30天上手"]
tags: ["AZURE", "AZURE教學30天上手"]
permalink: /posts/azurejian-li-chu-cun-ti-zhang-hu-zhong-lei-jie-shao/
---
# **Azure****建立儲存體帳戶種類介紹**

一、儲存體帳戶種類

在Azure存儲帳戶中，V1 和 V2 代表的是不同的帳戶類型，主要區別在於支持的功能和性能。

1. V2 儲存體帳戶（General-purpose v2）

* 特點：支援最新功能（Blob 分層存儲、審計、分析等）。
* 優勢：高性能、低成本、多存儲選項。
* 適用：現代應用、大規模數據存儲。

2. V1 儲存體帳戶（General-purpose v1）（目前版本已無此選項）

* 特點：基本存儲功能（Blob、文件、佇列、表格存儲）。
* 優勢：兼容舊應用。
* 限制：性能和功能較低，適用於傳統需求。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEisPzD1KNWVoy5mAt5ZkgeIAf4zYf7u7V0a2q1p3s6BupirUyXiGjufylxj69DvU7-F2nRsSueojk3ogigxtkusnRsHZgs2V3lOJQ670yE91z0rLfi7jvzqoKLyvnXNiWpFWkVCCPwNoDG0Z3Uhuj919IXaHgA2YrTDQBQDaCtOoRG-77-DxJDQSnboBWI=w643-h511)](https://blogger.googleusercontent.com/img/a/AVvXsEisPzD1KNWVoy5mAt5ZkgeIAf4zYf7u7V0a2q1p3s6BupirUyXiGjufylxj69DvU7-F2nRsSueojk3ogigxtkusnRsHZgs2V3lOJQ670yE91z0rLfi7jvzqoKLyvnXNiWpFWkVCCPwNoDG0Z3Uhuj919IXaHgA2YrTDQBQDaCtOoRG-77-DxJDQSnboBWI)

二、存儲帳戶的備援種類

在 Azure 中用來確保數據可靠性和高可用性的不同備援機制。這些選項確保了即使發生硬體故障、數據中心停機或區域性災難，您的數據仍然可以保持可用或得到恢復。根據需求可以選擇適合的備援選項來平衡成本、性能和災難恢復能力。

1. LRS（本地備援存儲）

* 描述：同一數據中心內保存 3 個副本。
* 適用：成本敏感、低災難恢復需求場景。
* 限制：無法防止數據中心級別的災難。

2. GRS（異地備援存儲）

* 描述：數據複製到另一地區（主地區 + 次地區）。
* 適用：需要跨地區災難恢復的關鍵應用。
* 限制：次地區數據僅在主地區失效時可用。

3. ZRS（區域備援存儲）

* 描述：多個可用性區內保存 3 個副本。
* 適用：需要高可用性和容災能力的應用。
* 限制：成本高於 LRS，僅部分地區支援。

4. GZRS（異地區域備援存儲）

* 描述：區域備援（ZRS）+ 異地備援（GRS）。
* 適用：需要極高可用性和容災保護的應用。
* 限制：成本最高。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjhesGdC316-7SrOiOs_fHxawS8ya8BMgCbABuo-ifFN2w-bhvhbbkb7wtXGOgV-whrUwzWv-0v13GpE6d6rp9nzn05hi9c0lWoAUOtxx_M231l7J4cpkCdCLreuk8legpP-0ipp6TOBbcSM4EtdxHBgiqD0nZsIelYxTBNzth5anqrEzcNOAauCEAuwhI=w640-h502)](https://blogger.googleusercontent.com/img/a/AVvXsEjhesGdC316-7SrOiOs_fHxawS8ya8BMgCbABuo-ifFN2w-bhvhbbkb7wtXGOgV-whrUwzWv-0v13GpE6d6rp9nzn05hi9c0lWoAUOtxx_M231l7J4cpkCdCLreuk8legpP-0ipp6TOBbcSM4EtdxHBgiqD0nZsIelYxTBNzth5anqrEzcNOAauCEAuwhI)

三、結論

選擇適合的備援選項取決於業務需求：

* 如果需要最低成本且不要求極高的可用性，可以選擇 LRS。
* 如果應用需要跨地區災難恢復並且不需要即時讀取次要地區的數據，選擇 GRS。
* 如果需要防止單個數據中心故障，並希望保證高可用性，可以選擇 ZRS。
* 如果需要更高的容災能力，能防止整個區域內的多點故障，並確保高可用性的應用，選擇 GZRS。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 備援項目 | 副本數量 | 數據範圍 | 災難恢復能力 | 成本 |
| LRS | 3 | 單數據中心 | 基本保護 | 低 |
| GRS | 6 | 跨地區 | 地區故障保護 | 高 |
| ZRS | 3 | 單地區（多可用性區） | 高可用性 | 中 |
| GZRS | 6 | 跨區域 | 區域與地區災難保護 | 高 |