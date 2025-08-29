---
title: "華為雲成本標籤---對雲服務器添加標籤及應用"
date: 2024-09-18 12:08:00
categories: ["華為雲"]
tags: ["華為雲", "標籤", "成本"]
permalink: /posts/huawei-cloud-label-cost-intro/
---
 可以透過以下兩種方式為華為雲雲端資源進行新增標籤(tag / tag management)的動作：

    1.經由TMS控制台新增

    2.透過各服務控制台新增

分別說明如下：

1.透過TMS控制台新增標籤

   透過標籤管理服務來統一為雲上資源進行標籤，以便於實現資源分類管理。

[![](/assets/images/HW-TMS-P.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2PdUTkJ3X6vGm3AfNUTsO9q2YrkwwxGjLmvvWELfeIgSCxU7Syn75vIKLkLZLGbPBbihPPZJrzgZnkULmre6RI2lkpXQKSrrtm5g_iA38-n87rK4DEOqzy7LAr937lTiS4M7zxrcNe0skM7EiEwNSuRPUynVOi2OxtZyNrsluIhjEs_1epl1yDTjG8Yg/s388/HW-TMS-P.jpg)

[![](/assets/images/HW-TMS-P2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgT_z1CJmIm9Lg3pFDTqP0e1ZasiAlroWcvm5QS8fgLqJmwWgQ5BfZcp_j5jSgNOCrU0T0fwYEiiiNeiIjPYeGU-J-l_txl3kFiICABT9e1jSWip-OhPqd32AuxA6FKkh7-_WtFhmguEcKet65A7T7Du39vI-ppPpj-FpX6sN_pizoKrDWcCMuD5z2M3Qs/s659/HW-TMS-P2.png)

1.登入管理控制台。

2.點擊頁面左上角的圖標，在彈出的服務清單中，選擇“管理與監管> 標籤管理服務”，進入標籤管理服務介面。

3.點選左側的“資源標籤”，選擇“資源配置標籤”頁籤。

4.設定資源搜尋條件。進行搜尋雲端資源。具體操作步驟可參考搜尋雲端資源。

5.按一下“搜尋”。

6.在搜尋結果清單中勾選需要新增標籤的雲端資源，點擊清單上方的“管理標籤”，進入管理標籤頁面。

7.在「新增標籤」區域，設定標籤的「鍵」和「值」。在標籤輸入框的下拉清單中可直接選擇已建立的標籤，無需輸入標籤的「鍵」與「值」。

8.按一下“確定”。

透過各服務控制台新增標籤

以上步驟僅為範例，透過各服務控制台新增標籤的特定操作請以各服務控制台實際顯示為準。

[![](/assets/images/螢幕擷取畫面 2024-09-17 084128.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjqSBR6c_Lzx91CMg5BDw051H35GrfrUloo7O5dERi2JkEmyWlszj2Ns-6e5aj5EdMH1v9Q4dfJwNLajaQiH0YU80nwsNvrbb8qRwDXlYWNk-t_hNw1v67Fl_uxNV1tI7S50TfVPFwVdfz1MVe0rPzZi5q2vbOcjkZfwBNBD4f67aUrqPl-JaRewgs-THP/s1124/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-09-17%20084128.png)

為查看標籤是否生效，您可以依照標籤搜尋該資源，透過搜尋指定標籤的方式驗證標籤是否生效。

2.透過各服務控制台新增標籤

        當您使用某一服務資源時，可以在對應服務控制台上為其新增標籤。對於新雲端資源，可以直接在設定參數時，對標籤項目進行設定。例如在創建 ECS 時添加標籤

  (1)登錄管理主控台。

  (2)按兩下左上角的指示，然後選擇您的區域和專案。

  (3)點選在 Compute （計算） 下的項目中，選擇 Elastic Cloud Server （彈性雲伺服器）。

  (4)按兩下購買ECS。

  (5)配置 ECS 的參數。

  (6)為 Advanced Options 選擇 Configure now （立即配置）。然後，添加標籤鍵和標籤值。

[![](/assets/images/HW-newECS-tag.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheeNVhroGMy_r2uh0XhuOfswj4In5dQ06YiwUlP5SKkaWlOomnD-wtEYTzp5464sZQU9W3B8qxw805osMrRcHoJD7id-IL5qKupbLohmMIyF5UnJBHRugkhAuLH1UiFhPNNQQ2vFEt9dWBkM43dIHzdt-6LBkK95poo9ghyv4Pl1hoVLk2T3luLacShNg/s914/HW-newECS-tag.jpg)

  

說明：

推薦您使用預先定義標籤功能：為雲端資源新增標籤時，可直接在標籤輸入框的下拉清單中選擇已建立的預定義標籤，無需輸入標籤的“鍵”與“值”，避免因大量重複添加標籤而產生錯誤與效率低的問題。

強烈建議勿將機密資訊或敏感資訊（例如您客戶的姓名、電子郵件地址或手機號碼）放入標籤欄位。

注意：標籤約束與限制

每個資源最多支援10個鍵-值對。

對於每個資源，每個標籤「鍵」都必須是唯一的，每個標籤「鍵」只能有一個「值」。

鍵的長度最大36個字符，由英文字母、數字、底線、中劃線、中文字符組成。

值的長度最大43個字符，由英文字母、數字、底線、點、中劃線、中文字符組成。

另外可參考華為官網以利確認相關介紹。

https://support.huaweicloud.com/usermanual-ecs/ecs\_03\_0903.html