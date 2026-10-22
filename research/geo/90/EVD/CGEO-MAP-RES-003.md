# CGEO-MAP-RES-003｜原版与《战帆》地形高程图块解码与拼接

- 日期：2026-10-22
- 版本：v1.0
- Google Drive 原件：[技术报告](https://docs.google.com/document/d/1pTiVx_yOJpP6IVFzUcwr2Yeni3m2xb1Y-rbdcNj9HsM/edit)
- 高程图对照：[Drive PNG](https://drive.google.com/file/d/1M84hDSPf-FqdxBAGj9FSMbHQft9P_6ZR/view)
- MIDX 与高程总览：[Drive PNG](https://drive.google.com/file/d/1GWUaZhTGMFB-m79wjfiO_NWCNm4eg8B1/view)
- 原版接缝差异：[CSV](https://drive.google.com/file/d/1rW2WVjRriCfZ941MMs_T0XMEBuOVD9bE/view)
- 《战帆》接缝差异：[CSV](https://drive.google.com/file/d/1rKeuFjbzcsucd5POpawSkXmayo1qBKPL/view)

## 结论

原版与《战帆》的 `terrain.bin` 的 HGHT 高程图块已完整解码。每版256张16-bit灰度PNG，每张257×257像素；按16×16排列并去除共享内部边界后得到4097×4097高程栅格。DLC的480条相邻接缝全部逐像素匹配；原版480条中477条完全匹配，另外3条只有有限差异。

## 格式解析

- 外层格式：`ZGR6RTRN`，版本2。
- MIDX、HGHT、PHYM的内部数据使用40字节封装头，随后为LZ4 raw block；解压输出长度与各分块声明的 raw size 一致。
- HGHT、PHYM的分块开头另有1024字节、256项uint32偏移表。偏移表指向解压后的raw输出，而非存储文件中的压缩字节。
- HGHT每个偏移分段以4字节PNG长度字段开始；长度字段与其后PNG字节数、相邻偏移边界完全匹配。
- MIDX解压后为4组“4字节长度 + PNG”序列；四张均为4096×4096、8-bit灰度图，序列恰好覆盖整个解压输出。
- PHYM解压为67,642,368字节，正好是256×264,228字节。264,228 = 32 + 257×257×4，提示可能存在32字节tile头和四通道257×257栅格，但通道语义未确认。

## HGHT结果

| 指标 | 原版 | 《战帆》 |
|---|---:|---:|
| 原始文件 SHA-256 | `3b583d9ff5504a6c871caa466a14654593bee42c27df3e3316eda6cb4d85ab49` | `56c3a0663fb2bf8404210772e187dcd707eb64d8b7e9b5496dfb509bdc3ea9fd` |
| 解压后字节数 | 17,862,043 | 14,684,844 |
| 高程图块 | 256 | 256 |
| 单块尺寸/位深 | 257×257 / 16-bit灰度 | 257×257 / 16-bit灰度 |
| 拼接栅格 | 4097×4097 | 4097×4097 |
| 样本最小值 | 3 | 0 |
| 样本最大值 | 65535 | 65535 |
| 样本均值 | 14974.173 | 12714.518 |
| 样本标准差 | 11685.203 | 12362.420 |
| 完全匹配的水平接缝 | 238/240 | 240/240 |
| 完全匹配的垂直接缝 | 239/240 | 240/240 |

原版仅3条接缝不完全一致：tile 134/135水平边界11像素差异、最大差3；tile 150/151水平边界4像素差异、最大差1；tile 61/77垂直边界5像素差异、最大差12。保留原值，不做平滑修补。

## 修订旧统计

CGEO-MAP-RES-002曾把偏移表当作存储字节偏移，并以 stored size 作为最后一块终点。现在确认偏移表指向解压后的raw数据，因此最后一块终点必须使用 raw size。修订后的图块片段统计：

| 指标 | 原版 | 《战帆》 |
|---|---:|---:|
| 最小字节数 | 724 | 723 |
| 中位数 | 87,689.5 | 78,176.5 |
| 均值 | 69,773.6 | 57,362.7 |
| 最大字节数 | 97,184 | 96,687 |
| 不超过2000字节的块 | 29 | 47 |
| 最后一块 | 65,403 | 81,002 |

完整修订表为本地分析包中的 `terrain_hght_tile_sizes_corrected.csv`。

## 解释边界

16-bit样本已恢复，但样本到场景Z高度的转换函数和X/Y轴方向尚未校准。node_size原版为53、DLC为65场景单位，因此这些图可以用于形态识读，不能直接把灰度当作米，也不能把两版差异自动解释为卡拉迪亚世界内部自然地貌变化。MIDX四图与PHYM通道含义仍待shader/terrain layer绑定证据确认。

## 交付物

- `original_height_mosaic_4097.png`、`warsails_height_mosaic_4097.png`：4097×4097、16-bit高程栅格
- `heightmap_dual_version_stretched.png`：双版本逐版拉伸预览
- `terrain_decode_montage.png`：MIDX四图与高程预览总览
- `terrain_hght_tile_sizes_corrected.csv`：修订后的图块长度表
- `terrain_height_decode_report.json`、`terrain_midx_image_manifest.csv`
- `original_height_tile_manifest.csv`、`warsails_height_tile_manifest.csv`
- `original_height_seam_mismatches.csv`、`warsails_height_seam_mismatches.csv`

研究快照只提交本报告和必要统计，不向GitHub提交游戏原始二进制资产或完整提取图块。
