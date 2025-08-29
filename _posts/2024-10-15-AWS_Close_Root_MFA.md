---
title: "如何關閉AWS root帳號的MFA"
date: 2024-10-15 08:18:00
categories: ["AWS"]
tags: ["AWS"]
permalink: /posts/ru-he-guan-bi-aws-rootzhang-hao-de-mfa/
---
 

警告！！

關閉 root 帳號的 MFA 是一個風險較高的操作，AWS 通常不建議這樣做，因為 root 帳號擁有整個 AWS 資源的完全控制權，一旦密碼或帳號資訊洩漏，可能會造成重大損失。

 

1.     
登入root帳號後，點選右上角帳號名稱，點選”安全憑証”，下拉到「多重要素驗証(MFA)」

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgQHzzjbRPCLGOFtmZq6HLPMUZq1nxLr88vH6dTmTxumzWTbj1uCcyyatc-OKe2dZQygIhA0zbQjGgnJfRGffYGN7y1u3s88ZA6eiKoYIygd2c7tN05ao_3VGQiyh8FZNL9NYtTmDkKH3G1WBbw3-ztZUNJXSdDMT07Cm-zllhBFG7N9fPsj0S_gZ_3nP1n=w902-h393)](https://blogger.googleusercontent.com/img/a/AVvXsEgQHzzjbRPCLGOFtmZq6HLPMUZq1nxLr88vH6dTmTxumzWTbj1uCcyyatc-OKe2dZQygIhA0zbQjGgnJfRGffYGN7y1u3s88ZA6eiKoYIygd2c7tN05ao_3VGQiyh8FZNL9NYtTmDkKH3G1WBbw3-ztZUNJXSdDMT07Cm-zllhBFG7N9fPsj0S_gZ_3nP1n)

  
  
> 選擇要移除的MFA裝置，點”移除”，會跳出警示訊息

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhXrKDtE2bMqBNxLGE-6Lgy0TBA3n_xhopA0567Hv6jm-rySpotIqskTyMHwGvAVhfbxAxi3Z-kJKdjPQosE_hQpbX7_EXyIy5E7f2b-FLpcPqu0NhaawuBphche4ggoFY-Rv9IQXIgdjjIaXrCOXQf-AasjSTDhZEtWqBbbFOs6vzbwOc4zprQvpH5IrB-=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEhXrKDtE2bMqBNxLGE-6Lgy0TBA3n_xhopA0567Hv6jm-rySpotIqskTyMHwGvAVhfbxAxi3Z-kJKdjPQosE_hQpbX7_EXyIy5E7f2b-FLpcPqu0NhaawuBphche4ggoFY-Rv9IQXIgdjjIaXrCOXQf-AasjSTDhZEtWqBbbFOs6vzbwOc4zprQvpH5IrB-)

2.     
MFA移除成功

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhPTrQJEVMaXEQ_-7JTM9Uur5khgFH8I-cgLmmdZ_9P5xf0VYJbAWVL8fOYiFJaOzzP8QpmgUEEpFv32r0JJ8Wj8_zms1bk0bJx8l329f481QWZXY8sPOAaquwFE2uo76cIzfTPLnbUdPn69Ogweq-3XRNELNxyqHDx-pDo_AHuduYdrl_z4CsridJGC0oL=w912-h397)](https://blogger.googleusercontent.com/img/a/AVvXsEhPTrQJEVMaXEQ_-7JTM9Uur5khgFH8I-cgLmmdZ_9P5xf0VYJbAWVL8fOYiFJaOzzP8QpmgUEEpFv32r0JJ8Wj8_zms1bk0bJx8l329f481QWZXY8sPOAaquwFE2uo76cIzfTPLnbUdPn69Ogweq-3XRNELNxyqHDx-pDo_AHuduYdrl_z4CsridJGC0oL)

  
  

 

3.     
刪除MFA後因原有裝置的驗証碼已無法使用，第一次重新登入root帳號時系統會寄信提供驗証碼，輸入後即可正常登入（後續即不再需要驗証碼，直到重新綁定MFA）

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhzpEPj_9L79N8NgCcL_s3nrAvgXKwQpcMUJAKTYC_zWDt7keKILAvxx9Q_isk3WnpeN10nxbXZU1OV9174tsrctNPycmCCR7MMKo8JybuD8ZzGBIx4Q4J_sKI3eOBxMDcDijbJwFNobwwBTcmGu26UIHrtdJePl7vZol5Z7_UkMI91RgNXv71pGwUb1CIW=w899-h446)](https://blogger.googleusercontent.com/img/a/AVvXsEhzpEPj_9L79N8NgCcL_s3nrAvgXKwQpcMUJAKTYC_zWDt7keKILAvxx9Q_isk3WnpeN10nxbXZU1OV9174tsrctNPycmCCR7MMKo8JybuD8ZzGBIx4Q4J_sKI3eOBxMDcDijbJwFNobwwBTcmGu26UIHrtdJePl7vZol5Z7_UkMI91RgNXv71pGwUb1CIW)

4.     
登入後系統會提醒要綁定MFA（可直接綁定或選擇跳過）

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh4pNAs8d85T_T0TwAVC_bIkuPL2oS0ooenGtwPePDNz2baTssqS8YbDvHXrPcP6yGBosKbBdo1ISxglVPszNB4h7_wOBEckkmKLENHQ3_SNxGFzpyx8Or15ElxXXcJKurXafgBQN1R0S2sHUzC-PU2nSZBDXnYehdC3MijtxQiYpHJgKN1Ip5BPE0xhd1J=w525-h565)](https://blogger.googleusercontent.com/img/a/AVvXsEh4pNAs8d85T_T0TwAVC_bIkuPL2oS0ooenGtwPePDNz2baTssqS8YbDvHXrPcP6yGBosKbBdo1ISxglVPszNB4h7_wOBEckkmKLENHQ3_SNxGFzpyx8Or15ElxXXcJKurXafgBQN1R0S2sHUzC-PU2nSZBDXnYehdC3MijtxQiYpHJgKN1Ip5BPE0xhd1J)

 

若選擇第二項綁定驗証裝置，可用Google Authenticator或Microsoft Authenticator，掃描QRcode後輸入兩次驗証碼即可登入

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhn90cu3xa2Svi-UhFkLskd8XC7YaVUao99LAiz_fwuwPVYraB96dtyi0zUN5q3gjgq-bAZMBP_hWAe8PJ1W1vsz1RKCpqcZMYq6nk3nH8sUCSKh9XUzPmVbOnuHZNUDuZ79mloh_Wyx-XYw2tWGwuTsvKuD8_RblkzdeZyux2RvCax9PlPySkPiGeIbpJ_=w530-h486)](https://blogger.googleusercontent.com/img/a/AVvXsEhn90cu3xa2Svi-UhFkLskd8XC7YaVUao99LAiz_fwuwPVYraB96dtyi0zUN5q3gjgq-bAZMBP_hWAe8PJ1W1vsz1RKCpqcZMYq6nk3nH8sUCSKh9XUzPmVbOnuHZNUDuZ79mloh_Wyx-XYw2tWGwuTsvKuD8_RblkzdeZyux2RvCax9PlPySkPiGeIbpJ_)

 

※MFA剛綁定完成後不可直接移除，必須重新登入一次才可正常移除

![上傳進度：已上傳 133849 個位元組 (共 133849 個位元組)。](/assets/images/transparent-2.gif)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg8VTYSZHUP63ngTLlFCbonaZqiY2x6OVZLJLSu_7vm0CNXSABzLaJWWbAu5dSvWNzpEWwfQAM5gcZfswgNtYLy9PA5td9G7d9SK_GIh4OGavO3ldfW1MDGleJqfKI1C_ck7JL8bq0_7RgFMTmJEZezFWM0t8Eg20lVp-vWsZ6tXdbUfrpgUrdlel5HX3jy=w921-h372)](https://blogger.googleusercontent.com/img/a/AVvXsEg8VTYSZHUP63ngTLlFCbonaZqiY2x6OVZLJLSu_7vm0CNXSABzLaJWWbAu5dSvWNzpEWwfQAM5gcZfswgNtYLy9PA5td9G7d9SK_GIh4OGavO3ldfW1MDGleJqfKI1C_ck7JL8bq0_7RgFMTmJEZezFWM0t8Eg20lVp-vWsZ6tXdbUfrpgUrdlel5HX3jy)

  
  
  
  

參考資料：

<https://docs.aws.amazon.com/zh_tw/IAM/latest/UserGuide/id_credentials_mfa.html>

 

<https://docs.aws.amazon.com/zh_tw/IAM/latest/UserGuide/id_credentials_mfa_disable.html#deactive-mfa-console>

 

 