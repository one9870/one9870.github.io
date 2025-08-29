---
title: "Azure－使用標籤繼承來分組和配置成本"
date: 2024-09-19 17:37:00
categories: ["AZURE"]
tags: ["AZURE", "教學30天上手"]
permalink: /posts/azure-label-cost-control/
---
 如何在成本管理中使用標籤繼承設定。 啟用時，標籤繼承會將帳單、資源群組和訂用帳戶標籤套用到子系資源使用量記錄。 您不需要標記每個資源，或依賴發出使用量的資源擁有自己的標籤。

標籤繼承適用於下列計費帳戶類型：

1.Enterprise 合約 (EA)

2.Microsoft 客戶合約 (MCA)

3.Microsoft 合作夥伴合約 (MPA) 搭配 Azure 方案訂用帳戶

**需特別注意：繼承的標籤會套用至子系資源使用量記錄，而不是資源本身。**

**[![](https://blogger.googleusercontent.com/img/a/AVvXsEhF7bp264o_f2l51hEwQ2Wp9MW60mU6Ixq5xHgFj0487b7kRkR2BPefUl33pvcBYMqftZZpklYnkyT7yrDZi1UiU6_FMBFemHyNeF2dospfjP-n3h3-88vUCDN5H1ejO5QRWRnxGxvMmVDXsWyRsQTI0LeiL-MMNTUUhz3lCOY5Z4rCFKhchxFA9rgSoe4=w400-h191)](https://blogger.googleusercontent.com/img/a/AVvXsEhF7bp264o_f2l51hEwQ2Wp9MW60mU6Ixq5xHgFj0487b7kRkR2BPefUl33pvcBYMqftZZpklYnkyT7yrDZi1UiU6_FMBFemHyNeF2dospfjP-n3h3-88vUCDN5H1ejO5QRWRnxGxvMmVDXsWyRsQTI0LeiL-MMNTUUhz3lCOY5Z4rCFKhchxFA9rgSoe4)**

所需的權限

針對訂用帳戶：  
要檢視的成本管理讀者、要編輯的成本管理參與者  
針對 EA 計費帳戶：  
要檢視的企業管理員 (唯讀)、要編輯的企業管理員  
針對 MCA 帳單設定檔：  
要檢視的帳單設定檔讀者、要編輯的帳單設定檔參與者

-----------------------------------------------------------------------------------------------------------------------------

### 在 Azure 入口網站為 EA 計費帳戶啟用標籤繼承

1.在 Azure 入口網站搜尋 [成本管理] 並加以選取 (綠色六邊形符號，不是 [成本管理] + [帳單])。

選取範圍。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgOJtD8MSVjUhAj7xZKH0Jklur1cyKlCuoaH-VJrVXct1Z28JSLlAKTJU3rM9dpPZueOOowAB9oW_HxHKPNCH8lB_dMvaMrppsxibisWsfTxfG7gKtJ11Arc1ASRGgt6ovtwZx4o8SWjDP-BvU50gJRlIe6Sy8usoIrcN1QbO99i_iineXtSAB2KJXYPVg=w385-h400)](https://blogger.googleusercontent.com/img/a/AVvXsEgOJtD8MSVjUhAj7xZKH0Jklur1cyKlCuoaH-VJrVXct1Z28JSLlAKTJU3rM9dpPZueOOowAB9oW_HxHKPNCH8lB_dMvaMrppsxibisWsfTxfG7gKtJ11Arc1ASRGgt6ovtwZx4o8SWjDP-BvU50gJRlIe6Sy8usoIrcN1QbO99i_iineXtSAB2KJXYPVg)

  

2.在左側功能表的 [建立] 底下，選取 [組態]。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjBm8CRE9_ds4fs619afbo3h_zKBLSzZyL7jmSS4RwPy6OU69AOCEaGYECg6hqSApdT5OwdA6XIJHReEsDcyBz1FvbOGQzlNfXTbGr5is2q0xPa4sdTrxCRrQt_4UCXfakrIlGV4m9eMGTWa1vuX0tZTz5naKq3VHWYasbOSmuOQaWFtXrJpfwIjZFZOXs=w400-h275)](https://blogger.googleusercontent.com/img/a/AVvXsEjBm8CRE9_ds4fs619afbo3h_zKBLSzZyL7jmSS4RwPy6OU69AOCEaGYECg6hqSApdT5OwdA6XIJHReEsDcyBz1FvbOGQzlNfXTbGr5is2q0xPa4sdTrxCRrQt_4UCXfakrIlGV4m9eMGTWa1vuX0tZTz5naKq3VHWYasbOSmuOQaWFtXrJpfwIjZFZOXs)

  

3.在 [標籤繼承] 底下，選取 [編輯]。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhDVZENSpi0uKf9uaRZ12Y_EXvZcyP3e1dpadg8SqIPuDvOBWhVl_HVyUAnOQklBGIxEbae2YeqD5gU_WzO9JP8bYzdQiu5To5smPhdAgFe6sXI4PgS3Psybi_VQK0rNTrwZZHfMXRq1ROvUrjef01_XnyEWy1GA0CIog51i33qEleSifxJKlmvixMT9C4)](https://blogger.googleusercontent.com/img/a/AVvXsEhDVZENSpi0uKf9uaRZ12Y_EXvZcyP3e1dpadg8SqIPuDvOBWhVl_HVyUAnOQklBGIxEbae2YeqD5gU_WzO9JP8bYzdQiu5To5smPhdAgFe6sXI4PgS3Psybi_VQK0rNTrwZZHfMXRq1ROvUrjef01_XnyEWy1GA0CIog51i33qEleSifxJKlmvixMT9C4)

4.在 [標籤繼承] 視窗中，勾選 [自動將訂用帳戶和資源群組標籤套用至新資料]。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhLp35XltE6f2NPcB81b0TGQi8Qxs9vvT067o8oLPAJKVndrvwyEkwZ-f8fyS6AdClJmLdqx75VcHWK_eHNHu1DjeW7DfLW6wY1js1TrI3VutK3vf_9XSG6glInk0wjq_cQmqHSwmRnTiPZUGDmfWwo3MASNIMQcF1HexgaAQF5nmyUHXwtD35O3KDemhM=w400-h282)](https://blogger.googleusercontent.com/img/a/AVvXsEhLp35XltE6f2NPcB81b0TGQi8Qxs9vvT067o8oLPAJKVndrvwyEkwZ-f8fyS6AdClJmLdqx75VcHWK_eHNHu1DjeW7DfLW6wY1js1TrI3VutK3vf_9XSG6glInk0wjq_cQmqHSwmRnTiPZUGDmfWwo3MASNIMQcF1HexgaAQF5nmyUHXwtD35O3KDemhM)

啟用標籤繼承後，訂用帳戶和資源群組標籤會在 24 小時內套用至目前月份的子系資源使用量記錄。  

### 在 Azure 入口網站為 MCA 帳單設定檔啟用標籤繼承

1.在 Azure 入口網站搜尋 [成本管理] 並加以選取 (綠色六邊形符號，不是 [成本管理] + [帳單])。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgpGxaYAPiUzvtRs0L73RqPRVYiKf_8pFK5aCwDgbdukVbfpYvpbRQs4U9U2z0yvObJBjWZkvfbAqi9AMU_pgwq37UZXNX3i0zmot5dq-T7v4gSFKFusuiVNc_wcTlld5BLQkrIg6_91C8kGln1Y6diPwqgeusKzCQhJwbN4MzL2QRxbXJRKDym3kBb4Ck=w385-h400)](https://blogger.googleusercontent.com/img/a/AVvXsEgpGxaYAPiUzvtRs0L73RqPRVYiKf_8pFK5aCwDgbdukVbfpYvpbRQs4U9U2z0yvObJBjWZkvfbAqi9AMU_pgwq37UZXNX3i0zmot5dq-T7v4gSFKFusuiVNc_wcTlld5BLQkrIg6_91C8kGln1Y6diPwqgeusKzCQhJwbN4MzL2QRxbXJRKDym3kBb4Ck)

  
  
2.選取範圍  
3.在左側功能表的 [設定] 底下選取 [管理帳單設定檔]。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjhTIqs2NW5U7lEsATuAZ2XojvXG2kj6dBUE3fmsvpnD20-4tpl-QqrWNQCxNkjxiGFK_pHWP50oul1VkbYjwupz66TGGANykY1tNcSaN94P17ZjoKAukoBT2tGXHWjxXyEQM8Hcs0W_5WfADx84kKNAaF3MGONP0WV-eT55Z35BWAdvBb1XMwOQult1ZI=w400-h195)](https://blogger.googleusercontent.com/img/a/AVvXsEjhTIqs2NW5U7lEsATuAZ2XojvXG2kj6dBUE3fmsvpnD20-4tpl-QqrWNQCxNkjxiGFK_pHWP50oul1VkbYjwupz66TGGANykY1tNcSaN94P17ZjoKAukoBT2tGXHWjxXyEQM8Hcs0W_5WfADx84kKNAaF3MGONP0WV-eT55Z35BWAdvBb1XMwOQult1ZI)

  
  
4.在 [標籤繼承] 底下，選取 [編輯]。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEikixm7Go_Qi4IfDuWNmDfCxLFgcleT-rQNDrPeHmV3O5Fw4QNZWFzJFloBII9OdCtD7Dv9xEy5UCtcxmJuagWHfrmTHhkpuzkW8JCAVaj65op_k04B1_NB5ca1f1nSpuZI5sHulGhhYk7e8SAoQw_r5O2tjutyGctDcvWuiH4HoRaGl8SS2ToIwG-e8Yk)](https://blogger.googleusercontent.com/img/a/AVvXsEikixm7Go_Qi4IfDuWNmDfCxLFgcleT-rQNDrPeHmV3O5Fw4QNZWFzJFloBII9OdCtD7Dv9xEy5UCtcxmJuagWHfrmTHhkpuzkW8JCAVaj65op_k04B1_NB5ca1f1nSpuZI5sHulGhhYk7e8SAoQw_r5O2tjutyGctDcvWuiH4HoRaGl8SS2ToIwG-e8Yk)

5.在 [標籤繼承] 視窗中，選取 [自動將帳單、訂用帳戶和資源群組標籤套用至新資料]。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgq-XeM_hXBFFzFtv4Dxu4TBZTA3nwScow7n-sP0IcLrM4EsV5Wu1Yq5135iuMXkV-iTKHdCcDcGna2gZmPjiNFvMx0krh_pe4PdD_hy3jPEDbilPy8OT7UjWDflpv-QHiIOMPrAisDEjzPTZ37qvP11e8aawdBfxoldWgbHKtfSV9tB4I5Iea8b_bVQu0)](https://blogger.googleusercontent.com/img/a/AVvXsEgq-XeM_hXBFFzFtv4Dxu4TBZTA3nwScow7n-sP0IcLrM4EsV5Wu1Yq5135iuMXkV-iTKHdCcDcGna2gZmPjiNFvMx0krh_pe4PdD_hy3jPEDbilPy8OT7UjWDflpv-QHiIOMPrAisDEjzPTZ37qvP11e8aawdBfxoldWgbHKtfSV9tB4I5Iea8b_bVQu0)

啟用標籤繼承後，帳單設定檔、發票區段、訂用帳戶和資源群組標籤會在 24 小時內套用至目前月份的子系資源使用量記錄。  

### 在 Azure 入口網站為訂用帳戶啟用標籤繼承

1.在 Azure 入口網站搜尋 [成本管理] 並加以選取 (綠色六邊形符號，不是 [成本管理] + [帳單])。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjCHzjHi7P-9py3Ey3ALZ53mOlGhIfwznIzyTWetqcgYk3B5kjhUrtA5JO0QJLnIUu-mT8qb47fLsgPFsMWF_xQaiM8LgEvnljSvlOhboHv6RvpYylyZ5-8GHgPADgFE0do9But3aSa021kJNDtueLydSBRRxnWYKwqF1bABBd7seAPLJjFU0J3pnAbs5o)](https://blogger.googleusercontent.com/img/a/AVvXsEjCHzjHi7P-9py3Ey3ALZ53mOlGhIfwznIzyTWetqcgYk3B5kjhUrtA5JO0QJLnIUu-mT8qb47fLsgPFsMWF_xQaiM8LgEvnljSvlOhboHv6RvpYylyZ5-8GHgPADgFE0do9But3aSa021kJNDtueLydSBRRxnWYKwqF1bABBd7seAPLJjFU0J3pnAbs5o)

2.選取訂用帳戶範圍。

3.在左側功能表的 [設定] 底下選取 [管理訂用帳戶]。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiXF7GWRc2BoE0fMa5x5d3USXXqvQkwgMR5rKPxFsf1u-U2qnKUiI9r396FdnHdAL-uT5ClKROnbhuBCUBXMb1lEAkCliHFImKh1be8cRY-I8gfB8M0L-BOZnXmMCSVRYwzU02VZ2bvnTETGl2wea2jz5dyhXMqxt8d1Pva9bPVNobRNwxYWnsOPL8kLbE)](https://blogger.googleusercontent.com/img/a/AVvXsEiXF7GWRc2BoE0fMa5x5d3USXXqvQkwgMR5rKPxFsf1u-U2qnKUiI9r396FdnHdAL-uT5ClKROnbhuBCUBXMb1lEAkCliHFImKh1be8cRY-I8gfB8M0L-BOZnXmMCSVRYwzU02VZ2bvnTETGl2wea2jz5dyhXMqxt8d1Pva9bPVNobRNwxYWnsOPL8kLbE)

4.在 [標籤繼承] 底下，選取 [編輯]。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh2oUKrlcfOd-0N-Em-rTe-i7WHDVQodyqPuU02q7JLX4xElOHy6cfQJjvISYgx5alfU8zPegSUIPpuklU56xC1ujtiHsxX-BMf3va0h2WBG9EFdjOewBMO46-PbOZDO5Py_aiZTkxomayqSvdMQgfWDTRbLHcmS0IZkUtkFcodU4SOMgBn6nmxn_OiALc)](https://blogger.googleusercontent.com/img/a/AVvXsEh2oUKrlcfOd-0N-Em-rTe-i7WHDVQodyqPuU02q7JLX4xElOHy6cfQJjvISYgx5alfU8zPegSUIPpuklU56xC1ujtiHsxX-BMf3va0h2WBG9EFdjOewBMO46-PbOZDO5Py_aiZTkxomayqSvdMQgfWDTRbLHcmS0IZkUtkFcodU4SOMgBn6nmxn_OiALc)

5.在 [標籤繼承] 視窗中，選取 [自動將訂用帳戶和資源群組標籤套用至新資料]。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEha7510O7ikjgBtvuztYRA_Y6leTZ5hkIRRSd0GkzOPr7Hq94cJX5UQTWuSYTUVxCfT26MK-RTllTzZ1ADzjF2c16CCP9_QOitM9oQahhI_HCI2L2ZI8mbP12Ng2p_7MwtPOOwvUQ7EE0K52brSI2jBJ0OIemZfU8_NUGoK5bAQdfaCY1j6j-y2HnGLtHI)](https://blogger.googleusercontent.com/img/a/AVvXsEha7510O7ikjgBtvuztYRA_Y6leTZ5hkIRRSd0GkzOPr7Hq94cJX5UQTWuSYTUVxCfT26MK-RTllTzZ1ADzjF2c16CCP9_QOitM9oQahhI_HCI2L2ZI8mbP12Ng2p_7MwtPOOwvUQ7EE0K52brSI2jBJ0OIemZfU8_NUGoK5bAQdfaCY1j6j-y2HnGLtHI)

### 在資源與繼承的標籤之間進行選擇

資源標籤符合已套用的繼承標籤時，資源標籤預設會套用到其使用量記錄。 您可以變更預設行為，讓繼承標籤覆寫資源標籤。

**適用於 EA 客戶：**

在 [標籤繼承] 視窗中，選取 [使用訂用帳戶或資源群組標籤] 選項。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjVion102TSX-MAvJCDJSajnqSNCrFmJZsMjSlEWMzSzaA9iwNoDH-38e1We5leD0907v2yhYVwWcg5toSw_oO38wXjrXzFSP_SiO2Nll4TMJ856hiaoYO2JMWvUvO3dD6uT1W4rxjEydMkk6NTWPOeFAM-DVwYY3R0mWemDFhBrlLXOh0iy_UPPaJpcBE)](https://blogger.googleusercontent.com/img/a/AVvXsEjVion102TSX-MAvJCDJSajnqSNCrFmJZsMjSlEWMzSzaA9iwNoDH-38e1We5leD0907v2yhYVwWcg5toSw_oO38wXjrXzFSP_SiO2Nll4TMJ856hiaoYO2JMWvUvO3dD6uT1W4rxjEydMkk6NTWPOeFAM-DVwYY3R0mWemDFhBrlLXOh0iy_UPPaJpcBE)

### 適用於 MCA 客戶：

在 [標籤繼承] 視窗選取 [使用繼承標籤] 選項。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgnkOMoxe_2MhOVHEvYwJgXFaGwlhx_03RXMfiALQFsSH5apc2Km4XihFmWO2UQcucaZ1b7LFMSU4TTf5_bqRiFHCfNwtvo8Sm9xUlkXEzUILXzrBdgv181_gLoJqvOv-hlTdxw5dhpzDwsvmSNLrKB9pe7Cf4JdcBdhxrRAzqYgTiGWWxATT1-ZMJd_tE)](https://blogger.googleusercontent.com/img/a/AVvXsEgnkOMoxe_2MhOVHEvYwJgXFaGwlhx_03RXMfiALQFsSH5apc2Km4XihFmWO2UQcucaZ1b7LFMSU4TTf5_bqRiFHCfNwtvo8Sm9xUlkXEzUILXzrBdgv181_gLoJqvOv-hlTdxw5dhpzDwsvmSNLrKB9pe7Cf4JdcBdhxrRAzqYgTiGWWxATT1-ZMJd_tE)

資源標籤的範例。下圖中，資源 4 和資源群組 2 具有相同的標籤：App。 由於使用者選擇保留資源標籤，所以使用量記錄 4 會使用資源標籤值 E2E 來更新。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgkikwadS3is8NSvhEh5GxtmqY2FeTCKAUwrB64MRTMVLpdT6jU41rWgVITqEO_A2M5GonzhPlxwk366MJzQYZEltbgm3gKAjGsQQBzEGLL7TAEScgDlbCcrMQ0kaFrjTlrkvYHq05lheqATy-0VXRyOcreXvdyHM8vRp4tKgKVeB5IfRnAUPNRBrQyTNA)](https://blogger.googleusercontent.com/img/a/AVvXsEgkikwadS3is8NSvhEh5GxtmqY2FeTCKAUwrB64MRTMVLpdT6jU41rWgVITqEO_A2M5GonzhPlxwk366MJzQYZEltbgm3gKAjGsQQBzEGLL7TAEScgDlbCcrMQ0kaFrjTlrkvYHq05lheqATy-0VXRyOcreXvdyHM8vRp4tKgKVeB5IfRnAUPNRBrQyTNA)

另一個會覆寫資源標籤的範例。 下圖中，資源 4 和資源群組 2 具有相同的標籤：App。 由於使用者選擇使用資源群組或訂用帳戶標籤，使用量記錄 4 會使用資源群組標籤值 (backend¹) 來更新。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh4UNZ_8HDEyZg0LZirKYGUs5TU690e9glEanL-phm6p-FNQ2tUejhZbrda8wrIreW_ZT4c1XaW2gbhN6rfaBxbSuIJVFY0xlZTXNuv609DQuzyO7Tekco8WtvxfAP9F_5MyFujuzBl0RDpLmPR6X-9yfK4EBbkPMnaGTF6FF_Pl0LkB-obxT02CwOXJJs)](https://blogger.googleusercontent.com/img/a/AVvXsEh4UNZ_8HDEyZg0LZirKYGUs5TU690e9glEanL-phm6p-FNQ2tUejhZbrda8wrIreW_ZT4c1XaW2gbhN6rfaBxbSuIJVFY0xlZTXNuv609DQuzyO7Tekco8WtvxfAP9F_5MyFujuzBl0RDpLmPR6X-9yfK4EBbkPMnaGTF6FF_Pl0LkB-obxT02CwOXJJs)

若訂用帳戶和資源群組標籤與資源標籤相同，且您選取 [使用訂用帳戶或資源群組標籤] 選項，就會使用訂用帳戶標籤。

### 檢視依標籤分組的成本

您可以使用成本分析來檢視依標籤分組的成本。

1.在 Azure 入口網站中，瀏覽至 [成本管理]。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj3xKYfFy8Tp2f2v_g4iKI45EuV4E-qZf6WLSyhSopQvkSRpenwSPCMWHmEbMDsXHDLVqztxN5wYsz1tDu5VSxtZVh0XjRXGhT7X4-Lm2ZtihPt8TleUYhsV4qTrRFtXVmV-Bp_GOU2uZTlhpvC58-pYDDSbvbSS3jhzFwgMIn2pp35gdl-DqwkrnZaNRw)](https://blogger.googleusercontent.com/img/a/AVvXsEj3xKYfFy8Tp2f2v_g4iKI45EuV4E-qZf6WLSyhSopQvkSRpenwSPCMWHmEbMDsXHDLVqztxN5wYsz1tDu5VSxtZVh0XjRXGhT7X4-Lm2ZtihPt8TleUYhsV4qTrRFtXVmV-Bp_GOU2uZTlhpvC58-pYDDSbvbSS3jhzFwgMIn2pp35gdl-DqwkrnZaNRw)

2.左側功能表中，選取 [成本分析]。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjodYXvcEoP8lPPPD_k_Swqg50MHj7QS7fub15kI6F6IxaKiOmyg1Pb1JIoYINzSyO32vl84x6RgwSqmfQ4OP-ZhB2Ueb3B14UUuM_tsy4eW8c6kxOdI1Ii0LPTKyB3nujWytYtPSRZGXelqFRIi7dvxnaSV5JLoFSN504pocbBTdnNYbJEKRvfV-9MCSw)](https://blogger.googleusercontent.com/img/a/AVvXsEjodYXvcEoP8lPPPD_k_Swqg50MHj7QS7fub15kI6F6IxaKiOmyg1Pb1JIoYINzSyO32vl84x6RgwSqmfQ4OP-ZhB2Ueb3B14UUuM_tsy4eW8c6kxOdI1Ii0LPTKyB3nujWytYtPSRZGXelqFRIi7dvxnaSV5JLoFSN504pocbBTdnNYbJEKRvfV-9MCSw)

3.選取範圍。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi1ZRQzUezJsRU8u5mmub6h3Sxru5s2AEZwLe0xsKU3yAzjRsTwtzjkT2UlCLE7YD6iFDTPvCZkFUP-7wLbhpshgBXOKQE_f5PZXbEGOgcdYBdi1xwnYFp2cOFGLi9pn8EqeYnW0v6ofo-7Jf2oTpuPPIJ3oRDOWLBVblgaVFmDJgE51vfMrFvYJUezcyI)](https://blogger.googleusercontent.com/img/a/AVvXsEi1ZRQzUezJsRU8u5mmub6h3Sxru5s2AEZwLe0xsKU3yAzjRsTwtzjkT2UlCLE7YD6iFDTPvCZkFUP-7wLbhpshgBXOKQE_f5PZXbEGOgcdYBdi1xwnYFp2cOFGLi9pn8EqeYnW0v6ofo-7Jf2oTpuPPIJ3oRDOWLBVblgaVFmDJgE51vfMrFvYJUezcyI)

4.在 [群組依據] 清單中，選取您要檢視成本的標籤。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiiYqGLrKsQck78s-91wTwEwU57G2nUhaBOiDVNaas4DL_VJ-B8YUbDaMwv-4ZiFM3m0EIxwJrA6Oc2DVeb1zh8smmkj557MUVqUuHfza51cBZIoNWc2wPvU4t2euBSjFeKwUS-d9ax1f6JR_4BLdQ2doy1tX5-pM_m1LMXiZpQ1bUCsXEdIKh6m7K1F_0)](https://blogger.googleusercontent.com/img/a/AVvXsEiiYqGLrKsQck78s-91wTwEwU57G2nUhaBOiDVNaas4DL_VJ-B8YUbDaMwv-4ZiFM3m0EIxwJrA6Oc2DVeb1zh8smmkj557MUVqUuHfza51cBZIoNWc2wPvU4t2euBSjFeKwUS-d9ax1f6JR_4BLdQ2doy1tX5-pM_m1LMXiZpQ1bUCsXEdIKh6m7K1F_0)

您可以在啟用標籤繼承 24 小時後，在繼承的標籤上建立具有篩選條件的預算。 您也可以下載 Azure 使用量來檢視繼承的標籤。

參考資料:https://learn.microsoft.com/zh-tw/azure/cost-management-billing/costs/enable-tag-inheritance