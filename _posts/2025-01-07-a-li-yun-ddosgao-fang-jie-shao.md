---
title: "阿里雲DDOS高防介紹"
date: 2025-01-07 21:39:00
categories: ["阿里雲", "阿里雲Alibaba Cloud"]
tags: ["阿里雲", "阿里雲Alibaba Cloud"]
permalink: /posts/a-li-yun-ddosgao-fang-jie-shao/
---
近期服務有被DDOS攻擊查看阿里雲DDOS高防，確認以下資訊

實例規格如下

![一張含有 文字, 螢幕擷取畫面, 數字, 字型 的圖片

自動產生的描述](/assets/images/AD_4nXfNXuKq3UZRFgaZcahTOhIBxJ3Gbwn1sUs9OX0zrEpkVAvmm4zoUC7RfgkUdqcxsoCARXj1w6jKF3cMyts1eOBG4Vrt9odqsSnX_DgsmciruKRgFQ9k9kTmaGKSaPD6oRkPHC7_7A)

如果攻擊是超過規格會在下方紅框處顯示事件(規格超限告警)、同理目的限速事件也是。如果控制台沒有數據代表就是沒有觸發規格超限告警、目的限速事件。另外，超限告警並非及時資訊，需要到周一10:00產出

然而，規格超限告警是當業務規格超出購買規格時提示的告警資訊，不會影響業務，當多次超出才會影響丟包等資訊；  
可以關注目的限速事件，當觸發目的限速事件會對業務產生影響。

  

此次攻擊最高為700Mbps，來自國內的攻擊，我們購買的防禦帶寬為300G，所以不會是流量攻擊造成影響，有查看到連接數異常上升，較有可能為連接型攻擊有部分請求漏過，導致源站服務異常(因為併發連接數為100,000，此次攻擊連接數已達270,000導致可能丟包)( 併發連接數可以作為影響服務的一個依據，具體要看您後端源站連線數承受能力)

![一張含有 文字, 數字, 軟體, 圖表 的圖片

自動產生的描述](/assets/images/AD_4nXeAJZA7ERWZnHCsfJbkzYdBQxalTrUOmvwPXVLTSkDq09N5oU4eSHjyZmM1w8sHsLPEXVJ3h7BHmAhVMVmxBT99tYpF3eWu5eQOA6OQwERVd8hqYHDCQ9KpuiJDveeAhXh0H1ak)

![一張含有 螢幕擷取畫面, 文字, 行, 數字 的圖片

自動產生的描述](/assets/images/AD_4nXfe0F1uHpQdWa79KL2SzxUBNmWa7LrrvbqgdI7KtKfxmoXHrmDQgAFxn60rpKeHBZajLEa-DNnhLCPH597mK8dgAbkA3-aU9U-NYLgulJ1E85ZOWeXql3nuwyw4ng6WhA9GWUZDBQ)

從攻擊分析也可看出為連接型的DDOS攻擊

![一張含有 文字, 軟體, 數字, 電腦圖示 的圖片

自動產生的描述](/assets/images/AD_4nXdg2sDa-rfIPgGHLsX94KgVKAnFRVJQWpNFUlxh71dUTS-lVL6OPO1f8vS1ReokmAgR9cR5FGXfPeejjLB7A7WOagRGzvwCawt_c1QvKfVKTONDWaoVhx0si_2-fTbuOaeBo3bn)

  

![一張含有 文字, 螢幕擷取畫面, 數字, 圖表 的圖片

自動產生的描述](/assets/images/AD_4nXd30Ttn38vx9mjXtVxNqQcn2F5fIXVdUKLzKS5m5bAtltjPWMqme932qcCzszNKVBOu-IgyNr2IAX93mVFTHRrvsP_0zDFA-HymKIY6m-gnYjF6zw5I_QpO1Ra0c4EDmkXwIROFFA)

  

因為這次攻擊我們也進行了調整，

對四層做源限速、目的限速策略，以及調整彈性QPS((會額外產生費用，只有超過基礎的QPS和連接數才會產生費用))，並且搭配AI智能防護保護四層的連接型攻擊

  

限速配置

例如正常用戶的存取頻率是60秒5次，那麼可以設定成60秒存取超過20次就會加入黑名單，若進入黑名單，則其連線請求都會被丟棄。

  

開啟彈性QPS，彈性QPS為300,000，新建連接數為200,000，併發連接數為4,000,000(可參考QPS 文檔)

![一張含有 文字, 軟體, 螢幕擷取畫面, 電腦圖示 的圖片

自動產生的描述](/assets/images/AD_4nXduw5qHcz3rTOcGeTBdcTbVaMmklmGGEr-faUQJcFOIOlHwsrhBhL06gCRSOwhB_RFMFQ6YMrrCSysYZHl8Cx-nciNgWymSNhqg-h_KxATJr6bQFC-NH4bYirVQvH-F4Nbp6KUy)

  

端口接入 為四層接入、域名接入 為七層接入

因為此次攻擊為針對WEB協議的CC攻擊還是建議改為七層接入避免影響服務

且因為是七層接入，遭受四層攻擊高防不會轉發，會直接丟棄，源站不會遭受影響，可以正常防護四層

  

文件參考

彈性QPS:

https://help.aliyun.com/zh/anti-ddos/anti-ddos-pro-and-premium/product-overview/billing-of-the-burstable-qps-feature?scm=20140722.S\_help%40%40%E6%96%87%E6%A1%A3%40%402330815.S\_BB1%40bl%2BRQW%40ag0%2BBB2%40ag0%2Bos0.ID\_2330815-RL\_%E5%BC%B9%E6%80%A7QPS-LOC\_doc%7EUND%7Eab-OR\_ser-V\_4-P0\_0&spm=a2c4g.11186623.d\_help\_search.i5

  

四層防護策略: 

https://help.aliyun.com/zh/anti-ddos/anti-ddos-pro-and-premium/user-guide/create-an-anti-ddos-protection-policy?spm=a2c4g.11186623.help-menu-28396.d\_2\_4\_0\_2\_1.1dbe5078MR8xOH

  

超限告警數據更新時間

![一張含有 文字, 螢幕擷取畫面, 字型, 數字 的圖片

自動產生的描述](/assets/images/AD_4nXfodrfAk-aIyB93PIh_uJDbNO_-mbqJM1BbJGUNRqI5MXndygNAB1RXZZlsKkqemZbnLuWkyvu-ejNaRYsP7Mkms0VJSTiDZsQcFClwIaPo4eflrPMb7QmovbsF8PVA4l9IMBa9)