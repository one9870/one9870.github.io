---
title: "CSP類型的Azure訂用帳戶需開啟Cost Management相關權限才可看見預估費用Azure Cost"
date: 2025-01-02 22:38:00
categories: ["AZURE"]
tags: ["AZURE"]
permalink: /posts/csplei-xing-de-azureding-yong-zhang-hu-xu-kai-qi-cost-managementxiang-guan-quan-xian-cai-ke-kan-jian-yu-gu-fei-yong-azure-cost/
---
# **CSP****類型的Azure訂用帳戶需開啟Cost Management相關權限才可看見預估費用**

## Azure Cost Management是Azure所提供的一套雲端成本控制和優化工具，重點在幫助用戶們有效管理在Azure平台上的支出。其中的功能包含了費用監控、預算管理、成本預測各個方面，可以讓用戶更好了解資源使用情況並進行優化調整。

## 而在建立新的虛擬機器時，Azure 入口網站會根據所選的配置（如 VM 大小、地區、作業系統等）即時顯示每月的預估成本(即 緊隨支隨付的帳戶才會估算顯示出費用)。 通常每月預估成本並不需要啟用到Cost Management，但可能受限於訂用帳戶類型和原則設定，例如: CSP類型的Azure訂用帳戶……等，因此，會需要開啟Cost Management功能，並且除相關限制，才可顯示預估費用。 // 上圖為以CSP類型的Azure訂用帳戶為例 >>>有開啟Cost Management // 上圖為以CSP類型的Azure訂用帳戶為例 >>>無開啟Cost Management 參考資料: 估計在 Azure 入口網站 中建立虛擬機的成本 （預覽） <https://learn.microsoft.com/zh-tw/azure/virtual-machines/estimated-vm-create-cost-card?utm_source=chatgpt.com>