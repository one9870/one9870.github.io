---
title: "華為雲成本標籤介紹"
date: 2024-09-11 12:28:00
categories: ["華為雲"]
tags: ["華為雲", "標籤"]
permalink: /posts/huawei-cloud-label/
---
1.什麼是標籤

標籤用於標記客戶在華韋雲雲端所布置或設定的資源，如實例、鏡像等。

如果客戶的帳戶下方有多種雲端資源，且在不同雲端資源之間存在有多種關聯性，則可以使用此標籤功能按所需的分類（例如資源用途、資源使有者或開發環境等）對雲端資源進行標記。

 

圖1 標籤範例

[![](/assets/images/華韋文章一P0.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcC8hnoNGnBnY7HGDulSLTodpbR03I-4J9XmkUGKMSxx_LntLZgiTX0gzjNnR4-hwrMLUImexTEeq8J5S1NfzjK_m2oVVheEFgnXL3MD9UkpIDAKrtZKT0cfaz6ttCu7nrCaQWhQZYeKwrD7oUtJNFkICcGe0Etio1_d6JGLDkq-m6MVIH2xwLWGDFMQc/s1026/%E8%8F%AF%E9%9F%8B%E6%96%87%E7%AB%A0%E4%B8%80P0.jpg)

  

在此範例中，您為每個雲端資源指派了兩個標籤，每個標籤都包含您定義的一個“鍵”和一個“值”，一個標籤使用鍵為“擁有者”，另一個使用鍵為“用途”，每個標籤都擁有相關的值。標籤的設計原則請參閱標籤設計原則和命名範例。

 

您可以根據為雲端資源新增的標籤快速搜尋和篩選特定的雲端資源。例如，您可以為帳戶中的雲端資源定義一組標籤，以追蹤每個雲端資源的擁有者和用途，使資源管理變得更加輕鬆。

 

2.什麼是成本標籤

您可以將標籤啟動為成本標籤，以方便您對華為雲端成本進行分類和追蹤。只有啟動後的標籤，才會應用在成本資料上。啟動成本標籤的具體操作請參閱啟動成本標籤。

 

成本標籤的來源主要包括以下兩種：

 

費用：即使用者在建立資源時所新增的標籤，一般在建立並產生費用24小時後才會顯示在「成本標籤」頁面。

預先定義標籤：即使用者在「標籤管理服務」控制台中建立的預先定義標籤，該標籤建立後即時展示在「成本標籤」頁面。

 

3.成本標籤的應用

 

您可以在「成本分析」頁面使用成本標籤匯總或過濾成本數據，也可以在預算管理中追蹤指定標籤的成本和用量情況。

 

4.成本標籤的限制：目前已支援標籤集中管理，也可參閱標籤與其他雲端服務的關係。

5.啟動成本標籤

   (1)登錄成本中心(Cost Center )。

   (2)選擇 Cost Allocation> Cost Tags。

   (3)選擇一個標記並啟動或停用它。

[![](/assets/images/HW-TAG-a or d.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgUodwlPaqX-zphB46iYzZw70iYLeQB4yU4RW2-f4toEZfPCGiJD0Zak7UqI3Be6rInUWS5usJGmhToNBm7aU0IEydg99Welc1tn3JgC5t-AkDmNo3G8y2w3UTgGxSOPIfnkuzT5OTUAl7ZB9liXpKu8kas0TGjcoTlt9JPen28AOmM13JVplm_9scGLDU/s856/HW-TAG-a%20or%20d.jpg)

6.對標籤的命名原則

(1)可以按資源的屬性（例如按部門、區域或專案）標記資源。

(2)使用標準化標籤名稱

標準化的標籤名稱應滿足以下要求：

(2-1)對所有標籤鍵和值使用一致的大小寫，例如小寫或大寫。

(2-2)如果標籤名稱中使用了中文字元，建議將字元數限制在6個字元以內，以免超過上限。

(2-3)使用一致且簡潔的標籤名稱

(2-4)建議對同一屬性使用一致的表達式。

(2-5保持標籤鍵和值清晰簡潔。請勿使用標記名稱來指示多個含義。

(3)提前計劃和預定義標籤

可以在規劃資源的同時規劃和預定義標籤，尤其是標籤鍵。然後使用預定義的標籤來對資源進行分類。

(4)避免包含隱私資訊：應避免包含企業隱私資訊，例如機密，企業專案名稱、收入資訊、電話號碼或電子郵件位址等。

例如，如果使用 「purpose」 來表示 resource utility，則應避免使用其他詞語 （如 “use” 或 “object”） 來表示 resource utility。

可參考以下範例表來建立標籤：

[![](/assets/images/HW-TAG-EX.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnxt-hRfaPtoM_nBsOBLvnOlB66R5aDmoCbeWjQm3o9i3WxIZlION6nvEp3N9xOtVTS4-tXrMEr_e2f4UFtQJk5EFtmkZiD-wKaf3zI1rez5fTbgNH0buK5sxXWylcQDN4hTMeEDJmVgKpB4gsken8580_vgd4Lh_mxnma45_9zpdLKLakgH9mhQ25eyM/s747/HW-TAG-EX.jpg)

  

原廠文章參考網址https://support.huaweicloud.com/usermanual-cost/costcenter\_000005\_01.html