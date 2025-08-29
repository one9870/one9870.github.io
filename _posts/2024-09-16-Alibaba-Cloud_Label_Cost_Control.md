---
title: "在阿里雲上使用標籤功能控管成本"
date: 2024-09-16 06:54:00
categories: ["阿里雲"]
tags: ["阿里雲", "標籤", "成本", "控管"]
permalink: /posts/alibaba-cloud-label-cost-control/
---
在阿里雲上使用標籤功能控管成本

 

1.登陸標籤控制台<https://resourcemanager.console.aliyun.com/tags?spm=a2c4g.11186623.0.0.45854457Q8FwVl>

2.在自定義標籤頁面中，創建自定義標籤

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiD0V5jCOlpslashM9LbvBMJW_LRscaJF7zhFjaVmdjBs8fZ_MhLs8nAuOs5qxSmmQfvEYwPAdy3nem0YFscRaat0SHXC1A316vQg8vB9HgLjjf677AgN02vx4zWNo2hGMckKYdO5jhaEApUkhA8-JyU89vJBueWvxl-tf2NqqPTG_VjoTOQpazKxcT7Sk=w495-h391)](https://blogger.googleusercontent.com/img/a/AVvXsEiD0V5jCOlpslashM9LbvBMJW_LRscaJF7zhFjaVmdjBs8fZ_MhLs8nAuOs5qxSmmQfvEYwPAdy3nem0YFscRaat0SHXC1A316vQg8vB9HgLjjf677AgN02vx4zWNo2hGMckKYdO5jhaEApUkhA8-JyU89vJBueWvxl-tf2NqqPTG_VjoTOQpazKxcT7Sk)

  
  

3.可以依照成本中心、部門、項目等標籤對資源進行分類

標籤鍵:為必填項目，選擇已有標籤鍵或輸入新標籤鍵，支援前綴模糊搜 索，一次最多選擇或輸入10個標籤鍵。

標籤值:為選填項目，選擇已有標籤值或輸入新標籤值。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjKAuT2L8dqKfWxoMOL6nluElAsmteBliCphNnlK4gi9_f2M4zauCbCk58ymOKBZlUu8Ne-KoBmWdZtwriG9ILtSRMX69gyBapMMfPGiHsnpAJ3b5TgifjV8-PwCwhogjv9GoY4RdlFFJIWHxuqTbsj4p5KqdTD9TFp2-Eci01qMP4VckGkujc5cqkWQhY=w610-h299)](https://blogger.googleusercontent.com/img/a/AVvXsEjKAuT2L8dqKfWxoMOL6nluElAsmteBliCphNnlK4gi9_f2M4zauCbCk58ymOKBZlUu8Ne-KoBmWdZtwriG9ILtSRMX69gyBapMMfPGiHsnpAJ3b5TgifjV8-PwCwhogjv9GoY4RdlFFJIWHxuqTbsj4p5KqdTD9TFp2-Eci01qMP4VckGkujc5cqkWQhY)

4.
輸入完成後點選下一步，並選擇需要綁定標籤的ECS實例，可以依照不同方式選擇資源。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgsH4fRcCYZ24N6atdwjQA4sq-DnAXFd51PMyJodE4_S513uwQfbI2j2sTB0f9_CCUZHHObJtQ_3iWBVF-pFh8s7YJHVWcE7XC5L47MOQn2RLJ5N4nshuB9Sjsp1fui979HKdgiw9OSWxBflhWaCSQQ_2hX7Ufj2ajT3lDsdmB4Ch8wVtVtk6dgDeNF2RE=w496-h217)](https://blogger.googleusercontent.com/img/a/AVvXsEgsH4fRcCYZ24N6atdwjQA4sq-DnAXFd51PMyJodE4_S513uwQfbI2j2sTB0f9_CCUZHHObJtQ_3iWBVF-pFh8s7YJHVWcE7XC5L47MOQn2RLJ5N4nshuB9Sjsp1fui979HKdgiw9OSWxBflhWaCSQQ_2hX7Ufj2ajT3lDsdmB4Ch8wVtVtk6dgDeNF2RE)

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjrMHAl831ZlEo4sz8GUjb3FfYESXSDbdsY-p03xH8htnOUHHlxvPdA8CaMuPCj3befbkzQMJSLYg9A4zYMpkSvVJ0KciRMwN8zXC-65MOFhSfpdku1Vqfx8GbjQIn0kjvvhqxKYtGoaqrwaXUdqVHMMEN_WonKuMKJGaAg5DhqK3o8CZdUtPfoi9X6Cvc=w500-h250)](https://blogger.googleusercontent.com/img/a/AVvXsEjrMHAl831ZlEo4sz8GUjb3FfYESXSDbdsY-p03xH8htnOUHHlxvPdA8CaMuPCj3befbkzQMJSLYg9A4zYMpkSvVJ0KciRMwN8zXC-65MOFhSfpdku1Vqfx8GbjQIn0kjvvhqxKYtGoaqrwaXUdqVHMMEN_WonKuMKJGaAg5DhqK3o8CZdUtPfoi9X6Cvc)

  
  

5. 在ECS控制台查看ECS實例是否有成功绑定標籤。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEijHP050TQNlNnLHP9nzjF8-m-55oN1XGuEyXns9LGOENmtHDWW_ESAS4Xd61LouyZP91QYYA-NsiVau5SIy1LDGwLY6MzxPZcIqjkfvb6UPjRQTjtZUj_qh2e9wWz4B6oRGF9eTICbIf2ExuK9vQAswvoQO6pqQcUa17JrKVavyBmUvQtWqDwqUI26zX8=w595-h82)](https://blogger.googleusercontent.com/img/a/AVvXsEijHP050TQNlNnLHP9nzjF8-m-55oN1XGuEyXns9LGOENmtHDWW_ESAS4Xd61LouyZP91QYYA-NsiVau5SIy1LDGwLY6MzxPZcIqjkfvb6UPjRQTjtZUj_qh2e9wWz4B6oRGF9eTICbIf2ExuK9vQAswvoQO6pqQcUa17JrKVavyBmUvQtWqDwqUI26zX8)

6.確認完成後點選首頁右上角的費用，並選擇費用與成本，進來後選擇分帳管理->費用標籤

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj6PJyOQIF-ReohPELFO4tft0bVGdBs4xNCAM-Fo51GMVdIQxR3SuspdglBGcx2PBoaE6scIR_5z3BRoa1y4yiYVzpSw61QvrPwdJbonfR-Pokg0oHKzc9TF8wnC3Ebeqq61HQnlZKa4paepYwjdP7c97QnIAhUDiH-2LF4YG1UnqLsYkbGyUFpeKxM9vo=w603-h311)](https://blogger.googleusercontent.com/img/a/AVvXsEj6PJyOQIF-ReohPELFO4tft0bVGdBs4xNCAM-Fo51GMVdIQxR3SuspdglBGcx2PBoaE6scIR_5z3BRoa1y4yiYVzpSw61QvrPwdJbonfR-Pokg0oHKzc9TF8wnC3Ebeqq61HQnlZKa4paepYwjdP7c97QnIAhUDiH-2LF4YG1UnqLsYkbGyUFpeKxM9vo)

  
  

 

7.選擇要啟用費用標籤的標籤名稱，選擇完成後會出現在右方已選擇啟用的標
籤中，點選啟用。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiMeSYGXwhJnJxv48-ET5eBNVa6VR7-IoElm_zc1JdaV7WqoQwuVF-JYNSGOffmjS1IO-wxXKKAjmpwy327g6eLwiJDDn62LYYo5AuJbS0PJWaJFnYvZ8Mgl7TVQsJy2m7F33jXBXFysZuqFIR0DMBE6gA5Z5R4u9LRPTj-6H3h_0j_UCKe5m3UoA5Yu2k=w633-h273)](https://blogger.googleusercontent.com/img/a/AVvXsEiMeSYGXwhJnJxv48-ET5eBNVa6VR7-IoElm_zc1JdaV7WqoQwuVF-JYNSGOffmjS1IO-wxXKKAjmpwy327g6eLwiJDDn62LYYo5AuJbS0PJWaJFnYvZ8Mgl7TVQsJy2m7F33jXBXFysZuqFIR0DMBE6gA5Z5R4u9LRPTj-6H3h_0j_UCKe5m3UoA5Yu2k)

  

8.回到首頁，右上角選擇費用->費用與成本->成本管理->成本分析

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiPJFKW1J6Ln2MzZew7cq4gxpaQry6lWqdjEkRCwI6WNGlngJUDSODcmoN0IxgozdYHpEnC6q-HaSs9uh-OABUTNbu_fkpTm52stOp0tUeFvYuuv8ii2jBt4_ngiU4mPhSADVZEILORN8ZKt931f2hLqM5yuJsGUe4NzdOO3FECS0KAmuDF3slw98hzNRc=w590-h342)](https://blogger.googleusercontent.com/img/a/AVvXsEiPJFKW1J6Ln2MzZew7cq4gxpaQry6lWqdjEkRCwI6WNGlngJUDSODcmoN0IxgozdYHpEnC6q-HaSs9uh-OABUTNbu_fkpTm52stOp0tUeFvYuuv8ii2jBt4_ngiU4mPhSADVZEILORN8ZKt931f2hLqM5yuJsGUe4NzdOO3FECS0KAmuDF3slw98hzNRc)

  
  

9. 設定篩選條件，查看費用資訊

在分類維度下拉清單中，選擇實例標籤，接著在標籤鍵下拉的清單中，選擇欲察看的自定義標籤。時間粒度範圍選擇月，並且設定開始和結束的時間段，最多不超過12個月，便可以查看該自定義標籤的費用支出狀況。

 

查看指定項目（project）的費用支出狀況

在右側篩選條件區域，按一下標籤，接著選擇標籤，例如：選擇標籤A，便能夠查詢項目A的費用支出狀況。並且支援選擇多個標籤，能夠查看多個標籤之間的費用關聯。

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhfYVMAfyzI5iGv3aH7MNj3YbJyC9gZr3w44Hu6rcGuHbONRtdUpGUNAWXjA4S6NwiE1jaU6ZfMKwqSgyLzUawjKCwFtAdZpm5bR2j38LJ8SyF1h_-MebcVcOGde9Q8FcuOGWZwWgZKYL-6ZJjl3E2UhKMuBMDBb05S038bt2MJhEYLaTpxwCq9S93uao4=w617-h276)](https://blogger.googleusercontent.com/img/a/AVvXsEhfYVMAfyzI5iGv3aH7MNj3YbJyC9gZr3w44Hu6rcGuHbONRtdUpGUNAWXjA4S6NwiE1jaU6ZfMKwqSgyLzUawjKCwFtAdZpm5bR2j38LJ8SyF1h_-MebcVcOGde9Q8FcuOGWZwWgZKYL-6ZJjl3E2UhKMuBMDBb05S038bt2MJhEYLaTpxwCq9S93uao4)

  
  

參考資料: <https://help.aliyun.com/zh/resource-management/use-cases/use-tags-to-allocate-costs>

<https://help.aliyun.com/zh/resource-management/use-cases/use-tags-to-allocate-costs-for-instance-based-services>

 