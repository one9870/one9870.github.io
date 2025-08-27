---
title: "AWS 帳戶異常活動處理方式"
date: 2025-06-09 03:43:00
categories: ["AWS"]
tags: ["AWS", "AWS教學30天上手"]
permalink: /posts/aws-unusual-account-activity/
---
 若收到如下列類似的AWS，帳戶異常活動通知，務必前往帳戶進行確認，避免被駭客入侵

以下為Access key 外洩信件範例:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhgIyPakNqcHkm_Wdu08BTKQOtLXMcVSfwXfqjjMC-p7gXLJAz-XNSHCFacjwansdZOJB7H4TIBbxlbG0Cxwl_N-7Z0Wca86WprlaMBTs7y9AIgoZqN0-1_18osvnwY-rCZ1KHLQx_TPDqQqYOUcj3Cf-y9CRk6DrbDdoBi6nHGoNW0JtkFt9FDBFLoZJM=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEhgIyPakNqcHkm_Wdu08BTKQOtLXMcVSfwXfqjjMC-p7gXLJAz-XNSHCFacjwansdZOJB7H4TIBbxlbG0Cxwl_N-7Z0Wca86WprlaMBTs7y9AIgoZqN0-1_18osvnwY-rCZ1KHLQx_TPDqQqYOUcj3Cf-y9CRk6DrbDdoBi6nHGoNW0JtkFt9FDBFLoZJM)

相關連結如下:

[[1]](https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Faws.amazon.com%2Fpremiumsupport%2Fknowledge-center%2Fpotential-account-compromise%2F/2/010001972a8487d8-82948692-b380-42a1-975f-94d13f54205c-000000/RVET4biRuei2nRRXO9bTFM_I3bI=428) [潛在不規則賬戶活動](https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Faws.amazon.com%2Fpremiumsupport%2Fknowledge-center%2Fpotential-account-compromise%2F/3/010001972a8487d8-82948692-b380-42a1-975f-94d13f54205c-000000/MWe-GNiHWcFOxjRakrRN4clMEHo=428)  
[[2]](https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Fdocs.aws.amazon.com%2FIAM%2Flatest%2FUserGuide%2Fid_credentials_mfa_enable.html/2/010001972a8487d8-82948692-b380-42a1-975f-94d13f54205c-000000/b9Mzfq5TEw_Ip0arunHr8K3M3-E=428) [在您的 AWS 根使用者](https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Fdocs.aws.amazon.com%2FIAM%2Flatest%2FUserGuide%2Fid_credentials_mfa_enable.html/3/010001972a8487d8-82948692-b380-42a1-975f-94d13f54205c-000000/7TASC0WvYWdYX6PnrsnPOwX9KWc=428)  
[[3]](https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Fconsole.aws.amazon.com%2Fiam%2Fhome%23users/2/010001972a8487d8-82948692-b380-42a1-975f-94d13f54205c-000000/qS2RALMqeZyGQrTMKiO2OL2eVOY=428) [上啟用 MFA https://console.aws.amazon。com/iam/home#users](https://console.aws.amazon.com/iam/home#users)  
[[4]](https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Fconsole.aws.amazon.com%2Fiam%2Fhome%23security_credential/2/010001972a8487d8-82948692-b380-42a1-975f-94d13f54205c-000000/nCpwbJ0ZBT_KkMV4u6aMb-UhTFc=428) [https://console.aws.amazon。com/iam/home#security\_credential](https://console.aws.amazon.com/iam/home#security_credential)  
[[5]](https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Fconsole.aws.amazon.com%2Fiamv2%2Fhome%23%2Fusers/2/010001972a8487d8-82948692-b380-42a1-975f-94d13f54205c-000000/0lYqZNZJHUU28bAGoUjoXEHIK2g=428) [https://console.aws.amazon。com/iamv2/home#/users](https://console.aws.amazon.com/iamv2/home#/users)  
[[6]](https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Fconsole.aws.amazon.com%2Fiam%2Fhome%23%2Fpolicies/2/010001972a8487d8-82948692-b380-42a1-975f-94d13f54205c-000000/LfQ8L0IHOIswmMCnCvs6k9PF45k=428) [https://console.aws.amazon。com/iam/home#/policies](https://console.aws.amazon.com/iam/home#/policies)  
[[7]](https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Fconsole.aws.amazon.com%2Fiam%2Fhome%23%2Froles/2/010001972a8487d8-82948692-b380-42a1-975f-94d13f54205c-000000/l2d15Z6B8poqG7ZN0pSPPRYP_gE=428) [https://console.aws.amazon。com/iam/home#/roles](https://console.aws.amazon.com/iam/home#/roles)  
[[8]](https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Fconsole.aws.amazon.com%2Fbilling%2Fhome%23%2Fbill/2/010001972a8487d8-82948692-b380-42a1-975f-94d13f54205c-000000/i8KEwcgoyJUxTB4oPOtj-zL2sCs=428) [https://console.aws.amazon。com/billing/home#/bill](https://console.aws.amazon.com/billing/home#/bill)  
[[9]](https://p6li1chk.r.us-east-1.awstrack.me/L0/https:%2F%2Fconsole.aws.amazon.com%2Fsupport%2Fhome%3F%23%2F/2/010001972a8487d8-82948692-b380-42a1-975f-94d13f54205c-000000/-ld9ygH1X0_rZuCtR512tohl7cU=428) [https://console.aws.amazon。com/support/home？#/](https://console.aws.amazon.com/support/home?#/)

以下為未經授權的IAM使用者信件範例

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh-q5A2mkI9awab3owKFzU4EKyWwkxtfkKoJTnE8-QWZW2CpGCmlBTPRPUDW23_zT_9nx-I1sxtPYKn7F11X7mq8vGpXNb5JTj4sfayxqh-_Dz-Q7rslsyItlYn2tHB9Ls-ohmFxmBAkGCuLvKbsHY5jVHGq58pBbi6h917kSINUxXMKAJoMbL8hMUhthI=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEh-q5A2mkI9awab3owKFzU4EKyWwkxtfkKoJTnE8-QWZW2CpGCmlBTPRPUDW23_zT_9nx-I1sxtPYKn7F11X7mq8vGpXNb5JTj4sfayxqh-_Dz-Q7rslsyItlYn2tHB9Ls-ohmFxmBAkGCuLvKbsHY5jVHGq58pBbi6h917kSINUxXMKAJoMbL8hMUhthI)

確認完畢後，回覆信件告知是否為異常行為

若有收到以上的類似相關信件，務必進行確認，避免後續產生異常費用，**或是帳戶被盜用情發生**