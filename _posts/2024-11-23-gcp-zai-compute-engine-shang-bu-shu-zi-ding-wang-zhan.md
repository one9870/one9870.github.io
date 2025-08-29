---
title: "GCP 在 Compute Engine 上部署自訂網站"
date: 2024-11-23 08:15:00
categories: ["GCP教學30天上手"]
tags: ["GCP教學30天上手"]
permalink: /posts/gcp-zai-compute-engine-shang-bu-shu-zi-ding-wang-zhan/
---
 

**《建立Compute Engine》**

1.      前往「Compute Engine」頁面，點選頁面頂端的「建立執行個體」

[![](/assets/images/1-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-5qVC5wh0Di2wOnjQ2FU75tUtxJhKdLUxJtckX1_VcHnznsMHnucbs2Nu3bhTUlAJq99fWLWNf5cQwZHI2oNslCeiXdaVoUhykvnG45LhVisnlO0591W_CF5tYKAb3YWojkbEfTjL_PF1Cxp_gMjvHwFnOqRtxIbimgqAV89WEg1a6hM3nf9zKhUFARPV/s1122/1.png)

2.      依業務需求選擇區域與可用區。

[![](/assets/images/2-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjy3bCD5EaRwthe5Kjf3Dg_0yHtWAUv26QDMyTeuuDzdg8Gtjs6YRNi9004674bMvqUvYVnqRQEbiqe1vvANQ_I-xklDXbcKui4eVaVKeJ3l7at7LW_OGFnF0m4vQidGmQFidWO-rudnyfXD06WQ1POQJIeBrU9Y8J4W-Dg1mgPElgy0k7LxZDA7tCf0j8Y/s1122/2.png)

3.      依業務需求選取機器類型。預設值是合理的起點，之後可視需求提高或降低機型。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEinJTkhTNd14wX3FntHlzeoncvD6yXiZZZ4KbyHsHxlkEYjZ-ewWmPi_6Y6fnbGk1oHj65pbFMYXydHXVPwFdvuZ856siXg3f5El-oSUOQ4W5pqdCxI7fNMZUl-C1Mt88WkUq4J7921o7uUlzHzvThMHr9p6egL9KChWIWiE_iJ1vHf77Pa7iAKv0dAdVK-=w598-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEinJTkhTNd14wX3FntHlzeoncvD6yXiZZZ4KbyHsHxlkEYjZ-ewWmPi_6Y6fnbGk1oHj65pbFMYXydHXVPwFdvuZ856siXg3f5El-oSUOQ4W5pqdCxI7fNMZUl-C1Mt88WkUq4J7921o7uUlzHzvThMHr9p6egL9KChWIWiE_iJ1vHf77Pa7iAKv0dAdVK-)

4.     
依照業務需求選擇開放存取權

[![](https://blogger.googleusercontent.com/img/a/AVvXsEipEqJy2FxCDCyJ6VC0cqq04ot7jpRF8mDSoyqqEdRUkdO_wjppoD8rLQXBAM7baOHu8bTOvXVmnGA_IGfpalY5nWiR_2dpO-Wo0BF8CuZ7gbrRnuE9ajH-ZS82TjeZS0kKrVw7VbNhzeCJvoWS3JakFv1xDlNY3oZSZrb2QC2u8riGsW2woEi0BqbxSPPc=w640-h277)](https://blogger.googleusercontent.com/img/a/AVvXsEipEqJy2FxCDCyJ6VC0cqq04ot7jpRF8mDSoyqqEdRUkdO_wjppoD8rLQXBAM7baOHu8bTOvXVmnGA_IGfpalY5nWiR_2dpO-Wo0BF8CuZ7gbrRnuE9ajH-ZS82TjeZS0kKrVw7VbNhzeCJvoWS3JakFv1xDlNY3oZSZrb2QC2u8riGsW2woEi0BqbxSPPc)

  

5.     
依業務場景選擇是否開放HTTP 和 HTTPS 流量及負載平衡健康檢查。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhTesZy31M3EfjmOcHUQtmkHj7-rVXO1mJ04LgL18wEhFJM-UZduRF4dwiCq5DwlwcYzyozqAcYj5Q4UqatK7XkThDj8IQhCXrhK9-ZYCvY3_h0IqqUKKgKKFyv4kN-6ej_STXtrWHv7EvaQnjfoK938psQNIVs7JM5RnjgyffjsEBUFyJ0zTFp1Fx8EzNT=w640-h170)](https://blogger.googleusercontent.com/img/a/AVvXsEhTesZy31M3EfjmOcHUQtmkHj7-rVXO1mJ04LgL18wEhFJM-UZduRF4dwiCq5DwlwcYzyozqAcYj5Q4UqatK7XkThDj8IQhCXrhK9-ZYCvY3_h0IqqUKKgKKFyv4kN-6ej_STXtrWHv7EvaQnjfoK938psQNIVs7JM5RnjgyffjsEBUFyJ0zTFp1Fx8EzNT)

  

6.     
另可依需求設定其他進階選項

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhDpJcwQMpEbI3HeAjYUWAhXhzo8esSxbRyC5PjbXhu1wKdd7lpEBEwBPjMco1iJgGwTnXyS8kcp6ghTydrslbzvnQVcr0ua6K71OsqIb6GWY7V7yRFXqyTBnv8W6j4KDGrz1x0wYvDf1cgJSlDkqKNikKMe0_ocnnHQx_4-jf9T3Nvw8SF1Ax7Ryh2V5-Z=w400-h338)](https://blogger.googleusercontent.com/img/a/AVvXsEhDpJcwQMpEbI3HeAjYUWAhXhzo8esSxbRyC5PjbXhu1wKdd7lpEBEwBPjMco1iJgGwTnXyS8kcp6ghTydrslbzvnQVcr0ua6K71OsqIb6GWY7V7yRFXqyTBnv8W6j4KDGrz1x0wYvDf1cgJSlDkqKNikKMe0_ocnnHQx_4-jf9T3Nvw8SF1Ax7Ryh2V5-Z)

  

7.     
以上設定完成後按
[建立]。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg1y87-1bU5DySVh3W-KDJxDr8QAAvfxuh8QKbqYMg4cX47O5TnV0paDps0QQ2N-8ueKi4m7KL_owYqwCmOGxdtV2ssuLgmXfN08eKZSZB7n00ksrvXsH5qn5E0By2UPWYMZE-C3Df6fBkh9VnyYdk89i655ggiUygwlhzrzi1E6-EWuqtffdiJe4SlO7Lr=w378-h92)](https://blogger.googleusercontent.com/img/a/AVvXsEg1y87-1bU5DySVh3W-KDJxDr8QAAvfxuh8QKbqYMg4cX47O5TnV0paDps0QQ2N-8ueKi4m7KL_owYqwCmOGxdtV2ssuLgmXfN08eKZSZB7n00ksrvXsH5qn5E0By2UPWYMZE-C3Df6fBkh9VnyYdk89i655ggiUygwlhzrzi1E6-EWuqtffdiJe4SlO7Lr)

  

8.     
VM建立完成

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjRS43ffY40PeP9HSLtfZ6cjuB513Wsr1seng6HojBvQnUyrlsq_b_LNVxVE12qQpHaXd0clniuXBnVsdKGZevXzP4fJIQcMVweYHILrMRepoECiTsCmnyxRVdIwnek6vS88DTibbd53uPACvrMuie3AygykwTFEHgtatsS1id63H8Qk_vqEuUSelVBjk0l=w859-h206)](https://blogger.googleusercontent.com/img/a/AVvXsEjRS43ffY40PeP9HSLtfZ6cjuB513Wsr1seng6HojBvQnUyrlsq_b_LNVxVE12qQpHaXd0clniuXBnVsdKGZevXzP4fJIQcMVweYHILrMRepoECiTsCmnyxRVdIwnek6vS88DTibbd53uPACvrMuie3AygykwTFEHgtatsS1id63H8Qk_vqEuUSelVBjk0l)

  
  

 

**《開啟及管理網站》**

1.     
在 Compute Engine 總覽頁面的「連線」欄中，點選 SSH 按鈕，選擇要連線至虛擬機器的方式、或安裝所選的網站代管框架和工具。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEivxzrJ9pWeRBJYMgjHncHw7QQ_JIqgWoAq68Wq3rL_Ph3Xalo11lBnx01guVpolnPvcHaiwIsmTFMvcskrrzgIHrqMfD8tyVmaYRFpvGtSX93dZts3yMwqw16gniXG4A-tuvJ6W_GPi2Ffb75fJ0lZ_lJKFMog1Whc8shvXP3jORnTNmLWcpzHF0AgDiR2=w858-h288)](https://blogger.googleusercontent.com/img/a/AVvXsEivxzrJ9pWeRBJYMgjHncHw7QQ_JIqgWoAq68Wq3rL_Ph3Xalo11lBnx01guVpolnPvcHaiwIsmTFMvcskrrzgIHrqMfD8tyVmaYRFpvGtSX93dZts3yMwqw16gniXG4A-tuvJ6W_GPi2Ffb75fJ0lZ_lJKFMog1Whc8shvXP3jORnTNmLWcpzHF0AgDiR2)

  

    這邊選擇“瀏覽器開啟”

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg-vuUKERIfoP_HdHcxx3JYjgClGNu5Qa7Jf4EEV6DoG5vyGDMu_fMSuB8xYOOqVZCqzPlvQOAjuxPnvRfJt_lYLIWDjYWsha32WckM3VYNvhUrlbYLbD-Lz-A7tLgna3vtXOfuaV0syOtgWns-Z02uzdK5cgcMDEbJPl-yHYUqahSuCbAQTqwG8mxcVFWW=w640-h460)](https://blogger.googleusercontent.com/img/a/AVvXsEg-vuUKERIfoP_HdHcxx3JYjgClGNu5Qa7Jf4EEV6DoG5vyGDMu_fMSuB8xYOOqVZCqzPlvQOAjuxPnvRfJt_lYLIWDjYWsha32WckM3VYNvhUrlbYLbD-Lz-A7tLgna3vtXOfuaV0syOtgWns-Z02uzdK5cgcMDEbJPl-yHYUqahSuCbAQTqwG8mxcVFWW)

  

2.     
連線成功

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiQCP0Rz3C_cHzCKiOqSdjonY80-WZ71PmwDr0FEC4Ja4ku3bVbbCyB6qiQeRsTR5kHGw6YoH1EV1bL59eRDQYGEIg3NyoXcn1KY0QZbH8Crz7tsHydFjL1xmChJU7pl17AGuGA9fY4_qTwCfF2X0pf7aWCc6J3pYxpu7wznfTM1p3ae7O_1NACvjUhjDRh=w860-h275)](https://blogger.googleusercontent.com/img/a/AVvXsEiQCP0Rz3C_cHzCKiOqSdjonY80-WZ71PmwDr0FEC4Ja4ku3bVbbCyB6qiQeRsTR5kHGw6YoH1EV1bL59eRDQYGEIg3NyoXcn1KY0QZbH8Crz7tsHydFjL1xmChJU7pl17AGuGA9fY4_qTwCfF2X0pf7aWCc6J3pYxpu7wznfTM1p3ae7O_1NACvjUhjDRh)

  

3.     
確認VM的外部IP

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjsDjWDiI9JiGx2KX12nPkNxQgiMiwKWfMpamRUml1fnmjdd_h9Eq3TiRrUsCexmEpr-IShgHNarm7Csks24pWcTAvGcSAVewFwYXTrNwyXIGis7G592Be1wZhlvm3Qr1S-Qf1Yr_lNHW4Vvundib2_cGqX_NFEUMAbcOxjou-MrDbg-ZD6ZxgBVQ_oeSNe=w856-h173)](https://blogger.googleusercontent.com/img/a/AVvXsEjsDjWDiI9JiGx2KX12nPkNxQgiMiwKWfMpamRUml1fnmjdd_h9Eq3TiRrUsCexmEpr-IShgHNarm7Csks24pWcTAvGcSAVewFwYXTrNwyXIGis7G592Be1wZhlvm3Qr1S-Qf1Yr_lNHW4Vvundib2_cGqX_NFEUMAbcOxjou-MrDbg-ZD6ZxgBVQ_oeSNe)

  

4.     
前往”虛擬私有雲網路 > IP位址”，找到外部IP 位址所在資料列中，點選其他動作按鈕，然後選擇「升級為靜態 IP 位址」。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhquEWgmdYLmVW2OTRRUd4LfFVdsLnzsA0qhjKtLoFOFcQSLy6WMseUOW8piWu9GILb6Yr6QxYBQ1kNYDVn4zsX_a2OkKGF_eHQUIlQzMH4yaF51TnEig05lPUDlNa2uyv7lpnjzUOCSKb3CdCOTe_Nkkrcl-zEuWzq4LRQBhJVjYZE8ybbOTvN7ObdJx9K=w861-h137)](https://blogger.googleusercontent.com/img/a/AVvXsEhquEWgmdYLmVW2OTRRUd4LfFVdsLnzsA0qhjKtLoFOFcQSLy6WMseUOW8piWu9GILb6Yr6QxYBQ1kNYDVn4zsX_a2OkKGF_eHQUIlQzMH4yaF51TnEig05lPUDlNa2uyv7lpnjzUOCSKb3CdCOTe_Nkkrcl-zEuWzq4LRQBhJVjYZE8ybbOTvN7ObdJx9K)

  

    輸入升級為靜態IP位址的名稱，按“保留“

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhFp_Pieg1Cie0IPQUpNVPnPYllPvnu0oz1HCIW_ltaUNk4Iks_K21UOMYiqnHhBpOHn-cjkRSnrCC2GYLchvrIRXUrEVaP5FjnCKLdVw-Qlj7GvQYER0cMGMvjxnERw3oR7TVaPk0Q6D4-ZqG4LyB780hOEO4JMl5Wy2fc8grvk4qNx3DhpxbnAYebXvZm=w400-h341)](https://blogger.googleusercontent.com/img/a/AVvXsEhFp_Pieg1Cie0IPQUpNVPnPYllPvnu0oz1HCIW_ltaUNk4Iks_K21UOMYiqnHhBpOHn-cjkRSnrCC2GYLchvrIRXUrEVaP5FjnCKLdVw-Qlj7GvQYER0cMGMvjxnERw3oR7TVaPk0Q6D4-ZqG4LyB780hOEO4JMl5Wy2fc8grvk4qNx3DhpxbnAYebXvZm)

  

    靜態IP升級完成

[![](https://blogger.googleusercontent.com/img/a/AVvXsEioiJs-KEX49kE3__ZIqIzy-5kAICIzuf5U9wQHP2X0RnE5N4Nn2OZQYQMd9Ln7u3ra8KegjQsTd1xXnbz2EqNIBY_DuZqFOHKyjGgh8GimOWK6ayS7yLqyeRQtD8FpHb7W-f0sklCeZNckuvivaJICP66R_-0w-K50fRZRhepTFi-6eTjssYKVBQrrddon=w854-h481)](https://blogger.googleusercontent.com/img/a/AVvXsEioiJs-KEX49kE3__ZIqIzy-5kAICIzuf5U9wQHP2X0RnE5N4Nn2OZQYQMd9Ln7u3ra8KegjQsTd1xXnbz2EqNIBY_DuZqFOHKyjGgh8GimOWK6ayS7yLqyeRQtD8FpHb7W-f0sklCeZNckuvivaJICP66R_-0w-K50fRZRhepTFi-6eTjssYKVBQrrddon)

**注意：請勿點選頁面上方的「Reserve External
Static IP Address」(保留外部靜態 IP 位址) 。**

 

**《為網站設定 DNS 區域》**

備妥靜態外部 IP 位址後，再來要將外部 IP 位址連結至網域名稱。

1.     
前往“Cloud DNS“頁面建立 DNS 區域，點選 [建立可用區]

[![](https://blogger.googleusercontent.com/img/a/AVvXsEisFMjBIWBehWBarNMnQmlGFabDvpLH2FMFj750i-re-irvDsM136Inw7miGBTaqw85HeT097JQlbs-8cW-vGSkLHAQpLMffEvgAyQy-ku2LDqQOUergp0JXmXRuWWdux07QwtIZY_DGjHRSOP4HehHh3Q8SUhsXLzzUSJToUMuCaM49Nck9biAKFXtsfhM=w640-h140)](https://blogger.googleusercontent.com/img/a/AVvXsEisFMjBIWBehWBarNMnQmlGFabDvpLH2FMFj750i-re-irvDsM136Inw7miGBTaqw85HeT097JQlbs-8cW-vGSkLHAQpLMffEvgAyQy-ku2LDqQOUergp0JXmXRuWWdux07QwtIZY_DGjHRSOP4HehHh3Q8SUhsXLzzUSJToUMuCaM49Nck9biAKFXtsfhM)

  

2.     
建立 DNS 區域

①       
在「可用區類型」中，選取 [公開]。

②       
輸入區域名稱，例：my-new-zone

③       
在「DNS 名稱」中，輸入您網站的網域名稱 (不含前置字元)，例如輸入
example.com，而不是 [www.example.com](http://www.example.com/)。

④       
如未設定 DNSSEC(DNS Security Extensions)，選“已停用“。

DNSSEC說明：[https://cloud.google.com/dns/docs/dnssec?\_gl=1\*d6jmtw\*\_ga\*MjA0MTI4MTI3LjE3MzIzNTc0Njk.\*\_ga\_WH2QY8WWF5\*MTczMjM1NzQ2OC4xLjEuMTczMjM2MTczMS4zNi4wLjA](https://cloud.google.com/dns/docs/dnssec?_gl=1*d6jmtw*_ga*MjA0MTI4MTI3LjE3MzIzNTc0Njk.*_ga_WH2QY8WWF5*MTczMjM1NzQ2OC4xLjEuMTczMjM2MTczMS4zNi4wLjA).

⑤       
選擇是否啟用將 DNS 查詢記錄至 Cloud Logging 的功能。 **※注意，這會產生費用。**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhV3b29Mjxuaw4TsO6cnHXgvETDK0y7XmsjJSGa5nky95HpTAO6z5l7ExU0N8QVPyJ22589GWzmYkd_EZCdLGZeDDFPt0sAneWHKLKu8qni1N3tqJCQQNkyMSMHQxTd4T2h4YcZbgmDJLW_yFWm6RXWbXSbfo6Ubhnz8x3WrF1777KG_qGVFglOSu_u72eq=w538-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEhV3b29Mjxuaw4TsO6cnHXgvETDK0y7XmsjJSGa5nky95HpTAO6z5l7ExU0N8QVPyJ22589GWzmYkd_EZCdLGZeDDFPt0sAneWHKLKu8qni1N3tqJCQQNkyMSMHQxTd4T2h4YcZbgmDJLW_yFWm6RXWbXSbfo6Ubhnz8x3WrF1777KG_qGVFglOSu_u72eq)

  

3.     
點選「建立」，這項操作會建立填入 NS 和 SOA 記錄的可用區。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj6cBqdbfEqBRFpKDqk2uA8U4BSYSOth_6GR5ZxrjUTmLflTkUb0TrmSgDTEFInqiJpCow1-pTIhQwaIffTo25aPYR4BFqfz6KlDF2AolzPetOR7vqfte5BrvchOPuhqTipzHuBWt0IiJhnJifXdGPsD5h7C7keiGboxFfZW2PvoDKK4V70He7LJf4aUZXk=w854-h511)](https://blogger.googleusercontent.com/img/a/AVvXsEj6cBqdbfEqBRFpKDqk2uA8U4BSYSOth_6GR5ZxrjUTmLflTkUb0TrmSgDTEFInqiJpCow1-pTIhQwaIffTo25aPYR4BFqfz6KlDF2AolzPetOR7vqfte5BrvchOPuhqTipzHuBWt0IiJhnJifXdGPsD5h7C7keiGboxFfZW2PvoDKK4V70He7LJf4aUZXk)

  

4.     
如要將已註冊的網域名稱指向託管伺服器的 IP 位址，必須將 A 記錄新增至可用區

①       
在「記錄集」 區段，點選「新增標準」。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhxP0ByfoHXeRvbqxSS8M40zhZdzRuxSalWnTcwrBR7mTrNThfCA3pSi9Oi7VKNHYGijT0AyKuOqB5CnLBbhoOJfoTgmkf5CnqNgrdkgq2751RZOnVNLFvsNpMfoXsB9wYuIp9lLMlnt88zis8B_us2d01escYZl209-mfTgYqcrM1attn9Fv-rBDOVUFv8=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEhxP0ByfoHXeRvbqxSS8M40zhZdzRuxSalWnTcwrBR7mTrNThfCA3pSi9Oi7VKNHYGijT0AyKuOqB5CnLBbhoOJfoTgmkf5CnqNgrdkgq2751RZOnVNLFvsNpMfoXsB9wYuIp9lLMlnt88zis8B_us2d01escYZl209-mfTgYqcrM1attn9Fv-rBDOVUFv8)

②       
「資源記錄類型」選擇 A（A record）。

③       
在「IPv4 位址」 中，輸入《開啟及管理網站》步驟4的VM靜態外部 IP 位址。

④       
按一下「建立」 即可為可用區建立 A 記錄。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiexRnn16K5TOihXcpaOhGqW_uyuoeMFtkeIBWVFe4OvoEjCf5VjBHebAT1Zadoaqp2Wa1Y8inU1ZhnFGnCgRkhqC_z3RSoTQDe8j5d7jtBWeo_cnVGkoigdlxDVcq1bRXjPt4knusBhRke8ALaXEq_jad1EYzGsQ7fH9UVJDXpDEj11RM6DMYeFa-omyNC=w544-h511)](https://blogger.googleusercontent.com/img/a/AVvXsEiexRnn16K5TOihXcpaOhGqW_uyuoeMFtkeIBWVFe4OvoEjCf5VjBHebAT1Zadoaqp2Wa1Y8inU1ZhnFGnCgRkhqC_z3RSoTQDe8j5d7jtBWeo_cnVGkoigdlxDVcq1bRXjPt4knusBhRke8ALaXEq_jad1EYzGsQ7fH9UVJDXpDEj11RM6DMYeFa-omyNC)

⑤       
A
record 建立完成

A record說明：<https://www.cloudflare.com/zh-tw/learning/dns/dns-records/dns-a-record/>

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgFo9m05VGlFJdAah4bAXD-EfMdD85u96VjpGB0YH0YKqPPMO9SR_Tg1B3upL_SWicnZcdF3c0GURB2VbaynursqJ4jcD_pFEbq49Oe8qTX9Y7PU8Y46hBjT4DTqIvn0MJ70nNzsIWK2FurAeBs0oFe0VJ8v4C4eHG444hMsjpRBBwPpVl4uiKHvFEpLHSa=w640-h335)](https://blogger.googleusercontent.com/img/a/AVvXsEgFo9m05VGlFJdAah4bAXD-EfMdD85u96VjpGB0YH0YKqPPMO9SR_Tg1B3upL_SWicnZcdF3c0GURB2VbaynursqJ4jcD_pFEbq49Oe8qTX9Y7PU8Y46hBjT4DTqIvn0MJ70nNzsIWK2FurAeBs0oFe0VJ8v4C4eHG444hMsjpRBBwPpVl4uiKHvFEpLHSa)

  
  

 

至此即已完成在 Compute Engine 上部署自訂網站，後續配置域名即可訪問在 Compute
Engine 托管的網站或服務。