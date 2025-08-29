---
title: "AWS收到Unexpected Activity Detected通知處理方式"
date: 2024-12-11 01:23:00
categories: ["AWS"]
tags: ["AWS"]
permalink: /posts/awsshou-dao-unexpected-activity-detectedtong-zhi-chu-li-fang-shi/
---
 收到原廠的未經授權的活動(Unexpected Activity Detected)通知後

進入後台按以下步驟處理

1.至帳號下 Support case，確認此相關 account/billing case ” [Action Required] Unexpected Activity Detected on your AWS Account”。

2.查看cloudtrail記錄, 確認資源正當性。

3.刪除通知的access key。

4.回覆該 Case。

如要自證為正常使用，可附上使用者 data 操作紀錄。

也建議定期檢查所有IAM和更新現有憑證：

• 刪除多餘Access Key 和不常使用 IAM 使用者。

• 確認使用者 data 是否仍然需要，若不需要建議定期刪除

• 定期更新現有憑證與密碼

• 盤查所有帳號，建議開啟多重要素驗證(MFA)