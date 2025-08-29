---
title: "AWS EKS自動創建的服務器，為什麼卷沒有上標籤?怎麼解決?"
date: 2025-01-15 07:30:00
categories: ["AWS"]
tags: ["AWS"]
permalink: /posts/aws-ekszi-dong-chuang-jian-de-fu-wu-qi-wei-shi-mo-juan-mei-you-shang-biao-qian-zen-mo-jie-jue/
---
如果遇到用 EKS 建立節點（EC2 實例）時，這些實例自動附帶的 EBS 捲和網路介面並沒有自動打上他們想要的標籤。換句話說，EC2 實例標籤OK，但磁碟區和 ENI 標籤缺失，需要手動或額外配置來補上，如果遇到該情況該如何處置呢?

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh_b2qjz_o-EfJ5_dVKqAzLrHCI7TSBiqIwM59i6GLd_xDSPJyhVstUfCdYS5vcLMVNGeVLWn-1jjw47im3koLReD448TUW6PxNsdygv5chktglBSn5zOGuzT7pRaD5W6YJRxoNsxNwLxPL0RjXsj0CFy2u3tQQW7PUrqDhsoLRWz30wukKaJqYjiCtftLd=w1461-h210)](https://blogger.googleusercontent.com/img/a/AVvXsEh_b2qjz_o-EfJ5_dVKqAzLrHCI7TSBiqIwM59i6GLd_xDSPJyhVstUfCdYS5vcLMVNGeVLWn-1jjw47im3koLReD448TUW6PxNsdygv5chktglBSn5zOGuzT7pRaD5W6YJRxoNsxNwLxPL0RjXsj0CFy2u3tQQW7PUrqDhsoLRWz30wukKaJqYjiCtftLd)

可參考以下文件，定義標籤使用方式。

1. EKS （eksctl）：

使用 eksctl 定義EKS標籤

https://docs.aws.amazon.com/zh\_cn/eks/latest/userguide/eks-using-tags.html#tag-resources-console

2. EBS（Storage Class）：

使用 StorageClass 定義 EBS 標籤。

https://docs.aws.amazon.com/zh\_tw/eks/latest/userguide/create-storage-class.html

3. ENI（VPC CNI ）：

使用 VPC CNI 定義ENI標籤

https://docs.aws.amazon.com/zh\_tw/eks/latest/userguide/vpc-add-on-create.html