---
title: "AWS Elastic Load Balancing介紹"
date: 2024-11-19 21:42:00
categories: ["AWS"]
tags: ["AWS", "Elastic Load Balancing", "ELB", "教學30天上手"]
permalink: /posts/aws-elastic-load-balancing-intro/
---
Elastic Load Balancing (ELB) 是一項自動將傳入的應用程式流量分配到多個目標（如 EC2 實例、容器、IP 地址等）的服務。

## 主要功能和特性

1. 流量分配：
   * ELB 能夠自動將流量均勻分配到多個目標上，確保沒有單一資源過載，從而優化資源利用率。
2. 健康檢查：
   * ELB 會定期檢查註冊目標的健康狀態，並僅將流量路由到健康的目標，這有助於提高應用程式的可靠性。
3. 自動擴展：
   * ELB 能夠自動調整其負載平衡能力，以應對流量變化，確保應用程式在高流量情況下仍能正常運行。
4. 安全性：
   * 支持 SSL/TLS 終止，集成憑證管理，並提供用戶端憑證驗證，以保護應用程式的安全性。
5. 即時監控：
   * 提供即時監控功能，幫助開發人員發現性能瓶頸並維護服務水平協議（SLA）的合規性。
6. 黏性會話（Sticky Sessions）：
   * ELB 生成一個名為 `AWSALB` 的 Cookie，並將其發送給用戶端。這個 Cookie 包含了與特定後端實例的映射信息。當用戶端發送後續請求時，ELB 會檢查 Cookie，並將請求路由到相應的後端實例。(僅支持ALB、CLB)

這項服務旨在提高應用程式的可用性和可擴展性，並且支持多種負載平衡器類型，如下圖所示

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjFq8qOYZSwsy8BCWjbGg_CWn8nUgOiwC-KltMHE2Fn4We7s5obNymdYhFTIHG0a6O7uFXr1CGASRBbpdNmdl3_uNESs8y5VJSvIkfNWAi0H84H_awPSI9SPXgYe9_pgxnDAcuLga1I8pV4m9j4123ronvZdVXiW067eCevG5qFCJLZagBe0gg2Qpqb-JOd=w640-h360)](https://blogger.googleusercontent.com/img/a/AVvXsEjFq8qOYZSwsy8BCWjbGg_CWn8nUgOiwC-KltMHE2Fn4We7s5obNymdYhFTIHG0a6O7uFXr1CGASRBbpdNmdl3_uNESs8y5VJSvIkfNWAi0H84H_awPSI9SPXgYe9_pgxnDAcuLga1I8pV4m9j4123ronvZdVXiW067eCevG5qFCJLZagBe0gg2Qpqb-JOd)

AWS 提供了四種主要的負載平衡器類型，可針對不同的使用案例：

## 1. 經典負載平衡器 (Classic Load Balancer, CLB)

* 層級：支持第 4 層（傳輸層）和第 7 層（應用層）。
* 用途：適合傳統的 HTTP/HTTPS 和 TCP 流量負載均衡。
* 特點：
  + 提供基本的流量分配功能，支持健康檢查和會話保持。
  + 不支持基於內容的路由，靈活性較低。

## 2. 應用負載平衡器 (Application Load Balancer, ALB)

* 層級：操作於第 7 層（應用層）。
* 用途：專為現代應用和微服務架構設計。
* 特點：
  + 支持基於內容的路由（如路徑和主機名），能根據請求內容進行流量分發。
  + 支持 WebSocket 和 HTTP/2，適合需要高級路由功能的應用。

## 3. 網路負載平衡器 (Network Load Balancer, NLB)

* 層級：操作於第 4 層（傳輸層）。
* 用途：設計用於高性能、低延遲的 TCP/UDP 流量負載均衡。
* 特點：
  + 能夠處理大量TCP 和 UDP 連接請求，適合需要高吞吐量的應用，如遊戲和實時通信。
  + 支持靜態 IP 地址，並能夠在高流量情況下保持穩定性。

## 4. 閘道負載平衡器 (Gateway Load Balancer, GWLB)

* 層級：操作於第 3 層（網路層）。
* 用途：主要用於處理來自雲和本地數據中心之間的流量。
* 特點：
  + 支持 TCP 和 UDP 協議，適合集成第三方虛擬設備（如防火牆）。
  + 提供透明流量管理，能夠實現高可用性和容錯能力。

ELB監聽用戶端 IP 地址的功能主要依賴於 HTTP 標頭和 Proxy Protocol。以下是如何在 ELB 中實現這一功能的詳細說明：

## 1. X-Forwarded-For 標頭

當使用 HTTP 或 HTTPS 負載平衡器時，ELB 會自動添加 `X-Forwarded-For` 標頭到請求中。這個標頭包含了客戶端的原始 IP 地址，允許後端應用程式識別最初發起請求的用戶端。

## 使用方式：

* 在應用程式中，您可以檢查 `X-Forwarded-For` 標頭來獲取用戶端的 IP 地址。

## 2. Proxy Protocol

如果您使用的是 TCP 負載平衡器（如網路負載平衡器 NLB），並且希望獲取客戶端的 IP 地址，則需要啟用 Proxy Protocol。這會將客戶端的 IP 地址和端口號作為請求的一部分傳遞到後端服務。

## 啟用方式：

* 在創建或修改 NLB 時，可以選擇啟用 Proxy Protocol。
* 後端服務需要能夠解析 Proxy Protocol 標頭，以提取客戶端的 IP 地址。

## 使用方式：

* 在支持 Proxy Protocol 的應用程式中，可以解析接收到的標頭來獲取客戶端信息。

## 3. 注意事項

* 安全性：使用 `X-Forwarded-For` 標頭時，確保應用程式能夠正確處理可能被偽造的標頭，以避免安全風險。
* SSL 終止：如果您在 ELB 上終止 SSL，則 `X-Forwarded-For` 標頭會被添加到解密後的請求中。如果不終止 SSL，則需要使用 Proxy Protocol。