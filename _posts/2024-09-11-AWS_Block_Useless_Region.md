---
title: "AWS 關閉沒在使用的Region(從account level block)"
date: 2024-09-11 00:38:00
categories: ["AWS"]
tags: ["AWS"]
permalink: /posts/aws-guan-bi-mei-zai-shi-yong-de-region-cong-account-level-block/
---
為避免同仁誤觸到其他region，故要 deny 掉沒有在用的 region，

目前SSO user 進去 payer 沒有 SCP permission 操作介面，且 Organization level 的服務監控

也需要手動設定，不能透過Organization 直接 apply，查詢相關資料後，

須建立 policy ＆ apply 到帳號上，所以須申請SCP權限

以下確認權限不足

![一張含有 文字, 螢幕擷取畫面, 軟體, 字型 的圖片

自動產生的描述](/assets/images/AD_4nXd9u4LL3fgPqi2LwGFyjalKfyGDu7sd7O8UazFHlZzxKgyZluilu20Z-ZRgziaVlzoD5k3uJWyMz9DnVMmsYwgQFF_OAn3B_8xOM-1CfIdFcl94DNfh7Pk6jhfTqDDLLlCZm2_qEQKwA5XZZjOT89APOAK4uyFoi5NK4f4pVg)

![一張含有 文字, 螢幕擷取畫面, 字型, 數字 的圖片

自動產生的描述](/assets/images/AD_4nXdv6K47jlRb-aWT2F4NFBN-NTKSA2EV9OH_kswTjK1Evlr3VekP3qbezoAuCqt0LZOQsuF4y3Ad3IBD-vd-Noikcew1XIAuEK42zlWhzMnVVlL2P-LFAxdYAKmvazciwwTpZ6tf-95bfVH2BetXIpr9v_oAlHaR5hyA_3iaCA)

如只是Organization level 的服務監控，用 Organization 直接 apply 啟用就可以

可參考文檔

<https://docs.aws.amazon.com/zh_tw/organizations/latest/userguide/orgs_manage_policies.html>

但發現文檔只適用 2019 之後開放的 region在這之前的全部預設啟用

![一張含有 文字, 螢幕擷取畫面, 數字, 字型 的圖片

自動產生的描述](/assets/images/AD_4nXeKweS-pLZLNRwwo03xDEmFUXn7OvJpMvayOiE5IkC2mIS7xmAvnAined25knwUNC9ePVw34WzNovgEbuuMVKRcWfL1G5EQMw1C8pp8hZDvDz4EWKZv5-RlqhpKnsoSBjL7z85L8TOdwz3iIK3ovkcTSLKFgAL2abdOnJp7jg)

IAM雖可以符合部分需求，而不需要申請SCP權限

https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html

1.可以先使用AWS頁面，將不必要的區域進行關閉

2.策略使用IAM進行控管 避免同仁誤觸

主要需要SCP權限，是因要從 account level block，避免其他同仁誤觸，故向原廠申請