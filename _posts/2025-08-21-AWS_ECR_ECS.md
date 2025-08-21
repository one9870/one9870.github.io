---
title: "AWS ECR 與 ECS 的差異"
date: 2025-08-21 02:00:00
categories: [AWS]
tags: [AWS, Docker]
permalink: /posts/AWS_ECR_ECS/
---

#Content

兩項應用在不同的環節上，但整個CI/CD流程是可以串在一起。<br>
Amazon ECR 為受管的 AWS Docker 登錄檔服務。<br>
可以使用眾所熟知的 Docker CLI 來推送、提取和管理映像。<br>

AWS官方介紹：<br>
https://docs.aws.amazon.com/zh_tw/AmazonECR/latest/userguide/what-is-ecr.html<br>

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-vWvy3oDS42S6lyeGgKEQMDQXmKYZthttxKz4TEcgvaWSfMlSA_puEXHnmTT7AjmcpRSafpQGGJWfEWEcoFAkhNOZYkzCJIEJqSrZM2a08P8_wGeD95hdx9J7YD9YHR9HN4Yg4gsVPT1YeBozgONN5E1isfuoLSNLLN4y0t7C8WNM7OgyZbieSNGOFCR3/s800/ECRvsECS.png" alt="AWS官方介紹ECR與ECS的差異">

Amazon Elastic Container Service (Amazon ECS) 為全受管容器協同運作服務，可以輕鬆部署、管理和擴展容器化應用程式<br>
AWS官方介紹：<br>
https://docs.aws.amazon.com/zh_tw/AmazonECS/latest/developerguide/Welcome.html<br>

ECR是映像檔保存庫, 所以跟使用 Docker hub 方式基本是一樣的, 可以推、也可以拉, 當然也有建立與刪除<br>
詳細的建立與推拉作業, 可參考AWS文件：<br>
https://docs.aws.amazon.com/zh_tw/AmazonECR/latest/userguide/getting-started-cli.html<br>

ECR 的對比就是有名的 "公有的映像檔儲存庫 【Docker Hub】" <br>
自己寫程式, 自己打包後(如果是容器方式打包), 就可以放在私有的映像檔保存庫, 重要度較低的, 放公開的 Docker Hub 就可以了<br>
