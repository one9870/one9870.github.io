---
title: "阿里雲－CDN建置"
date: 2024-11-16 15:10:00
categories: ["阿里雲", "阿里雲Alibaba Cloud", "阿里雲教學30天上手"]
tags: ["阿里雲", "阿里雲Alibaba Cloud", "阿里雲教學30天上手"]
permalink: /posts/a-li-yun-cdnjian-zhi/
---
**阿里雲CDN**

**什麼是阿里雲CDN**

阿里雲內容分發網路CDN（Content Delivery Network）是建立並覆蓋在承載網之上，由遍布全球的邊緣節點伺服器群組成的分布式網路。阿里雲CDN能分擔來源站點壓力，避免網路擁塞，確保在不同地區、不同情境下加速網站內容的分發，提高資源訪問速度。

**CDN架構示意圖**

[![](/assets/images/download_device_resize_jpg_v2.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgilrKeiEOzKFYBh8PNQfUd3i3e7ahO1-WC3gakECf-yYYccrAaMynoMHE2-ebbIg5W70EcW0eVe1DGHGTqj13VKCMEQWpZkubdqmN3oOV5GkKQl2vVNRmL4Dmf7v3BfSLCIEtn1Lw-0UkhCvi3rkzhNZ83SKlaA4EUk1u7o_UfvmqfE6EgIGn1enmaJhQ/s1000/download_device_resize_jpg_v2.jpeg)

**CDN建置步驟**

1.於阿里雲點選或查找CDN

[![](/assets/images/001.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgawQs_6ZQPFvTnonAdZhSUm8TQ-OdURv3JeNjOJeBtRIWGtGvYd_bnplSaeGAqlZMayEl6L6NsG3ZTL3V3RexgluZTPOHtggx_hZIP8ynAj0v5zDLVHiaAyLTgHrJ0AV00zngTCwsMYERPeHq3nFvLoFZ2pyiz8bBAfn36VBZ9FzehqI6Kx2vDrvvQIME/s729/001.png)

2.選擇CDN服務→域名管理→添加域名  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhFagoJmf-fsvaHuwhkUaa6CXVsidhnRI1F_niSpc503kFR93ylR_0Aohu6FNGXW0EZfX835kNb6ORYFxpDb0r1WxMM2efjhRq-8NG9t1A8zLf9N5sNdxHaRtw0nwbQaWpDaxW9Ji8aJ1S77igvQki24TnVSpVSxSGcXALUfeKvmbopDMdUkon38pYiKtg=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEhFagoJmf-fsvaHuwhkUaa6CXVsidhnRI1F_niSpc503kFR93ylR_0Aohu6FNGXW0EZfX835kNb6ORYFxpDb0r1WxMM2efjhRq-8NG9t1A8zLf9N5sNdxHaRtw0nwbQaWpDaxW9Ji8aJ1S77igvQki24TnVSpVSxSGcXALUfeKvmbopDMdUkon38pYiKtg)

3.填寫想**創建的域名**，**選擇區域**(備註:若要在中國境內使用CDN，需要準備ICP備案，並且源站資訊也需要填寫)及**業務類型**

[![](/assets/images/003.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg46fcOXvdxRkTRS66SwZnSr-tvVQuaNSP6yiqLgRLafoQv8zDvDzcUh9xkuD0WAOVvQ8rC7vxpm1jjGvTPsSywpTibraEHnst4nKIHfwoDLIStSW8RakanYOAIhSe0sWjwCGkQiT3Z39OJHSdyrzr4xPmKrgccGHEXu8rnaitt-zHmzop7FYAIjXNkjIE/s786/003.jpg)

4.點選新增源站信息

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhhERe_6y3k9DygnbHGNyAQNDqx_mFRRhn5kqP9VdBcdpeX-_vEJMM2Q7fmuPR-j87PTrBeMpSCZv8dn56q7oXapPrE2FDuIbfSQs6lamr6zDJU3kQ0TFbVJDtHq0XLXB31cqh4ySkwj42sxXI213kD5kAZRrIdnQSVzQX_AMEIyB0eu1aRE6Y8gI8I-Fw=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEhhERe_6y3k9DygnbHGNyAQNDqx_mFRRhn5kqP9VdBcdpeX-_vEJMM2Q7fmuPR-j87PTrBeMpSCZv8dn56q7oXapPrE2FDuIbfSQs6lamr6zDJU3kQ0TFbVJDtHq0XLXB31cqh4ySkwj42sxXI213kD5kAZRrIdnQSVzQX_AMEIyB0eu1aRE6Y8gI8I-Fw)

5.依照業務需求填寫源站資訊

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhTK98rIgTaA36U0xwuP-v6jl8y1QZWIwGvtrGSU-W4jKCvVilkhuxK_yQmDOK-s-DO8H_MyIQCb0AGyzerGJNiWgkBHT3IBZnKsBYjqc8BX-FISgvYKQsyX-ri-TofE4vvA11eqY18xhbzxe5nxEgGyy-kcOtV-xKZAfTbHvqs-95FcuJUBDFlmyPE41c=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEhTK98rIgTaA36U0xwuP-v6jl8y1QZWIwGvtrGSU-W4jKCvVilkhuxK_yQmDOK-s-DO8H_MyIQCb0AGyzerGJNiWgkBHT3IBZnKsBYjqc8BX-FISgvYKQsyX-ri-TofE4vvA11eqY18xhbzxe5nxEgGyy-kcOtV-xKZAfTbHvqs-95FcuJUBDFlmyPE41c)

6.完成後將CDN的cname地址解析到 DNS cname紀錄  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg3SOA72sYrjHz9gQls4UORYoHFa9yf7_TT1gWHEMXniJUUPUPSqoawlA4u-IpArud8HDvcQda4tkSHr3LCVUSJUQnT2AC4aWNyueiGLsHKahkfBANfqCiWGRvDrYQeWIHUAXY4EmYcGVQ-EP55cBWbTFED35tGaVqYThhYx2xXv-NVc6jqsKKaWL2VPzQ=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEg3SOA72sYrjHz9gQls4UORYoHFa9yf7_TT1gWHEMXniJUUPUPSqoawlA4u-IpArud8HDvcQda4tkSHr3LCVUSJUQnT2AC4aWNyueiGLsHKahkfBANfqCiWGRvDrYQeWIHUAXY4EmYcGVQ-EP55cBWbTFED35tGaVqYThhYx2xXv-NVc6jqsKKaWL2VPzQ)

7.完成CDN配置後點選管理選單，可進行設定調整

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiwKbeIKLS5YizvaoroO0XDWXe1cp0e9BNnHu7i_hNViIpdSs8S3Z-C5j9zwmjK3hTlsQ6CUeL9_NLXWnHPFjn-6RIEbS6qaL_dv5wILuLmUpyB00YsGc5boM_ngvHql7oPG6ib-mb-ecfBKNDK9gy6HaM_9zYwdtS9T3NBzVnuUNCztswim1VydmraQ0E=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEiwKbeIKLS5YizvaoroO0XDWXe1cp0e9BNnHu7i_hNViIpdSs8S3Z-C5j9zwmjK3hTlsQ6CUeL9_NLXWnHPFjn-6RIEbS6qaL_dv5wILuLmUpyB00YsGc5boM_ngvHql7oPG6ib-mb-ecfBKNDK9gy6HaM_9zYwdtS9T3NBzVnuUNCztswim1VydmraQ0E)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgnmkaDIgz4HBhoLFO6J-bh_NKYaxUUR446M2yD5hJsmQBOBrk_Zd0DtidzAyDGcPMllSGdUDeq6uYTt9IEbYKEjhkJJC8-hfpcx_4mA__FID8sCkNdvz83bjCrCFBXaDvr04V68ESMr5KPH0fRUVQD2nMRD6ay4-TwcIZ5VQ0soLzVfRv6gO8dHv8Em44=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEgnmkaDIgz4HBhoLFO6J-bh_NKYaxUUR446M2yD5hJsmQBOBrk_Zd0DtidzAyDGcPMllSGdUDeq6uYTt9IEbYKEjhkJJC8-hfpcx_4mA__FID8sCkNdvz83bjCrCFBXaDvr04V68ESMr5KPH0fRUVQD2nMRD6ay4-TwcIZ5VQ0soLzVfRv6gO8dHv8Em44)

8.使用nslookup，回傳阿里雲的CDN cname域名及CDN結點IP，確認設定無誤