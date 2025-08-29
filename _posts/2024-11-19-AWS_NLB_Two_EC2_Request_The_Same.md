---
title: "問AWS NLB如何調整才能使兩EC2所獲得請求一致"
date: 2024-11-19 11:35:00
categories: ["AWS", "NLB"]
tags: ["AWS", "NLB"]
permalink: /posts/wen-aws-nlbru-he-diao-zheng-cai-neng-shi-liang-ec2suo-huo-de-qing-qiu-yi-zhi/
---
如果在AWS上設置了兩台EC2實例，分別位於不同的可用區（Availability Zone），並配置了NLB（網路負載均衡器）來進行流量分配。目前注意到，當在兩台EC2實例上分別執行Linux指令 `netstat -tunlpa | wc -l` 來檢查網路連接數時，發現兩邊的結果並不一致。更具體地說，流量似乎大多集中在其中一台EC2實例上，這引發了相關的疑問。

[![](/assets/images/SET-NLB-LINUX.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxH5bgLZkKdEN0ssXDW6blNsqYzk3Rp-newl0scvjUDkHw49SeeKCjXM0VkZdYHTsuDq1I5uENj0Fj6NoUQUWPpqOyQCWej3czaMakME5Ahk7cAA4GwAAgJGDqVp2s-wacfLvw9BvGYnv7NK8aXJqi4JJobRuLLPPc7vmDVsGpu6p4mjACCdWNkh5R1OU/s1088/SET-NLB-LINUX.jpg)

目前使用的指令 `netstat` 是Linux中用來查看網路連線、路由表、連接埠狀態及相關統計資訊的工具。`netstat -tunlpa` 用於顯示所有監聽和非監聽的Socket連線，並顯示由程式佔用的TCP/UDP端口，通常會顯示多組數字。`wc -l` 是用來統計結果中顯示行數，即統計符合條件的連線數量。

**可能的原因：**

在這種情況下，造成結果不一致的原因可能有多方面，以下是幾個可能的方向：

1.NLB健康檢查設置：若NLB健康檢查設置不當，可能會影響流量分配，導致流量不均勻。

2.跨區負載均衡設定：默認情況下，NLB會將流量均勻分配到所有健康的目標EC2實例。如果未啟用跨區負載均衡（Cross-Zone Load Balancing），則流量將僅在每個可用區內的EC2實例之間進行分配。如果EC2實例分佈在不同可用區，可能會導致某區域接收更多流量，特別是在某可用區存在的EC2實例較少的情況下。

3.EC2實例配置問題： 目前所提到的 netstat 結果不一致，可能與EC2實例本身的配置或狀況有關， 比如某些實例處於高負載狀態，或者未能正確處理來自NLB的流量。

### 建議的步驟：

1. **檢查NLB健康狀態**  
   如圖所示，確認NLB的健康檢查結果是否為「健康」（Healthy）。如果健康檢查顯示正常，則可以進一步排查其他可能的原因。

[![](/assets/images/SET-NLB-Health.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWPIRZBbrSp6JnevGTFT7IEN7YoGTIgyBaMrrN1YwZ5AC2TapH7exBrz6pC_Sx9alj7GMYwnA8IUDsIZ1YGHyzbaNidtmqzkni89eLQmdX19f9oOuS1gogE8uJnU2QFFxFylrzIcpzvzmQ1oEz1EpHuNR0sEeEYJyPOxc9MJB4p0I5ySFRajSPTueXyUo/s1244/SET-NLB-Health.jpg)

  
    2.**檢查NLB是否開啟跨區負載均衡（Cross-zone Load Balancing）**        如圖所示，跨區負載均衡功能目前處於關閉狀態。  

[![](/assets/images/SET-NLB-cross-off.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFB2buUYyACuIxsxjLlT1j81lD1RFu7TK6f5VcYkzxeMQLv-jhdL9ufhyphenhyphenV3jufPtKQ-vUBBn-2ffaxTTWiREjcBuvbX8MGJSktUdo8Cx9jFaIywV8QFKzoGAAaWSgmbOmM5KvOdpCrM9t2qlzAcfvwWMxlARdtEI0GadD5UwxDmewi8xJMnvDKPMHmSks/s1000/SET-NLB-cross-off.jpg)

### NLB結論：

1. **NLB設置正常**  
   經過檢查，相關設置和配置均顯示正常，且健康檢查結果顯示為「健康」（Healthy），這表示NLB的負載均衡功能正常運作，並且在將流量分配到目標EC2實例時沒有問題。
2. **跨區負載均衡未啟用**  
   由於跨區負載均衡功能未開啟，而情境中並未提到有配置EC2集群，因此流量僅會在當前可用區內的目標EC2實例之間進行均衡分配。這並不影響負載均衡的運作，因為該功能僅限於跨可用區進行負載分配。
3. **問題可能出在EC2設置，而非NLB**  
   根據目前的檢查結果，問題並不在於NLB的配置，而可能是在設置的EC2實例上。如果需要進一步分析，就需要檢查EC2的相關日誌和配置資料，以便進行更詳細的排查。

**檢查 EC2 實例的資源使用情況**

EC2 實例的資源使用情況，如 CPU、內存、網路帶寬等，會直接影響其處理流量的能力。如果某台 EC2 實例的資源處於高負載狀態，它可能無法處理更多的連線請求。

* **CPU 和內存使用率**：檢查 EC2 實例的 CPU 和內存使用率。使用 `top`、`htop`、`free` 等工具來監控資源的使用情況。若某一台實例的資源消耗過高，則需要調整應用配置，或考慮升級實例類型。
* **網路帶寬使用**：檢查 EC2 實例的網路流量，確保其網路帶寬未達到瓶頸。使用 `ifstat`、`netstat` 等工具來監控網路帶寬使用情況。如果某台實例的網路帶寬達到限制，可能會影響其處理連線的能力。
* **負載均衡設置（應用層）**：如果 EC2 上運行的是應用程式（如 Web 伺服器、API 伺服器等），需要確保這些應用層的負載均衡設置是合理的。例如，若使用 Nginx、Apache 或其他反向代理服務，應確保其配置允許跨可用區均衡地處理流量。

### **檢查應用層的負載均衡配置**

如果 EC2 實例上運行的是 Web 服務或應用服務，這些服務的負載均衡設置也會影響流量的分配。

* **應用層的負載均衡**：如果使用 Nginx、HAProxy、或其他反向代理，檢查這些應用層負載均衡工具的設置，確保它們能夠均衡分配流量，並且不會因為配置錯誤導致不均衡的流量分配。
* **Session Stickiness（會話黏性）**：檢查是否開啟了會話黏性（Session Stickiness）設置，這會讓同一用戶的所有請求被定向到同一台 EC2 實例。如果開啟了會話黏性，則可能導致某台 EC2 實例的流量過高，另一台過低。可以根據需要調整會話黏性策略。

### **監控與性能調整**

* **CloudWatch 監控**：利用 CloudWatch 監控 EC2 實例的 CPU 使用率、網路流量、磁碟 IO 等指標，這可以幫助你發現性能瓶頸，進而調整實例配置或應用設置。
* **性能調整**：如果發現某台實例處於高負載狀態，可以考慮升級 EC2 實例類型，增加 CPU、內存、網路帶寬等資源，來提高其處理能力。也可以使用 Auto Scaling（自動擴容）來根據需求自動增加或減少 EC2 實例。

### **檢查應用程式或服務的配置**

如果你的 EC2 實例運行的是需要長時間保持連接的應用程式（例如 Web 伺服器、數據庫服務等），需要檢查是否有不合理的配置，導致某一台實例的資源被過度消耗，或是某些連線未被正確關閉。

* **TCP 連線數量**：檢查是否有大量的半開或掛起的 TCP 連線，這可能會導致某一台實例的負載過高。可以通過 `netstat` 或 `ss` 命令來檢查 TCP 連線狀態。
* **Keep-Alive 設置**：如果應用程式使用了 HTTP Keep-Alive 連接，確保設置合理。過長的 Keep-Alive 連線時間可能會導致不必要的資源佔用。

### **檢查網路拓撲與延遲**

在某些情況下，網路延遲也可能影響負載均衡的效果。雖然 NLB 會根據健康檢查將流量分配到健康的 EC2 實例，但如果某一台 EC2 實例所處的可用區（AZ）出現延遲或網路問題，可能會導致流量分配不均。

* **檢查 VPC 和子網配置**：確認 EC2 實例所在的 VPC 和子網設置沒有問題。網路瓶頸或錯誤的路由配置可能會影響流量分配。

若發現

關於NLB健康檢查相關操作可參考AWS原廠文件

https://docs.aws.amazon.com/zh\_tw/elasticloadbalancing/latest/network/check-target-health.html

  
  
  