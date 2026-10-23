# CGEO-MAP-AUD-004｜地形图缺失区事故与保守修复（v1.9）

日期：2026-10-23。状态：**高程全域工作图（非海陆分界图）**。

## 问题确认

1. v1.6/v1.7 地图错误地依据已渲染高程图的蓝色像素或色相判断为“海洋”，把低高程陆地误判为海洋。v1.8 的回退并未取得海陆分类掩膜，因此不能宣称已经恢复经验证的海岸线。
2. 在不同大小的预览中，曾将缩放后的图像坐标与原始图片像素坐标混淆。原始 CGEO-MAP-RES-005 双版本高程图实际大小为 **2170×930 像素**。原版地图绘图区为 (218,83)–(994,859)；《战帆》为 (1227,83)–(2003,859)。每个绘图区恰为 776×776 像素，分别映射到 0–848 与 0–1040 的游戏场景坐标。
3. 已从原始研究绘图裁切**两个完整绘图区**并在每个像素保留可视化的相对高程，没有执行任何根据 RGB 色相、高程阈值或导航面类别的海陆填充或土地删除。

## v1.9 工作图与下载

- [原版高程全域图](https://drive.google.com/file/d/1WBIJ2VOKQ6HntE4HQxdkj4PO2Tvibaju/view)
- [原版河流证据图](https://drive.google.com/file/d/1AK2EEBftTrtGwT7fIEdrMg0yvbEeZWuD/view)
- [《战帆》高程全域图](https://drive.google.com/file/d/1nfgyZ89szStr0PUnPD0MtwCrbAULYyDP/view)
- [《战帆》导航水域类型图](https://drive.google.com/file/d/1rztHFI1OdfcIkvUFav-uncAt2zHuwZGy/view)
- [完整工作包（四图、脚本、色阶底图、审计记录）](https://drive.google.com/file/d/1xYydTrMuPsp4xp5jXiwAqmOdm4G-rZef/view)
- [制图说明文档（Drive）](https://drive.google.com/file/d/1ydiR96F5aE-4gPDUy0xG3CrSkBmDas6d/view)

## 证据和方法边界

- **中性色高程图不是海陆分界图**。低值色带可同时包含海域和低地；中性色处理的目的仅是不因误判海域而掩盖地形证据。
- 由于当前工作环境只有 CGEO-MAP-RES-005 的已渲染图，本轮相对高程由原 Matplotlib terrain 颜色大致反解，不是原始 16-bit HGHT 数值；不得用于高程统计、地貌定量测算。
- 原版河流图叠加的是 RES-005 中的显式 river scene paths 与 PHYM 第 7 层，与天然水文连通的论证仍有距离。
- 《战帆》水域图保留 RES-006 的 Navmesh 分类，**不作为地形海陆掩膜**。
- 正式重新绘制深海、浅海、低地分区，仍须恢复两个版本独立且可验证的原始水面/海岸线几何。**在此之前不得以 v1.6、v1.7 或 v1.8 的海陆填色图作为论文正式地图。**

## 归档

- [Google Drive 地图资料夹](https://drive.google.com/drive/folders/1eJjV3BJr2AOS3N3_d-6lY8sQHOGSqPVT)
- 本档为 v1.9 事故审计与保守工作稿。旧版本应保留作修订历史但标注撤回；不得隐匿问题。
