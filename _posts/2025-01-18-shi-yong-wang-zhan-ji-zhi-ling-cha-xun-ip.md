---
title: "使用網站及指令查詢IP"
date: 2025-01-18 18:39:00
categories: ["指令", "網路工具", "網路相關 Network technology"]
tags: ["指令", "網路工具", "網路相關 Network technology"]
permalink: /posts/shi-yong-wang-zhan-ji-zhi-ling-cha-xun-ip/
---
 

**若你想知道你連上的網路對外是哪一個IP(公網IP)，只需去搜尋IP查詢的網站即可得知。**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEim_8RJ55Gxvg2CY4K4cZKLtgvL6gMKzjpuQRsMJ3A26w-691u2k6IKPVsJqsULPkIn2rRAEOvTFx2wvCgGwp4XuiNlPpSXPhbzK-R4_8dYMBfBVvNC2_tlQO_G5CtAq8-4O-aNtuZEw4ODm0Emt8rfdUJwSE5RSWGcFNLaaSEPP2Qmt7rFiOnCUenFX_A=w625-h262)](https://blogger.googleusercontent.com/img/a/AVvXsEim_8RJ55Gxvg2CY4K4cZKLtgvL6gMKzjpuQRsMJ3A26w-691u2k6IKPVsJqsULPkIn2rRAEOvTFx2wvCgGwp4XuiNlPpSXPhbzK-R4_8dYMBfBVvNC2_tlQO_G5CtAq8-4O-aNtuZEw4ODm0Emt8rfdUJwSE5RSWGcFNLaaSEPP2Qmt7rFiOnCUenFX_A)

  

 

**然而因為IPv4的公有IP量不夠分配給每一個主機，所以大部分會讓主機再分配到一個私有IP，這時候就可以使用在終端使用ipconfig指令查詢到私有IP**

**1.****先按Windows鍵+R 輸入 cmd**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiyOVGU_aZLfAORIXNdslkyY3VAihiLdEzc5Cd6FAwju0C6dzE-yFRI40pvoEWmgJJpvXVsFPdgX11pL8G2-QPYnOkxjbQTNYZd6Nt4skO1ARXUxJF6Hun2kcB-ULiSDKkNT60Jsud_-9-dZZI35HDv3QxTCuFCqBzrVxroOFB3IQRX7Mr1AujoC2pIJJo=w507-h250)](https://blogger.googleusercontent.com/img/a/AVvXsEiyOVGU_aZLfAORIXNdslkyY3VAihiLdEzc5Cd6FAwju0C6dzE-yFRI40pvoEWmgJJpvXVsFPdgX11pL8G2-QPYnOkxjbQTNYZd6Nt4skO1ARXUxJF6Hun2kcB-ULiSDKkNT60Jsud_-9-dZZI35HDv3QxTCuFCqBzrVxroOFB3IQRX7Mr1AujoC2pIJJo)

  

**2.****在終端輸入ipconfig即可得到私網IP**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh0jFmOKevBzlqe7U0RVeEIzjGjJpGyulhPpNvpDS0TKsEbJGeDgOVWv5KJrk1U1dY5JYXz1sx9HZ1X9aJotauORq2uzjH4wlRMTC6Pb45iIK2VWaxd6PeOWMUIJyO8yFKWPaAeFY9rZs_gQdYDe6FoAdH1JrjywA7Zs7qXmHSxOrXW4ctAYvCYP4CfNvQ=w608-h353)](https://blogger.googleusercontent.com/img/a/AVvXsEh0jFmOKevBzlqe7U0RVeEIzjGjJpGyulhPpNvpDS0TKsEbJGeDgOVWv5KJrk1U1dY5JYXz1sx9HZ1X9aJotauORq2uzjH4wlRMTC6Pb45iIK2VWaxd6PeOWMUIJyO8yFKWPaAeFY9rZs_gQdYDe6FoAdH1JrjywA7Zs7qXmHSxOrXW4ctAYvCYP4CfNvQ)

 

**想要查詢某個網站的伺服器IP(以<http://smokeping.asuscomm.com/>為例)，則可以在終端輸入指令nslookup + 網域**

**1.****先按Windows鍵+R 輸入 cmd**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEghXw_9euJBWvQQgoChiC3luDV2ja-LdV1M5Akq9rV6wdXu1yKST-XEpmF6K5Lx4lOnqy3Yj2AeXn2eZ6HaQgHqjh7Syp6LwNEei31JcSftq2s4VA4neDaPpvDfzf5xKxwoPQsAx_Mjyn_lLGxF7xkoUjWk3ABKkhaOslsLFI-GHHZKtQHA1gEElaFFa0g=w461-h228)](https://blogger.googleusercontent.com/img/a/AVvXsEghXw_9euJBWvQQgoChiC3luDV2ja-LdV1M5Akq9rV6wdXu1yKST-XEpmF6K5Lx4lOnqy3Yj2AeXn2eZ6HaQgHqjh7Syp6LwNEei31JcSftq2s4VA4neDaPpvDfzf5xKxwoPQsAx_Mjyn_lLGxF7xkoUjWk3ABKkhaOslsLFI-GHHZKtQHA1gEElaFFa0g)

  

**2.****在終端輸入nslookup + 指定網域即可得到該網域之IP**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjz9XIuZYs5vpPFTqakzdFKV-gXDbJlyt5u7_RnXHV-KDMGEKX7oUDTHTpf4fQoisuJ0Ckk0Hhn8XeAkAcsGnjqO9SzizHgsH91MB3cgJ-tFeW1x-W1rEu9jvPcerzNf3QWLrwNhrnNdkqWZ3fJIm4w2LoKZIevWtxX6i6iU-3sRP0hUA-9VooslCi3u8o=w554-h294)](https://blogger.googleusercontent.com/img/a/AVvXsEjz9XIuZYs5vpPFTqakzdFKV-gXDbJlyt5u7_RnXHV-KDMGEKX7oUDTHTpf4fQoisuJ0Ckk0Hhn8XeAkAcsGnjqO9SzizHgsH91MB3cgJ-tFeW1x-W1rEu9jvPcerzNf3QWLrwNhrnNdkqWZ3fJIm4w2LoKZIevWtxX6i6iU-3sRP0hUA-9VooslCi3u8o)

  

**也可以使用網站工具取得**

**1.****左方輸入網域，再點擊開始測試**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgHQVvUq662fUcKYmq6TC2WKiyfAqma_U2n143TWitDWUeZdahVTJ8PIPuKiMBKnKIc1Wc5iSWNGAyl9u-FVPnrx3OqY795h26yLKYe12QnaCcYA649BW80RHU4u4Zn5_LzfPcai79m_rZzVJQr5vH7EnwY_cZ4wiWj-7tjrbpTjswRTwkxZ1TaH70zAMo=w594-h401)](https://blogger.googleusercontent.com/img/a/AVvXsEgHQVvUq662fUcKYmq6TC2WKiyfAqma_U2n143TWitDWUeZdahVTJ8PIPuKiMBKnKIc1Wc5iSWNGAyl9u-FVPnrx3OqY795h26yLKYe12QnaCcYA649BW80RHU4u4Zn5_LzfPcai79m_rZzVJQr5vH7EnwY_cZ4wiWj-7tjrbpTjswRTwkxZ1TaH70zAMo)

  

**2.****即可得到此網域IP**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiaBMh32G7fDIJVMUb4qo0KG47OQtOJpnB3C-rJNCZ8GAUuIj2M-iV0gvq6_juIq5bhYEL8zaVIiswQy1VS3xg2evKGMaAwZjUP1vtuFHYn-EOmlTSe9S_S65TtV-P1OEmSp7WpE0bEZS9_Ki4_yejTZLraV1FWQen8y722D55cPlQIyzXJJYOr_teLhUo=w578-h379)](https://blogger.googleusercontent.com/img/a/AVvXsEiaBMh32G7fDIJVMUb4qo0KG47OQtOJpnB3C-rJNCZ8GAUuIj2M-iV0gvq6_juIq5bhYEL8zaVIiswQy1VS3xg2evKGMaAwZjUP1vtuFHYn-EOmlTSe9S_S65TtV-P1OEmSp7WpE0bEZS9_Ki4_yejTZLraV1FWQen8y722D55cPlQIyzXJJYOr_teLhUo)

  