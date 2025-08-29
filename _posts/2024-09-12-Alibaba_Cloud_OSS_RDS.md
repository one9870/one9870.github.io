---
title: "阿里雲OSS跟RDS"
date: 2024-09-12 06:53:00
categories: ["阿里雲"]
tags: ["阿里雲"]
permalink: /posts/a-li-yun-ossgen-rds/
---
以下將說明檢查阿里雲的OSS跟RDS服務

一、OSS

1. 若為 同城冗余（ZRS)，則可忽略

2. 若為 本地冗余（LRS)，建議可嘗試

(1) 跨區域搬遷

<https://www.alibabacloud.com/help/zh/oss/user-guide/crr/?spm=a2c63.p38356.0.0.51a071436q91Ic>

(2) 同區域搬遷

<https://www.alibabacloud.com/help/zh/oss/user-guide/srr>

(3) 或熟悉 ossutil，也可嘗試進行指令操作搬遷

<https://www.alibabacloud.com/help/zh/oss/developer-reference/ossutil-overview>

二、RDS

1. 若為 HA，則可忽略

2. 若為 單節點架構，建議可嘗試

(1) 利用之前的備份，在其他可用區或跨區域新建實例 (不要採用方法三、查詢時間點，可能會時間錯亂)

<https://www.alibabacloud.com/help/zh/rds/apsaradb-rds-for-mysql/overview-of-data-restoration-methods?spm=a2c63.p38356.0.0.52075740dXA4IR>

(2) 利用 DTS 進行數據傳輸

<https://www.alibabacloud.com/help/zh/rds/apsaradb-rds-for-mysql/migrate-data-between-apsaradb-rds-for-mysql-instances#concept-fxm-bhp-ydb>