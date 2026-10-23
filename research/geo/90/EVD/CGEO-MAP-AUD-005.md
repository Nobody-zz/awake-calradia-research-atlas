# CGEO-MAP-AUD-005｜海陆候选边界可辨性与地形保全审计（v2.0）

- 日期：2026-10-23
- 状态：**研究工作图；不是正式海陆分布图或已核验海岸线**
- [Google Drive 制图说明](https://drive.google.com/file/d/1FQxTfyVAcMZpBW6WnNPNXkT6fX0lRCPD/view)
- [v2.0 四图、两版掩膜、制图脚本及审计完整包](https://drive.google.com/file/d/1LM6o8TTAHVLzNggpL0GdIWItR_t12QG3/view)

## 修复的问题

此前 v1.6–v1.8 将宽泛蓝色色相或高程阈值作为海洋掩膜，错误遮盖低高程陆地；v1.9 撤销全部水面填色，使海陆不易读。本版从两个版本的原始高程可视化中独立抽取**与图边缘连通的严格平坦低值色块**，只为这一保守候选区绘制灰蓝填色、7源像素宽的候选区内侧浅蓝描带和深色界线。其他像素一律保留为相对高程色阶，既不归类为“陆地”，也不强行涂海。

## 数据与复核

- 原始双版高程分析图：`CGEO-MAP-RES-005_双版本同尺度高程图.png`，2170×930像素。
- 原版：裁切(218,83)–(994,859)，映射 0—848 场景单位，平坦低值众数RGB (40,72,174)，候选区域占源图像素 **20.59%**。
- 《战帆》：裁切(1227,83)–(2003,859)，映射 0—1040 场景单位，平坦低值众数RGB (45,61,163)，候选区域占源图像素 **32.64%**。
- 每个RGB通道仅容差±1，按四邻域连通、图框边缘连接且区域像素数至少30提取；不使用通用蓝色阈值，也不向非候选像素扩张。上述比例不是海洋面积比例。
- 地形阴影由已渲染Matplotlib `terrain` 色阶逆推作**相对可视化**，并非原始16位HGHT定量高程数据。

## 地图

1. [原版高程—外海候选界线](https://drive.google.com/file/d/1IGiI4QH-B4RVIc4o0v11zvPRH48V79bJ/view)
2. [原版水系—外海候选界线](https://drive.google.com/file/d/15_lj7An8q1kNaIPJhHaEBWP827ELHemN/view)
3. [《战帆》高程—外海候选界线](https://drive.google.com/file/d/10_PrwaakPz2ngtkX3MRbl5U7wYNPEM-x/view)
4. [《战帆》Navmesh水域分类（独立证据）](https://drive.google.com/file/d/1TDrVDdbXgaZKvqZaFWVIOJ6a6LQq5Hgv/view)

## 解释限制

图中外海候选界线 **不是官方海岸线、真实水深界限或校验过的海平面线**。候选区之外可以存在低地、湖泊、河流、浅海；不能把其他高程色阶直接认定为陆地。Navmesh导航水域面不是天然海陆掩膜，单独出图，不叠合生成假海岸。坐标与译名继续沿用各自研究档案，不能把候选XY解释升级成正式已核验坐标。

**后续必须取得原版与《战帆》各自的原始数值HGHT、可配准的水面/海岸几何，再绘制用于正式论文的海陆分布图。** 此次图件仅为避免“整片陆地被填成海水”且提高海陆候选区域辨识度的中间成果。


### CGEO-MAP-RES-015 · v2.1 外海候选区交叉校验（2026-10-23）

- [研究说明](geo/90/EVD/CGEO-MAP-RES-015.md)
- [对照图](https://drive.google.com/file/d/1QiGiWXozYRN_NOrergjFJKjpsFTSrzHy/view)
- [82 个城镇和港口坐标锚点表](https://drive.google.com/file/d/1UxQNIGfQaThaOztpfP9iuCco1UW-Rl7q/view)
- [全部可复核数据及脚本 ZIP](https://drive.google.com/file/d/1rgANNff1eAfpxxXgRxYiZ0DbGTrqj6Ye/view)

本次以《战帆》独立 Navmesh 分类复核 v2.0 的高程平坦低值外海候选区：候选区仅覆盖 43.1% 的可识别 OpenSea / CoastalSea 类别像素；另有 3.2% 可识别 Navmesh 陆面像素与候选区重合。近似图像配准有误差，但足以说明候选区不是经过核验的海岸线；原版53城镇、《战帆》29港口锚点均未落入外海候选区。继续保留分版本工作图，不使用候选区作海陆面积测算。


## CGEO-MAP-RES-016｜《战帆》港口与Navmesh图像配准核查（v2.2；2026-10-23）

- [学术审计说明](geo/90/EVD/CGEO-MAP-RES-016.md)
- [29港口逐点CSV](https://drive.google.com/file/d/1e8z29r9rZ0kaSmrYcpGReVAEAY3UQYa_/view)
- [清理后的独立Navmesh类别与港口QA地图](https://drive.google.com/file/d/1a47JBgqUn6NoufCyL-7EOJdhY0X2U8rl/view)
- [29港口最近同类水域颜色距离统计](https://drive.google.com/file/d/1sWPwUNSGtfZlfxYSVATk113dGxW2JAtc/view)

重要发现：RES-012 的 29 个港口候选 XY 与 RES-006 Navmesh渲染图回标后，仅1个直接匹配已有面类型颜色，18个落于图像导航陆面颜色；11个距离任意可辨导航水域色块超过20近似场景单位。**这只是跨图配准检验，不说明游戏原始网格有误。**在取得原始Navmesh顶点/面ID数据前，不可把该港口叠加图作为准确港口区位或海岸线证据。
