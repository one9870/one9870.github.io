---
title: "GCP使用標籤功能控管成本"
date: 2024-09-17 01:55:00
categories: ["GCP"]
tags: ["GCP", "標籤", "成本", "控管"]
permalink: /posts/gcp-label-cost-control/
---
## GCP使用標籤功能控管成本

在Compute Engine下列表中點選左側VM執行列表，勾選要標註的機器

[![](/assets/images/標籤1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8dlama25rYCvihO5PC5CcFgFQtGw46mtjXjc0tCTQNR_DCwjGhyphenhyphenW4u3D0uOQOSJT6VXsZEnEjyqssLZDYBbw2nMmSwo7_tFV1lG8hL0B0jOWkIYopB9aRb4bZ16-Q3HCVL7X8ukziQ5dWBeJbL5zWPTG4Ar6ix0iSghGFYW0oKIbLrGhIQdWOKIixo_E/s1556/%E6%A8%99%E7%B1%A41.jpg)

  

標籤
>>> 新增標籤

[![](/assets/images/標籤2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg20JdH3vtjwTR-0yOLu7vXNAVHTWdAbc0OsdzW7ul3kfgWXnBtfxDKC345LkqgldWMi9L_ujOdBRBzpiXM6sV8cgV2-OkuMPRkOzPayiDZAlaGFtc5BUCblplzSZOXrrngWCi1mL58t10eNKD0Dk207ISNO5m6Fm3r-jd5rEGZYcNfO41YBRjiYViPW7Q/s1522/%E6%A8%99%E7%B1%A42.png)

  

[![](/assets/images/標籤3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjGL0nIOBZAzWpPw_zPwtfCMShw7dI49WiqxJiwJnYesqblVncrQt28KZuICGMUuP0bavv8f8533deLQHJPGJYI3iqNlSaHqyxnD8VjmIZnh1IKJVXPakxjPp1v5YYEeS0avmabVnFIbtEmR9ZnYm4zCRiZolAx42w7faABvhDlYfqE8fZ7G9HP8w_Dm-o/s1597/%E6%A8%99%E7%B1%A43.png)

  

鍵1欄位輸入”ap”，值1欄位輸入”vm01”後點選儲存。

[![](/assets/images/標籤4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiv9lPmV6cEacxeTd0SZfV5pKiEmuaer1RBl4YOxLXcz3jOdhJJfzVdF6krHxEu037l7CwlFx0kkgCCcNmBlpX-pVkV7lpNDKS5N1o_A2V6agJmjKCxgmviFD6Su2SnfrA6WxtRGAZICiAhLO0IIENnFH-AgU4AGG0XAwQPO4jYpwcCnAFmObVc2nGOvuo/s1592/%E6%A8%99%E7%B1%A44.png)

  

因為key-value的方式鍵入，以上述的鍵入方式我們成功地給執行個體上加上了標籤與群組(如下圖 ap:vm01;ap:vm02 )

//可以在旁勾選是否顯示標籤

//請注意只能使用連字號 (-)、底線 (\_)、小寫字元、數字和國際字元

//VM 執行個體只包含到CPU 和 RAM 的費用，要完整的紀錄vm費用，需要在DISK(磁碟)也加上標籤，操作方式與VM 執行個體標籤類似。

[![](/assets/images/標籤5.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSvv7V0DhTxiRsGR_yH-RIiUbsab7XcWxTmsh67w-k9qQKNpv3oxDvEGAX5J1lL3F3-8sUONNf-LZlE8fCoTEuyCY32iHIETbolr97WJxcU0iBWnvHNKaa06Dif3_sbD3FKObdvAmN6-wi3xBpf4pFswrhqxqs8-jb3zwEndyfbpu7_a_ykRDkU3Rg9oI/s1591/%E6%A8%99%E7%B1%A45.png)

  

[![](/assets/images/標籤6(VM標籤).png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIvllrHpieHmnUBMgTlC8-HD7M5PUqztzKCmsrDGWd9qJjwmyGSQJCiLTwXZtztDjnE79OaHA0WlfyqW3hthi1m4Q0MuRw41kzZ6IxTWjp2PIF7mcApGle6Aii6EknqyzBe19z9Gp93Hl0slWVPjC306YSgUD80wlY2V6HCTQDEip7SuplKuvokHRbVgA/s1599/%E6%A8%99%E7%B1%A46(VM%E6%A8%99%E7%B1%A4).png)

  

標籤設定完畢會變成以下顯示

·        
VM1：**ap:vm01**

·        
VM2：**ap:vm02**

·        
DISK1：**ap:vm01-hdd1**

·        
DISK2：**ap:vm02-hdd2**

 

[![](/assets/images/標籤7(磁碟標籤).png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjE63ycoBtMDiNeoSSnrdYfGUTd1-DFMKbPPOO226wp6wnCVKkNhMmLYfRF3tcUtGQvf1WaSQjceYgoDjpRMt8q-AkiUzMOnjKPhsB86dMyp-8aLM85qcG59RSk4zY7G6_apvNjXjhLovptOOBSE1DF4cr3iK8L6oV4RGrPx2N5Yh2uRuKcqoWgk5MpJAY/s1599/%E6%A8%99%E7%B1%A47(%E7%A3%81%E7%A2%9F%E6%A8%99%E7%B1%A4).png)

  

[![](/assets/images/標籤6(VM標籤)-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-kcjN7qwSqSUYUja_jbjTV1T5sF_L1RlANuEbRSSKHMMHBBe9foAoXdrLe7-jKCO5d4bf2ClRHfRMeOcUQoP_JIEL65fcOTd6txmjUS9cuI14SwxNy_hyphenhyphen-rfSC9Qb80oiHP8lk9oaoOcFHh_wjsvVd1MsbQXEtkq7NKuW35gqFYHhmJNoWydQeEtEJGQ/s1599/%E6%A8%99%E7%B1%A46(VM%E6%A8%99%E7%B1%A4).png)

  

設定帳單匯出功能

//目前只有BigQuery才能看到依標籤記錄的費用

帳單 >>> 帳單匯出功能 >>> **使用費用詳細資料**(編輯設定)

[![](/assets/images/帳單1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisjJw7QRTkNekX4tU79pzpefnoDu6wVuXwSmjbkxXChn6ytzlLXMzCR42jHeIxBlte6niSX1PBBXYzzm6vQeFlY142JSOFINXJnKxjNPbcWtuwHRON5CjRER7mjVjvQQRtyBYCabf76387DxUwZ342vxPB8yJf3Y6toWEYO90egi9ugNCKOf2UX6C29nM/s1306/%E5%B8%B3%E5%96%AE1.png)

  

[![](/assets/images/帳單2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgO4QJjAu9CkxYdXAEi_vPyKCtfV5euMs0I-r3MtyXBTQKG1hfkG0Qgu9pUqZ4Qj8Jt_FhORwKmyhTOrrxH1hdL6L8h88szYocAIjwly8hOOsgIitC8ecsqbz43Fw4TrfFVpEqPL2sWl3r3pl6e_v1LTRpdyrYbB4SnZDiQQ6Wfu0RVI40KiSnHJKcIvqU/s1277/%E5%B8%B3%E5%96%AE2.png)

指定BigQuery的DataSet，就可以儲存了。

設定完畢，即可在右側的報表選擇篩選器，從分類依據即可查看設定好的標籤(ap)

 

[![](/assets/images/收尾2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5mN-q0XdwMi_p2RTxCGf-6e7theFUTTV8K-Blwji4PBC2oACR5kLATGlXLtRsTl2aSaj2J3YRq3o5ej_b17rsLAx5xsepGhqbHITW7eAeqRS12XllWZw4ayru77lioz88d5-mh2aD5auSX9PkTqFKiw1mNvCU29UjMnbwr9tOFcfaNlkVB-pREkxgGX4/s974/%E6%94%B6%E5%B0%BE2.jpg)

  

[![](/assets/images/收尾1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUmaffiSg1hnllmeDbvQqhLF76buYVZhXN1n9opxBWDVjCEIDTgsQgnoXbol4bhxEmkkoQGxXIhNOQ-Gs2KmggKFbTUGLYvQ9a_8ia1CKPqd6DHrxcJV7Joaq9mNIeHpk2ctkv_MFrJfgRaeXKxIjT6OzUJN9c3xfvjlc8A5fFVUf6f0YPfGGxplDPlXc/s1598/%E6%94%B6%E5%B0%BE1.png)

參考資料: <https://blog.cloud-ace.tw/google-cloud-platform/pricing/how-to-get-cost-of-each-vm-use-label/>