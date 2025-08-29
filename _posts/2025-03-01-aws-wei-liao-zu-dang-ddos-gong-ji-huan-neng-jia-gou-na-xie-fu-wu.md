---
title: "[AWS]為了阻擋 DDOS 攻擊還能加購哪些服務"
date: 2025-03-01 01:28:00
categories: ["AWS"]
tags: ["AWS"]
permalink: /posts/aws-wei-liao-zu-dang-ddos-gong-ji-huan-neng-jia-gou-na-xie-fu-wu/
---
當遭遇DDoS攻擊後，為防止業務損失再發生，還可以購買AWS哪些服務來阻擋 DDOS 攻擊?

以下依序介紹：

1. AWS WAF (Web Application Firewall)

AWS WAF 是專為Web應用程式設計的防火牆，可以幫助您過濾不必要或有害的流量，並阻止惡意請求。AWS WAF 可以與NLB（及其他AWS服務如ALB、API Gateway等）結合使用，對進入的流量進行過濾。

(1)AWS WAF 配置：

自訂規則： 可以根據IP地址、HTTP標頭、URI、參數等設置自訂過濾規則。您可以設定特定的安全規則來攔截來自可疑IP地址或特定模式的流量。

自動規則： 可以使用AWS WAF提供的Managed Rule Groups，這些規則集由AWS或第三方提供，並且會不斷更新以防範最新的攻擊技術。

[![](/assets/images/AWSWAF.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTGRL6EfkqCo3YtI9zFDL-yQBciKENniXoL8F3g2X97gsW6tQOTAcSAx0Lw2M9Utq2ejgTspu_9fxemYDFAMEmI0XKuLUOWjLtTbmyc4mfzkwm4LyMujz6w-hQGczq9xQGvONjFFJhXX6v7vtdggMJSBHoDHamyXQUPEOrDrICwdrHiz2HEN_tVc9NH0A/s1169/AWSWAF.jpg)

  

(2)AWS WAF與Shield Advanced的整合：

Shield Advanced和WAF可以配合使用。WAF可以過濾不必要的HTTP/HTTPS流量，而Shield Advanced則專注於對抗大規模的DDoS攻擊。這兩者結合能提供更全面的防護。

  

2. AWS Shield

AWS提供了兩個層級的DDoS保護服務：AWS Shield Standard和AWS Shield Advanced。

(1)AWS Shield Standard：

AWS Shield Standard 是內建的免費DDoS防護服務，對所有AWS用戶自動啟用。它提供基本的防禦功能，可以抵擋常見的DDoS攻擊（如SYN/ACK flood、UDP反射攻擊等）。對於大部分基於互聯網的攻擊，此功能已能提供足夠的防護。

[![](/assets/images/AWSshield-X.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdK2Dz_4btTE2ws-MhOu97NyOiN5UzR5DOD4fN3AQH_QB_878oyG3367J7wHEKbnM6XMcg_5VlkPHnq4tUo2a5ogggi99eIjRfdsv1_YGrWDaOxXe2gIATkk3FSXmvY3svGDxf2Mcwg756wgKNhrao8cjPL7Y8lLSvrB4s68LVaHYHdypNXIkMEkoFVlU/s1347/AWSshield-X.jpg)

(2)AWS Shield Advanced：

如果面對的是更高層級的DDoS攻擊（例如大規模的攻擊），可考慮升級到 AWS Shield Advanced。此服務提供更高級的保護，包括：

。自動檢測和緩解更複雜的DDoS攻擊。

。高級DDoS攻擊報告和分析。

。與AWS WAF整合，可以針對攻擊模式進行更精細的控制。

。可以使用AWS DDoS成本保護，防止DDoS攻擊帶來的額外費用。

[![](/assets/images/AWSshield-2-1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4N_55IBRAANqnLeCAIudfkyA_LFp8334aBLGQNEwcpOH_RE6trP_mKGGqZJtWGz4UvDflR68mNDKgyX77rDWLl8X6HUmJsZMKmOa0PKuAymyZQ7vSsZGULw1a_DsefZQaPCIkeLL98CB-FX4XsTI2fDuZt99HhoD259CTV6srAg-njEmNSPSBouChC-g/s694/AWSshield-2-1.jpg)

3. AWS Firewall Manager

如果有多個AWS帳戶或資源，AWS Firewall Manager 可以幫助集中管理和統一配置WAF和Shield的規則。這使得防護多個服務變得更加簡單。

[![](/assets/images/AWS-FIRE.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZ7_Jqb9rMwgg3L24uNw7eQVlmE8FDWkeb1x5Ty-lPHx5-mbwCESAXjR9qJ8dcqoDhsZF2v1Clh7NypUOGbaN34s_NzzaSM5s-POhkmQ440uvpsxC4F0Qu84aBimfaOEZH3w6F-k3OrV2T7f6ttPcmlcvfGlcY88IasoemABkSX9WJDjxKOh178shmX9U/s998/AWS-FIRE.jpg)

  

4. Amazon Route 53

如果流量預判來自於全球，可以使用 Amazon Route 53 的 Geo DNS 和 Traffic Flow 功能來將流量分配到不同的區域，這樣可以減少DDoS攻擊的影響。

[![](/assets/images/AWS-53-0.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCvjA04t3l5GmhgPphDLcTKrtTJr_XPjtMZeiW-38cMtFfG0ZhWdodnnHWJxmxYt1ZJMILH838NgEhWh3wa2K6cY6LNNzaNUyCmbGjZNbEublZN_ffKpIZbHtF5LqamVPjtz0gX9tBpjWdcruSCWt2zUiLsFTJzm8jI9qopvHFJt7dcK5JjMAetDAznaM/s855/AWS-53-0.jpg)

  

5. Amazon CloudFront

將流量通過 Amazon CloudFront（AWS的全球內容傳遞網路）來加速，並利用它的DDoS保護。CloudFront可以緩解來自全球的攻擊流量，減少源伺服器的負擔。

[![](/assets/images/AWS-CLF.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgo-48J2V8QQgKsdQahn_l-Xf4xH9SxDepZzwErXh23NaN-G7k_RtFS0hwHawFCv8-dYikf94yFvlOcSiLr404zhool31SoDDjaDxDschUY_8z5JHplMzj04cPChAD63RUeHoViJRX1LAfdLgZvrjLvyKLONtmtd0JiHvfVt0gUpt15Z_sqefh-WX2IQQk/s1028/AWS-CLF.jpg)

  

總結以上服務，可以歸納為：

AWS Shield Standard：提供基礎且免費的DDoS保護，適合中小型流量攻擊。

AWS Shield Advanced：經付費後將啟用高級DDoS保護，適合面對大規模攻擊的情況。

AWS WAF：用來設定自訂規則來過濾HTTP/HTTPS請求，並防止不必要的流量進入。

AWS Firewall Manager：如果有多個帳戶或資源，此方面的設定將有助集中管理防火牆規則。

Amazon CloudFront：可以透過CDN來減少源伺服器的負擔，並提供DDoS防護。

參考文件：

[Responding to DDoS events in AWS - AWS WAF, AWS Firewall Manager, and AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-responding.html)

[AWS Shield Standard overview - AWS WAF, AWS Firewall Manager, and AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-standard-summary.html)

[AWS Shield Advanced overview - AWS WAF, AWS Firewall Manager, and AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html)

[AWS Firewall Manager - AWS WAF, AWS Firewall Manager, y AWS Shield Advanced](https://docs.aws.amazon.com/es_es/waf/latest/developerguide/fms-chapter.html)

[Amazon CloudFront - AWS Best Practices for DDoS Resiliency](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/cloudfront.html)

  
  
  
  