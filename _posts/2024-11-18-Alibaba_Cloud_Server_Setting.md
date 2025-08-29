---
title: "2-3 阿里雲伺服器架設"
date: 2024-11-18 08:34:00
categories: ["阿里雲", "阿里雲Alibaba Cloud", "阿里雲教學30天上手"]
tags: ["阿里雲", "阿里雲Alibaba Cloud", "阿里雲教學30天上手"]
permalink: /posts/2-3-a-li-yun-si-fu-qi-jia-she/
---
**雲伺服器 ( Elastic Compute
Service • ECS)**

**ECS是阿里雲上提供伺服器租用的服務，包含CPU、Memory、OS、Network、Storage 等基本需求組成。**

**在阿里雲上擁有眾多的實例規格可以選擇，每種實例對於各自的強項阿里雲進行了分類，可以依據預計規劃要使用的場景選擇合適的實例：**

**以實例字母開頭區分**

**•C：計算型**

**•g：通用型**

**• r：記憶體型**

**• ne****：網路增強型**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgv23VxP_BySN7JABg09e_ZSIqhn6pEa8gI2pFMI8YddqL_rab9UDxFv6XvN6OMyKgu7GnhXakNi1aLlbifcyX2yxSw_OYYua9HfkcnEg4T5UmRIUojxMv1U5pjO3IFCgPI0SQvvFbop2AHBx1VCDNcrZkoCN5Df92NJP6CxF0waGb0wePyTyMC8A4-zQq7=w392-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEgv23VxP_BySN7JABg09e_ZSIqhn6pEa8gI2pFMI8YddqL_rab9UDxFv6XvN6OMyKgu7GnhXakNi1aLlbifcyX2yxSw_OYYua9HfkcnEg4T5UmRIUojxMv1U5pjO3IFCgPI0SQvvFbop2AHBx1VCDNcrZkoCN5Df92NJP6CxF0waGb0wePyTyMC8A4-zQq7)

  
  

**接著在實際建立ECS前，需要注意的幾項主要內容，如下圖：**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgoxvykHblXsI7_gZSNmUK8Anfe4xjhuYMTEnpmpnX4GERQ2f-IETNypxn3uvFlUXxHc4nCeniWTtSqRh6o4qDWZyKkjrE_sLxY3RCJAokvVmnIksVCcWXIR5iqWTHM37tGKWvXyRayRq-Ltdjk0jnDD2KD5JXXzZcS_h6k8zFIrKORJAinz1jEkbr_Q-Wh=w640-h382)](https://blogger.googleusercontent.com/img/a/AVvXsEgoxvykHblXsI7_gZSNmUK8Anfe4xjhuYMTEnpmpnX4GERQ2f-IETNypxn3uvFlUXxHc4nCeniWTtSqRh6o4qDWZyKkjrE_sLxY3RCJAokvVmnIksVCcWXIR5iqWTHM37tGKWvXyRayRq-Ltdjk0jnDD2KD5JXXzZcS_h6k8zFIrKORJAinz1jEkbr_Q-Wh)

  
  

**(1)  首先，在產品導覽找到雲服務器****ECS**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgYTtJLd4JUxsqdTdtoW4D6bHEJywdcSdPEPuINpaGkohpQsAoEaeEIyqHnDt4BToSG-0S4VAWqf4XZdt2tjug9iklkrP_C6Gy7-juGt97rC_ScUr3yASYc7J_Our3CAJRIhdJSBTB_biSZxaJxCiM1NKuMsEt-WVEHLNbd6JBlsi-y7DgDJ-drooEAnTs4=w640-h412)](https://blogger.googleusercontent.com/img/a/AVvXsEgYTtJLd4JUxsqdTdtoW4D6bHEJywdcSdPEPuINpaGkohpQsAoEaeEIyqHnDt4BToSG-0S4VAWqf4XZdt2tjug9iklkrP_C6Gy7-juGt97rC_ScUr3yASYc7J_Our3CAJRIhdJSBTB_biSZxaJxCiM1NKuMsEt-WVEHLNbd6JBlsi-y7DgDJ-drooEAnTs4)

  
  

**(2)  在ECS裡，找到實例，點選創建實例**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg4Uqw2jukEorV31jwDev8NsyGq_c2uCXeWaTx-ATZlMJANwkXRU5wGAMlxOQIcoTS9vSTpVT5AYySJidehdFOlmxSJcEfDmSsfDpPs9mv1pqjRxtN0fBvJ0DjeRzRSWxaEPa0kAXsMPrmubUvYR_knWL1nVsZZZ-90mka2sSCHZLmbhfJ5dmcdwVaAYmxV=w640-h316)](https://blogger.googleusercontent.com/img/a/AVvXsEg4Uqw2jukEorV31jwDev8NsyGq_c2uCXeWaTx-ATZlMJANwkXRU5wGAMlxOQIcoTS9vSTpVT5AYySJidehdFOlmxSJcEfDmSsfDpPs9mv1pqjRxtN0fBvJ0DjeRzRSWxaEPa0kAXsMPrmubUvYR_knWL1nVsZZZ-90mka2sSCHZLmbhfJ5dmcdwVaAYmxV)

  
  

**(3)  基礎配置**

**a. 首先，可以看到計費模式有三種模式:**

**l   包年包月(每月付費，長時間可以有折扣)**

**l   按量付費(使用多少計費多少)**

**l   搶占式實例(可以用低成本競標實例，適合短時間運算服務)**

**b. 注意所開的機器所在的地區和可用區**

**c. 選擇實例規格，可透過vCPU、RAM規格選擇實例**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjmMrVKrRKn76PYK5y0arg1abrmWifadzyqnwGfZo5eEiOOyeJ4nV7rLkktD2Vk675lvVRma3vf_-j8enSpen1BJVIsYsDgK6_CCI2W1n0SE_j68d63qtyX5S4hxde4Xl6itGkn9nOr5kLG9CKj4gjoh7-O4OUgFL2Xze1ycCyBLvMp8m9v1MqCmHJ-oX8z=w640-h322)](https://blogger.googleusercontent.com/img/a/AVvXsEjmMrVKrRKn76PYK5y0arg1abrmWifadzyqnwGfZo5eEiOOyeJ4nV7rLkktD2Vk675lvVRma3vf_-j8enSpen1BJVIsYsDgK6_CCI2W1n0SE_j68d63qtyX5S4hxde4Xl6itGkn9nOr5kLG9CKj4gjoh7-O4OUgFL2Xze1ycCyBLvMp8m9v1MqCmHJ-oX8z)

  
  

**d.  在鏡像選擇所需的作業系統，選擇硬碟規格及容量，完成後就可設定下一步的”網路與安全組”**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiXVPCNIteZJVCKIu5C63tODZxmaNkzKM-zw7SCWGc48JIEUSTA1mMGI-hDb-WUnov2fh3qJg_w0qJeLefmKt_OT6zI4uQX-66fZnN-hHEZXDYPmgchBiGmEOWb5eHw7wYp8fIeodU5OQCk1_6MlCYd4njvpI1y84c0kVG_nra_wRRL4fDEWKcQ2DwQd22M=w640-h450)](https://blogger.googleusercontent.com/img/a/AVvXsEiXVPCNIteZJVCKIu5C63tODZxmaNkzKM-zw7SCWGc48JIEUSTA1mMGI-hDb-WUnov2fh3qJg_w0qJeLefmKt_OT6zI4uQX-66fZnN-hHEZXDYPmgchBiGmEOWb5eHw7wYp8fIeodU5OQCk1_6MlCYd4njvpI1y84c0kVG_nra_wRRL4fDEWKcQ2DwQd22M)

  
  

**(4)  網路與安全組**

**1. 選擇規劃好的VPC及預計將ECS部屬的可用區**

**2. 分配公網IP可以給予外部網路連線至該主機(如需永久不變更IP則需使用彈性EIP)**

**3. 網路計費分為按流量計費及固定頻寬，並可以設定頻寬限制**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEixPu8k7wL5EYz2sFCQe48fp7iMmSMjcr6JvnsjH46ggQwedEdcT12WeFhu7MHFLfcqTgka_7_ZwX6yxUBgnl9UKpb6ML5Y7h061XEbE8LlXXVY8YTTWbcw0JwX8qfH14MdmI1NOG2bFXAxHUDu4UAu2QOBgGAcGbx-7piEhxoDUCFX2F-yLWvuO3VN3Q0e=w640-h234)](https://blogger.googleusercontent.com/img/a/AVvXsEixPu8k7wL5EYz2sFCQe48fp7iMmSMjcr6JvnsjH46ggQwedEdcT12WeFhu7MHFLfcqTgka_7_ZwX6yxUBgnl9UKpb6ML5Y7h061XEbE8LlXXVY8YTTWbcw0JwX8qfH14MdmI1NOG2bFXAxHUDu4UAu2QOBgGAcGbx-7piEhxoDUCFX2F-yLWvuO3VN3Q0e)

  
  

**(5) 選擇安全組，設定可以訪問的port，預設會配置一張網卡，可以依需求增加網路卡**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhE3ZCONXOB7j_M4JH0kAZm1n5oeJAgw66HqW-NCP6FzI0Y15qQWGCynHxT1q4xSYf6SKaa7AqXmeiAwOtN-3Hq4aiwS4_UnCn5amuc4OUkPbc05s4VYGWWQduvqM3LV_v15DqXrcrtXFWN86medRKG80-6mj9ZCiaG1y1_YtL5wsCPoHc2Ehb8wxydCvdo=w640-h242)](https://blogger.googleusercontent.com/img/a/AVvXsEhE3ZCONXOB7j_M4JH0kAZm1n5oeJAgw66HqW-NCP6FzI0Y15qQWGCynHxT1q4xSYf6SKaa7AqXmeiAwOtN-3Hq4aiwS4_UnCn5amuc4OUkPbc05s4VYGWWQduvqM3LV_v15DqXrcrtXFWN86medRKG80-6mj9ZCiaG1y1_YtL5wsCPoHc2Ehb8wxydCvdo)

  
  

**(6) 系統配置**

**a.選擇設定登入密碼或SSH Key Pair或創建後再設置**

**b.可選擇設定host名稱**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiGBlMcnLK3CPEeN7vOhSrdtmMlbhbmNipQ5huZ8JMnpwGu3ffMO_7O5DNlHmha9uLg9hmmFx-sNGnCR-a8EhdqiT2gQfLA3HKS-4HunM-LNxe4DwO4cDRpFDDM4FB8OxfXwv3aNGLLUErFQyYEpl2D6tUVJsr7SgN3XIo68MVQ_J0tncIMGlv_dzDBp76t=w640-h220)](https://blogger.googleusercontent.com/img/a/AVvXsEiGBlMcnLK3CPEeN7vOhSrdtmMlbhbmNipQ5huZ8JMnpwGu3ffMO_7O5DNlHmha9uLg9hmmFx-sNGnCR-a8EhdqiT2gQfLA3HKS-4HunM-LNxe4DwO4cDRpFDDM4FB8OxfXwv3aNGLLUErFQyYEpl2D6tUVJsr7SgN3XIo68MVQ_J0tncIMGlv_dzDBp76t)

  
  

**(7) 分組設置可以為ECS配置標籤(Key:Value)在資源分類及管理成本、自動化管理應用上**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgSA8-OAz5p7q8C1V44I053s6grOMNTCKiRyHtIWfj1LCVUwCXTq4sbzW2GejcNiBtS-AwaHRS0Xp3N7E_Lorjk7SEoX2j4Z_2zLHaUSxR56KHkiz7hRV317Bf4rKmSTtcP9SFVnhl0ttfED7jsBEkt_XMEmG_fRxZbU3ODt0FXg_60Ha39E_l-OMODd0YV=w640-h142)](https://blogger.googleusercontent.com/img/a/AVvXsEgSA8-OAz5p7q8C1V44I053s6grOMNTCKiRyHtIWfj1LCVUwCXTq4sbzW2GejcNiBtS-AwaHRS0Xp3N7E_Lorjk7SEoX2j4Z_2zLHaUSxR56KHkiz7hRV317Bf4rKmSTtcP9SFVnhl0ttfED7jsBEkt_XMEmG_fRxZbU3ODt0FXg_60Ha39E_l-OMODd0YV)

  
  

**(8) 設定完成後，可從右方欄位檢視完整的設定內容，確認好後就可點選”確認下單”(須先完成付款方式綁定，才可正常下單****)**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg9RYAzR8zCAA5zptOmKqfrXtFbjiNN5ed511TUuMgnf7qSYhg4C1ZqsZv4gP2RnU7CtWltOcfPA26BiOZZhcbOOxZ-px4Ee2qKZlmo4cBeyS0nWI8L6vWFVSdty4-ziVbwkQy9xyXZjL-ez5xdRDq0hZy25aWD70m_VBOrJaltkB800Qu0aTAbQMdM9-qM=w640-h510)](https://blogger.googleusercontent.com/img/a/AVvXsEg9RYAzR8zCAA5zptOmKqfrXtFbjiNN5ed511TUuMgnf7qSYhg4C1ZqsZv4gP2RnU7CtWltOcfPA26BiOZZhcbOOxZ-px4Ee2qKZlmo4cBeyS0nWI8L6vWFVSdty4-ziVbwkQy9xyXZjL-ez5xdRDq0hZy25aWD70m_VBOrJaltkB800Qu0aTAbQMdM9-qM)

  
  

**(9)下單完成後，就可在實例列表看到建立好的主機**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhG0TijS1QlvROZH_n7mY9byrnbEOV5jjlz3AWKnPgdJD6WQ4rNWj-6Tm4h04kDEPPvxaau6J8dStCc5eNjZZ9fx_yhk80eZVmQyXdtbrJ-ckK9R4WtRkzyQXOR8hveAWM-nycqnAiD0cDo8hBcaLk66Cgs1NoOXJMBYibQNGxyLeghGcGJ0AOjMWFM2aRq=w640-h220)](https://blogger.googleusercontent.com/img/a/AVvXsEhG0TijS1QlvROZH_n7mY9byrnbEOV5jjlz3AWKnPgdJD6WQ4rNWj-6Tm4h04kDEPPvxaau6J8dStCc5eNjZZ9fx_yhk80eZVmQyXdtbrJ-ckK9R4WtRkzyQXOR8hveAWM-nycqnAiD0cDo8hBcaLk66Cgs1NoOXJMBYibQNGxyLeghGcGJ0AOjMWFM2aRq)

  
  