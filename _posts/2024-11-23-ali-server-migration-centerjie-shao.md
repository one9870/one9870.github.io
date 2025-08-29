---
title: "Ali Server Migration Center介紹"
date: 2024-11-23 12:40:00
categories: ["阿里雲", "阿里雲教學30天上手"]
tags: ["阿里雲", "阿里雲教學30天上手"]
permalink: /posts/ali-server-migration-centerjie-shao/
---
伺服器遷移中心（Server Migration Center，簡稱SMC）並支援P2C(實體到雲)/V2C(虛擬到雲)/C2C(雲到雲)等遷移模式，是阿里雲提供給的遷移平台。

[![](/assets/images/01-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQOcBxWsvX998uLo3Hd6x20Cy-PC_AOnXhRzduR2mIj7iyksIeNv6SzTpjRJQangj30xc_aYNryOeykoJ-OSsbAZnBbI6U3LCZHo4EMwdV1Hu-mmIiXu2D6hHMkyEWRxXF3kzU_e8kboT-J0zZm0v7omKUGi9RaUVPY09_fBmcZOTj73crKVdKOg5ols_v/s1340/01.png)

  
  

應用場景

1.    
伺服器遷移:

透過有遷移方式，將來源伺服器從實體機、其他雲端伺服器平台遷移至阿里雲平台。

2.    
作業系統遷移:

雲端伺服器作業系統如CentOS 7/8、Windows Server 2008/2012等遷移升級到新的作業系統版本，以保障更長的作業系統維護週期。

3.    
跨可用區域遷移:

ECS雲端伺服器遷移到同地域的不同可用區，提高阿里雲內ECS雲端伺服器遷移效率。

[![](/assets/images/6-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFeidQ7iKtEY6tH6cAgCVvmzb2yrx73Khuoca5L0aU_5Ypt-NzerLBv2kWreewujrVHSHE3SOL60uQr1WM5B-MtkGwjcpbkiOSw2uYMlhBsGVgUn7Di2lCAB_nSkH20ywAGvFOMIr5CgqdBrVx-hpE6uzjjtOMoUc4xhDJE3iEk9qwZEiB7WWsH_qYDsAR/s1557/6.png)

  

以下遷移配置過程，下圖所示:

遷移來源類型:

[![](/assets/images/8.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjrKh33DDvrisWxIf1R10RYhmx8tkNuSpXyxw5ge4Ij3BnHUvlvFCXaoR98qRi-BfFvkcZDc2cdPwr5cScldE24JbkCiSuch36kUOs0opncnStQEcQd1UXbbZdPc2_a6kXs_728eIOa9XqPBBXjt9rQMxc2mGK8-LkQenjVFm_bUO9tWKs7QR0nknash1Cq/s913/8.png)

  
  

1. 在控制台找到服務器遷移中心SMC->遷移源->導入遷移源

[![](/assets/images/7.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEia_5XBfbJN1qDvE185ccJjrLC6hoy0ZrO2GDHy2l-RaC0zM6pgzCRm-Qq3hjGdcO8ni0pH4Cc9sCxhr5hyFkYz4QkpEOCHgOKwbnli-9N9T8cwA5OevwwxP0bh1xYvWqPRLBPE3FhaP4pgZEeZmgoDcGonpzj_kG879SsVsN5Hc65V4BAm8UuhbeDc5YoR/s554/7.png)

  

2.配置我們來源伺服器相關設定(儲存完等待來源導入完成)

[![](/assets/images/02-2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhb7H3M9twnJiAOtIjVmYSrPqvlCteGLBy5ts1NcLsLtDpeCVDb3orFb7xdyGF5PBxUpeaKLgZrfNd_NFRfX5ExrjMg9kP6zD6xJIlLGG5-RpRi0J8mSUJeJQuQ1BV0h-_or9MG4bNiPXdLYDPhmIvKVTnIwt1wLDtUvfWentTY5gxhQrP2cqQqS_9a2bAc/s1173/02.png)

  
  

3.創建工作組->選擇遷移源(配置遷移源ID)

[![](/assets/images/3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgc9yMxf-piSAJ51UHwocJa60rqZ8Xbm3hkcEqp83NI8E-7DMVtrPlIcuI-4ZFjtqcSM2s14tj_UW8oRLWZCTvnNB_6-K4s1kTYbqYhHTEDYy2qf_vR1XrXLmjDk8Ct092aB_8laCm5NoZAr3iWF8-1stdmzzFHpiYKbLUPBXuhTy5Zp7g1U0Ndmelusyf2/s1122/3.png)

  
  

4.等待遷移源(狀態:進行中)

[![](/assets/images/4-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnPUYzDyKA8IBot1T36Jgk3g67v-jC1WoK4eY024QrfJlAXPpAnKAva2eTrnmeiObz_DTljA8jIhbwU2JK6V5Svdz-l0MXoqkXV-oqKALMb-JH3dC_0Hp1tgOIeG6_kkSusxAoAgt4pdrJwvIYHzM9VPlB5c2i_4SO8BlVA_VFe2NkWUuGzGcS_wTJmM8X/s1171/4.png)

  
  

5.完成遷移

[![](/assets/images/5-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjkdxKSPV8R2PzGn6GxzXawDf6rAnLvONmIUGM8C30BN5k25ISSa99qvlYOOLaiy7wvXw_kqcn8Uil4pQKbHsNDTozqpaU0IYbSlrHKcEh9ObvKMgiNQaJHz8hyphenhyphenOgi5lA8PFiuQw07ZHWTJMZK50QGCvk96pJKeK_wCMBT6XK4HnJX1aiyWo2hrChYfH0aW/s1098/5.png)

  
  
  
  