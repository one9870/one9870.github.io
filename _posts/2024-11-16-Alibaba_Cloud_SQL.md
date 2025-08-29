---
title: "阿里雲的雲端資料庫類型"
date: 2024-11-16 17:32:00
categories: ["阿里雲"]
tags: ["阿里雲", "教學30天上手"]
permalink: /posts/alibaba-cloud-sql/
---
**關聯式資料庫** (Relational
Database)  
在所有應用中都可以見到的資料庫應用，但是在套裝軟體或自行安裝建立資料庫的時候，常會遇到一些問題 :   
  
˙需要維護資料庫版本、作業系統的設定。  
˙當App、Database放在同伺服器，當伺服器發生障礙，會造成資料庫效能降低或是無法運行。  
˙定期備份、事故復原的手動成本較高。  
  
**關係型資料庫** (Relational
Database Service˙RDS)
  
阿里雲RDS 是一個完全託管式的資料庫工具，只需專注在資料庫的使用，不用擔心底層維護，只需要選擇好機器、硬碟的規格，後續阿里雲會直接幫助完成環境調校，資料庫搭建，同時提供備份、Log、監控報告等功能。  
  
以下是RDS實務操作  
(一)找到雲數據庫RDS並創建實例

[![](/assets/images/圖片1-4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGKwaXE1F4pGobiCO6K12lq70YsXA3OnHSlgwKHoxm8MJgYM-hSrRLs8Zyj2-Lokut4CtRSRpR-Pu7-7czrulo-Ri_IFqIbYbiytqyx2AGIZAw-w8xdxYnxZWNB-oVzoCOcScCRHI0sLBZOD9jjweYLwCjm6YnsDmxU68rqTRiy4YEL15yZRd-SeP2/s554/%E5%9C%96%E7%89%871.png)

  
(二)選擇資料庫版本和適合的規格需求  
  

[![](/assets/images/圖片2-3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkimDm2QK4rz3B6pYB9YxTumcXtRkJF3_GePqMkAi-b8AeglNn4nT0G1cngenuG7WHxAsSEFIEfaLm1FJo8AIOtOkIBUurCK7tPW4cQgX9JwicyaQoy3-sECzacJ7n_sFMFZFPnkHolZfXLoNPcyEauLC1imLrXnQfBsFEi6cEqIY5T6cwUhIkQn3T/s554/%E5%9C%96%E7%89%872.png)

  
  
(三)選擇主資料庫建立可用區位置，可選擇單一可用區佈署節省成本  
  

[![](/assets/images/圖片3-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXMML0xaldXYIqgjxXIXLuV-b7IeuwB86n7_tqk70bh-__1o2Ga_8GC2M_xncKQd-h9bDFOCLZcTGIp98NjXoob-BFCIfEADyfkaqQdUyceCM2z-mO_x4xN_6yIPju8gj-bogYoJaiAf8xfg2jc4MAmsCl5g0GR1hxHuqkSwtNSVYg-O2E1BnYI_XD/s554/%E5%9C%96%E7%89%873.png)

  
  
  
  
  
  
  
  
  
  
  
                                                                                                                                                                                                                                                                                                                        (四)選擇在先前選擇的地區預先建立好的VPC  
  

[![](/assets/images/圖片4-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgf2-dDpUCbdPJ8aZj1povt5iqAH78EgZB_bRsGUz01jYrSEOZ1BQRGGEZTJqJVNWkq2KyFdBBRVJNlJca4kBaWzQ2m5vP4Dnu4JcRQtzm8Opf5Yv99oiGn02rPETqhfAZd2ld5ZlKC-zaFOsMn8iGmh60TGbuFCl979y_xd62o0jPROgREDzfXvclg/s554/%E5%9C%96%E7%89%874.png)

  
  
  
  
                                                                                                                                                                                                                                                                                                                                                                                                                                   (五)確認訂單後，等待機器建立成功就完成資料庫實例建置了。  
  
  

[![](/assets/images/圖片5-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgX29GaicYv_-pWJXOvjGRBW7hkCQBPJteZLRE1unJMh9AEvXAO3VuyETnc3v-b5xZIVFSVBp1Cb6Co3ok46KRNaAX33hagP9jTCIOrycYQmn8iYr5LUXlDctPyUzVRRNryikPnHFsIidvQEYyGSzYqFWzDANehdpOlJM8-DXEEBoja9RwVGWM1WipO/s466/%E5%9C%96%E7%89%875.png)

[![](/assets/images/圖片6-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5FUab_4jykbbGNAOUvcmMAexAmXn-uRPrEspKfZwINttbitxP3EHbUnp2KX6xXnrVC77N2GhTJhP2PgDC7f06qdgn97bjnnM8b_1kffcx9KpO58NtnlsQNkJI4gtY3x40uV476KHT-nDyCLy4KwI-_bcJiQLMG1qkQ5TJh9_-jKc5C-L7nqZDzW3w/s554/%E5%9C%96%E7%89%876.png)

  