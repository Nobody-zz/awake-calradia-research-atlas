# CGEO-MAP-RES-018｜原始地图资源可恢复性与《战帆》港口衍生几何复审

版本：v1.1；复核日期：2026-10-24。性质：原始资源可恢复性检查与衍生数据复算；**不构成原始地图二进制重解析或正式海岸线测绘**。

- [Google Docs v1.1（本轮复核正文）](https://docs.google.com/document/d/1DAC0wDXLP0tantGCQo522EUF3v1AQXS-yztADc43miU/edit)
- [RES-012 派生分析 ZIP](https://drive.google.com/file/d/1GMG8gXe70m376txGvIcZH0lQrSz5552G/view)
- [RES-018 资源追溯复核 ZIP](https://drive.google.com/file/d/1buCN7S784RaduPZnJVfcaYifGDBOP-s8/view)

## 第一、第二手数据分级

CGEO-MAP-RES-001 曾直接读取原版和《战帆》的 scene.xscene / terrain.bin / navmesh.bin；其原始字节数、SHA-256 见[原始资产资源清单](https://docs.google.com/document/d/1RchZ3Q87ii5CmrIkqJjl8IDFG-ZTe8jAsJOcpEnXB0s/edit)。RES-003 从 terrain.bin 恢复两套 4097×4097 16-bit HGHT 栅格；RES-008 从原始 Navmesh 多边形核验《战帆》29/29 港口和144/144登陆标记位于候选可航面。这些属于**已归档的前序直接分析**，本轮未再次读取这些二进制原件，不能写作已复算。

本轮重新读取当前可访问的 `CGEO-MAP-RES-012_港口村庄导航网络复核数据.zip`，ZIP CRC通过；其中有 `navmesh_reference.py`、`town_port_network_access.csv`、`summary.json`、网络距离表等八项派生研究文件，**不包含完整 navmesh 顶点、面或原始 bin 字节**。对照原 CSV 和 summary.json，29 条城镇港口记录全部可读，CoastalSea(18) 23 条、River(11) 6 条；这一核对是针对保留的派生数据，不是再次执行多边形包含测试。

## 港口空间统计（仅描述保留的派生表）

CoastalSea 类港口场景 Z 中位数2.580，范围2.5698—3.327；其中20/23位于2.569—2.581。River 类六港口 Z 中位数5.736，范围3.885—9.996。River 父级ID：town_A7、town_ES3、town_EW1、town_EW6、town_N4、town_V3。上述Z是场景标记候选坐标，不能直接断言自然地理海拔、水面高度差或河床坡度。前序重心图距离是路径代理，非实际航程。

## 仓库与云盘存储核查

已检查 GitHub `Nobody-zz/AWAKE` 与 `Nobody-zz/awake-calradia-research-atlas` 的可见分支及文件树；研究库实际保存文本报告与校验清单，并明确说明不上传游戏版权二进制。Google Drive 的 `NavalDLC.zip` 是官方文本XML摘录，不能作为 Main_map 二进制镜像。Google Drive 保存 RES-001—017 研究档案及中间图表，不等于保存可再下载的 scene/terrain/navmesh 原件。项目早期直接读取过的原件是否仍在旧附件其他存储层，尚未确证；不能说用户从未上传，也不能说本轮已经找回。

## 恢复路线

1. 恢复二进制原件后先逐一验证大小与 RES-001 的 SHA-256（前序指纹，本轮未重测）。
2. 调用已保存的 `navmesh_reference.py` 从原始 RNM1/NMG9 重建全部顶点、面和地形/水域类，并以官方港口场景标记重新做点在多边形核验；拒用 PNG 像素分类替代几何。
3. 对原版与《战帆》分别恢复完整16-bit HGHT 栅格，整合独立解析的场景 water_plane/真实水域边界；导航可航区域并非精确天然海岸线。
4. 正式地图只有在陆海掩膜来自可靠源几何、并对低洼陆地与岛屿进行独立验证之后才可发布。v1.6—v1.8 错误陆海填色不复用，v2.0 海水候选色块仍属于猜测。

## 关联原件与边界

- [RES-001 原始资源指纹](https://docs.google.com/document/d/1RchZ3Q87ii5CmrIkqJjl8IDFG-ZTe8jAsJOcpEnXB0s/edit)
- [RES-003 16-bit 高程图块解析](https://docs.google.com/document/d/1pTiVx_yOJpP6IVFzUcwr2Yeni3m2xb1Y-rbdcNj9HsM/edit)
- [RES-008 港口原始网格核验](https://docs.google.com/document/d/1aL-g-FRDguFHEAFbMZ2ypz5uWMIEcHXnd3HS5mmMYVw/edit)
- [RES-012 留存港口与导航数据 ZIP](https://drive.google.com/file/d/1GMG8gXe70m376txGvIcZH0lQrSz5552G/view)

本条记录是研究证据链恢复，不声明已找到全部地图二进制；不得以此报告推断任何实际海岸线细节。

## 补充交叉命题：CoastalSea 港口标记与主水面实体高度接近

RES-001 的《战帆》主 `water_plane` 实体中心Z是 **2.570** 场景单位。RES-012 当前重新读取的 23 条 CoastalSea(18) 港口中，20条港口功能标记 Z 处于 **2.569—2.581**（距该实体中心Z约0.011以内），其余3条为2.688、2.711、3.327。相比之下，六条 River(11) 港口Z范围为3.885—9.996，中位数5.736。这个独立来源的高度对应支持“沿海港口的标记经常依据主水面参考高度布设”的**待验证机制假说**，而不是海平面标定证据；严禁将Z=2.570当作陆海阈值或真实水位。

## 本次可下载的审计文件

- [Google Drive 完整复核包：报告、29港口CSV、8项原件指纹表与复核JSON](https://drive.google.com/file/d/1buCN7S784RaduPZnJVfcaYifGDBOP-s8/view)
- [Google Drive Markdown 完整论文](https://drive.google.com/file/d/1alwdPxpAiQJptm8jN38nl2FPWjE4qKRX/view)

这些新增文件是衍生研究报告和表格，**不包含游戏原始版权二进制**。


## v1.1｜精确归档校验与模板变量勘误（2026-10-24）

本轮通过已知 Drive 链接重新取回 RES-012 ZIP，重新计算 SHA-256 为 `9bca8d83d9b814c3722c88ee89b50f57fccf01957a4e4729f1055279c6f930c3`，文件大小 579,804 字节，ZIP CRC 通过。RES-018 资源追溯包重新取回后，SHA-256 为 `0362b8290e40def44bdff926b7d1410b19e34d346b92cddb1ced272a02667619`，大小 7,845 字节，ZIP CRC 通过。两者均为派生资料包，不含原始地图二进制。

从 `town_port_network_access.csv` 复算的 CoastalSea 标记 Z 中位数 2.580、范围 2.5698–3.327，20/23 位于 2.569–2.581；River 标记 Z 中位数 5.736、范围 3.885–9.996。72个村庄父级中，56个直线最近港口与网络代理最近港口一致，16个不一致；28对双状态标记 XY 完全重合，44对非零间距，最大 0.63712 场景单位。以上基本计数均与 `summary.json` 一致。它们仍是既有派生数据的重新计算，不是原始 Navmesh 的再解析。

**模板变量勘误：** RES-018 ZIP 内嵌的 Markdown 副本在若干统计位置保留了未替换的模板表达式（例如 `{meta['input_bundle_sha256']}`）。该副本的相关数字行不应直接引用；本 v1.1 以 ZIP 实际字节、JSON 和 CSV 复核后列出确定数值。请优先引用本版报告与 Google Docs v1.1。

本轮再次检查了当前对话附件、Library 的 `Calradia Geography Research Source Files` 及 Drive 精确文件名检索结果，仍未取回原版或《战帆》的 `scene.xscene`、`terrain.bin`、`navmesh.bin`、`river_triangles.bin` 或 `flowmap.dds`。RES-001 中的原始 SHA-256 仍为前序历史指纹，本轮没有原件可供重算。这个结论仅限当前可访问范围，不代表原件从未上传或不存在于其他旧附件/存储层。

**对地理研究的处理：** 达玛尔河等地点的官方文本证据可继续研究，但“聚落坐标—真实河道几何—高程”的同版本配准仍待核；不以港口候选坐标或渲染 PNG 推定正式海岸线、河岸线、河口位置或完整水系拓扑。
