---
title: "Azure 申請提高網路配額"
date: 2024-11-29 16:17:00
categories: ["AZURE"]
tags: ["AZURE"]
permalink: /posts/azure-shen-qing-ti-gao-wang-lu-pei-e/
---
如果發現Public IP Addresses不足需要向Azure申請大量網路配額，花費的時間會依照申請配額的數量去做調整，假如申請配額數量高可能最多會花費兩個工作天。(如下圖

[![](/assets/images/圖片1-2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjaMrO7JWWYRvJiPMo1FF2PH8peZkSZ3dgYuxH-Jdr67xGIvn7P5YMvzeZxhGI_0uSzSdzwBXBaKgdfw8VmhYD3RHoCkJxns-ilajH2i-RYl0FlP8vEfwW6J3PvjGOe8Xdk9JH74-MBmT_63Cf3J09JhyVnlQSHAOa92CfpMOXfz5Ks_7Ck-AS8vqZ9/s554/%E5%9C%96%E7%89%871.png)

  
因為向Azure請求公共IP配額(如申請200個配額)，在申請過程中可能會遇到廠商詢問關於以下幾點問題 (如下圖  
  

[![](/assets/images/圖片2-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8nBwuqIh0NPxbAR7KKOlezPK1FY_F-XayEHbUwIPGrZQqMdGfzfHba8MQGDY6d6N1RBDjdDA1ALgAwZO4D4RHAFNQ03m7ab9foA6E332UJCFafbgjoUiN1YH-uB-o_OroBGdyONZ_wkJkQsRl-cu2Oadxu8c01XI9KdgGboAQatJWubzbUDrBTKSp/s554/%E5%9C%96%E7%89%872.png)

  
Q1 : 這是生產環境嗎？ （詳細解釋一下）  
Q2 : 如果是，影響程度如何？  
Q3 : 另外，您能否分享一下這可能對收入造成的影響程度？  
以下是上面問題的回答範例。  
  
Q1 :  
   
Yes,
this is a production environment. Our applications and services are hosted
here, and they are critical for our daily operations. The environment handles
real-time data processing, customer interactions, and other essential business
functions.  
  
Q2 :  
   
The
potential impact is significant as it could affect all users who rely on these
services. Currently,  active users, especially during peak hours, who may
experience disruptions if the change is not implemented smoothly.  
  
Q3 :   
  
Any disruption in this environment could have a substantial impact on our
revenue.  
  
Additionally, we kindly request that this process be expedited to minimize any
potential risks. Thank you for your prompt attention to this matter.  
-------------------------------------------------------------------------------------------------------------------------------  
  
如果情況緊急，請在回覆內容說明已經嚴重影響生產並請求廠商加快申請過程，另外詢問廠商是否可以將申請請求升級為 A 級案例，以確保其得到適當程度的關注，並告知廠商如果申請過程還需要協助的部分請馬上通知。  
  
註:避免申請時間拖太久，以40分鐘到1小時為單位詢問廠商目前進度。  
  
如果等待申請時間過長且情況非常緊急，詢問廠商是否能提供一部分的配額先使用，例如 :  本來申請200個配額改成先申請50個配額。 ，後續再慢慢補到200個。  
-------------------------------------------------------------------------------------------------------------------------------  

此外，將案例升級至A級，需要滿足一定的條件，廠商可能會再詢問以下幾點問題 (如下圖) ，依照圖片裡的問題，請詳細告知廠商此案例已經嚴重影響生產，並提供影響的持續時間。  
  
  

[![](/assets/images/螢幕擷取畫面 2024-11-30 080339.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgl5M4YBF_X9K8dv4EDeIwzBqOJYd4qqjhsKYZElVG-sLpGxMoh3_AfQRvFIlNU9k55scCtz80hHP-nzChFhVkdCeIxOEu7IzRrEBrVm1MIIBju6jZ9YDSIteu6sEyI7F-S4VXLDAmXPkyuAdhd9Zki1pVuqSLVgswpd0QnW_HhUp0GGHh7YCphu0R1/s1057/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-11-30%20080339.png)

  
  
Q1 : 有多少使用者和/或機器受到影響？   
Q2 : 該問題如何阻礙業務？  
Q3 : 財務影響是什麼？   
Q4: 問題發生在哪裡，生產還是測試？   
Q5: 該問題對生產環境造成了多少停機時間？   
Q6 : 問題是持續存在還是間歇性？ 

以下是上面問題的回答範例。  
  
Q1:  
  
The entire company's services are affected, impacting all users and associated machines.  
  
Q2:  
  
The service is currently unavailable, leading to a complete halt in our operations, significantly disrupting our business processes.  
  
Q3:  
  
The issue is causing a severe financial impact due to the inability to deliver our services, leading to potential revenue loss and operational delays.  
  
Q4:  
  
The issue is occurring in the production environment, directly affecting our live services.  
  
Q5:  
  
The production environment has experienced 24 hours of downtime, with ongoing disruptions.  
  
Q6:  
  
The issue is persistent and has not been resolved, continuously affecting our operations.

  

# **以上，是在申請的過程中可能會遇到的問題，文章中的回答僅供參考，請依據實際情況去做回答。** 參考資料 : <https://learn.microsoft.com/en-us/azure/batch/batch-quota-limit>