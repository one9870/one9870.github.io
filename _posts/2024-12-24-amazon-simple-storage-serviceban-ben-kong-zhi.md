---
title: "Amazon Simple Storage Service版本控制"
date: 2024-12-24 19:39:00
categories: ["AWS", "AWS教學30天上手"]
tags: ["AWS", "AWS教學30天上手"]
permalink: /posts/amazon-simple-storage-serviceban-ben-kong-zhi/
---
 

使用 S3 版本控制將物件的多個版本保留在一個儲存貯體中，以便可以還原意外刪除或覆寫的物件

 

S3啟用版本控制

1. 登入 AWS
   Management Console 並開啟 Amazon S3 主控台。
2. 在 **Buckets** (儲存貯體) 清單中，選擇要啟用版本控制的儲存貯體名稱。
3. 選擇 **Properties** (屬性)。
4. 在 **Bucket
   Versioning** (儲存貯體版本控制) 底下，選擇 **Edit** (編輯)。
5. 選擇 **Suspend** (暫停) 或 **Enable** (啟用)，然後選擇 **Save
   changes** (儲存變更)。

列出已啟用版本控制之儲存貯體中物件版本

      1.登入 AWS Management Console 並開啟 Amazon S3 主控台。  
      2.在 Buckets (儲存貯體) 清單中，選擇包含該物件的儲存貯體名稱。  
      3.若要查看儲存貯體中的物件版本清單，請選擇 Show versions (顯示版本) 切換開關。

(設定版本控制狀態之前儲存貯體中所存放的物件會有 null 的版本 ID。)

 

已啟用版本控制之儲存貯體中的物件

一.新增物件:

儲存貯體上啟用版本控制後，Amazon S3 便會自動將唯一的版本 ID 新增至儲存貯體中存放的每個物件 (使用 PUT、POST 或 CopyObject)。

[![](/assets/images/圖片1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgucCr7w2bHdjF6g0YHcPKfauASBfyygGImt6uKBauh1CIjqw5XiDX_Bj9Sr0waiBSL8LBjlJtXaV8XL5gcxcpDCpWPBlAtgSlJay1aEO2S-xNY7hYoEGIi8Kw7cjia7lk8LmG203lynqDAwm2kWPemL_wvToc4TxuWlMR929rn2er5RIMNqgH7YAfjAfSj/s363/%E5%9C%96%E7%89%871.png)

  
  

二.擷取物件:

簡單 GET 要求會擷取物件的目前版本。下圖顯示 GET 如何傳回 photo.gif 物件的目前版本。

 

[![](/assets/images/圖片2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhakoTFedudFmwfgRW15PHxRjz8KyATjvUlhFmoGOSSYWR5hDgJzJrSgYB4IhQGglZ4crCLpArtG7U_8iZWcqhyphenhyphen7-90ARQr3XRaLj2ix1dGFjyeLp2ayXw_IkdRZCqpGumVErgLuQiJ6TF6Sfck2Du4Vyfgf4gWrEU1gkQes0cAoUi4En5LPcvXVGw_wEzA/s554/%E5%9C%96%E7%89%872.png)

  

若要擷取特定版本，您必須指定其版本 ID。下圖顯示 GET versionId 要求如何擷取物件的指定版本

 

[![](/assets/images/圖片3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhi8lMPTfUTxOd2GoVeKuWd13FJFO4zBGEe9mBxjJ0eJ5Hh2kkhsW1yToYkYfkt8LM0I07l4YHurl45-fGvR4cui6c9PF4_e9Z6te2_3teV8srwpqu_KLOEjGyh2o13vWWPK-kTEScaDhix1hWnA307D1KVZhj2uDdUV-o2N5j6jxU7I7WtQS6cE19zamnb/s554/%E5%9C%96%E7%89%873.png)

  

使用主控台下載特定版本

1. 登入 AWS
   Management Console 並開啟 Amazon S3 主控台。
2. 在 **Buckets** (儲存貯體) 清單中，選擇包含該物件的儲存貯體名稱。
3. 在 **Objects** (物件) 清單中，選擇物件的名稱。
4. 選擇 **Versions** (版本)。

Amazon S3 會顯示該物件的所有版本。

5. 選取要擷取版本之 **Version
   ID (****版本 ID)** 旁邊的核取方塊。
6. 選擇 **Actions** (動作)，選擇 **Download
   (****下載)**，然後儲存物件。

 

三.刪除物件

啟用版本控制時，簡單 DELETE 無法永久刪除物件。Amazon S3 會在儲存貯體中插入刪除標記，而該刪除標記會成為具有新 ID 的目前物件版本。

[![](/assets/images/圖片4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiU2-yv0dwx-jw7Q5RJtKceP102KmfQjeh60zUwq_a6u7db7y-yjsxTlq-UYtDDDDz-_3DRhRIQCoZoefZgl_gDf4uAeYVKZV2jIK9fw35dqyzvr0iTJm-_L4dqNCDY6ae_eT_qfiGnl5jJ3eWjNXP4kIDoIk9xb3Jo4ryAIEOxMZO8qhDUha035K5rMeot/s431/%E5%9C%96%E7%89%874.png)

  
  

若要永久刪除已使用版本控制的物件，您必須使用 DELETE Object versionId。

下圖顯示刪除所指定的物件版本會永久移除該物件

[![](/assets/images/圖片5.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggKbW6xxCi2XSiitnBCgFkQM6K0BdY_61JQ-xCsk_dmDFN30hQaFd5HKbWg-CHEFDI6wGKBVQ5dPA0k5BmTerur6EzDYqq6O33XVZWJm9pUn-FymtdyPpNnBlwXbrZZoihhTfMX0Xq91xICG3TjA8CfKxf1jyKHwzJ0YAhvwwY-nv79aKpDgUSUonvygi-/s453/%E5%9C%96%E7%89%875.png)

  

使用主控台刪除

1. 登入 AWS
   Management Console 並開啟 Amazon S3 主控台。
2. 在 **Buckets** (儲存貯體) 清單中，選擇包含該物件的儲存貯體名稱。
3. 在 **Objects** (物件) 清單中，選擇物件的名稱。
4. 選擇 **Versions** (版本)。

Amazon S3 會顯示該物件的所有版本。

5. 選取要永久刪除版本之 **Version
   ID** (版本 ID) 旁邊的核取方塊。
6. 選擇 **Delete** (刪除)。
7. 在 **Permanently
   delete objects? (****永久刪除物件？)** 中輸入 **permanently
   delete**。

四、取消刪除物件

如前所述，一般刪除是新增一個具有刪除標記得新版本，若要取消刪除則需要將具有刪除標記的版本移除。您必須在 DeleteObject versionId 要求中包含其版本 ID。

[![](/assets/images/圖片6.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmTjEc4_tPVM31W5G-5Uk1JxgOdZ4-8Izlobhah-n8EQUVV1Ooizs5UooL0MLISbUvEvq4O2sdGtaBw7oYcEt3YAOHgWgYRt5Oc1sALvndFvIP6riPSORgvWB5bqbME28m0Cjd-RrXLH7CM30Y8mcwrvf1vuT3k8dJ5FokqzcGxesNRCC2wO_DCf22Bqxv/s445/%E5%9C%96%E7%89%876.png)

  
  

 

如果您只使用 DeleteObject 請求，其中目前版本為刪除標記 (不指定刪除標記的版本 ID)，則 Amazon S3 不會刪去刪除標記，而是 PUTs 另一個刪除標記。

[![](/assets/images/圖片7.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWHv94IOG6p0Qdl_2Ov5R9hUBFMCnPx-L2BN9uIZ_jPQH2u4v0WolOLB4MHZsB2PtDpJJpHFLhYwmPjzbSEaYAIFxKkYgo_AFqyhPnFpyFs6wbzKJNktzTmgcwQINSge7hiOhuh2aNCOVoHZuMtDf2Qg10yU1eJpVAbmWW_L7GArOC0jKaUiO6g3NOUoIg/s410/%E5%9C%96%E7%89%877.png)

  
  

若要刪除具有 NULL 版本 ID 的刪除標記，必須在 DeleteObject 請求中作為

版本 ID 為 NULL。