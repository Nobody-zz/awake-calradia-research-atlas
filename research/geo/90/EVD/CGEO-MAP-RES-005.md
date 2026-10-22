# CGEO-MAP-RES-005｜双版本共同高程尺度、PHYM季节图层及原版河流路径校验

CGEO技术成果·v1.0·2026-10-22

## 研究摘要

本轮直接读取项目中已保存的原版与《战帆》Main_map原始文件，而非仅利用此前的报告或公开截图。研究以CGEO-MAP-RES-003已恢复的两张4097×4097、16-bit HGHT栅格为基础，按各自scene.xscene的min_height/max_height转换为场景Z单位，采用共同的−1至30场景Z色标绘制双版本地形图；同时逐块解码两版PHYM季节layer index，并与scene.xscene的terrain/layers定义直接对应。原版另将PHYM第7层“river”的空间分布同以river开头的场景Paths河流线路叠加，并进行系统抽样检验。

主要发现：两版PHYM各自包含256块、每块四季、每季257×257个图层索引；全部样本索引均落在该版scene.xscene定义的层数范围内。两版夏、秋、冬、春的PHYM层索引在各自地图上逐像素完全相同，但并不能推出世界内部没有季节差异。原版8个terrain layer，8个在PHYM中均出现；《战帆》7个terrain layer，PHYM仅使用其中5个，其中index 0和4未出现。原版PHYM中名为river的第7层约占单季所有图块记录的1.821%，且原版10条以river开头的场景路径中，2,019个插值采样点的98.86%距离该图层不超过3场景单位。与等量随机背景采样相比具有强烈空间对应性。

## 一、原始文件、版本与处理流程

原版数据：/mnt/data/original/scene.xscene、terrain.bin，以及原版已解码的original_height_mosaic_4097.png。战帆数据：/mnt/data/warsails/scene.xscene、terrain.bin，以及warsails_height_mosaic_4097.png。两版terrain.bin的SHA-256分别为3b583d9ff5504a6c871caa466a14654593bee42c27df3e3316eda6cb4d85ab49与56c3a0663fb2bf8404210772e187dcd707eb64d8b7e9b5496dfb509bdc3ea9fd，与CGEO-MAP-RES-001登记一致。

两个4097×4097 HGHT栅格均为16-bit无符号数。按CGEO-MAP-RES-004确认的编码公式：Z=scene_min_height+v×(scene_max_height−scene_min_height)/65535。原版min/max为−0.723/23.052，地形覆盖16×53=848场景单位见方；《战帆》为−0.900/29.109，覆盖16×65=1040场景单位见方。使用−1至30场景Z单位的统一色标，保留各自独立的场景X/Y轴，不对图像做虚假的逐像素同址对照。场景单位尚未校准到现实长度/海拔。

PHYM按ZGR6RTRN目录定位：先读取256项uint32偏移表，再解码40字节内部封装头之后的LZ4 raw block；每块分成夏秋冬春四组记录，每组8字节字段头加257×257个uint8图层索引。season值依次0、1、2、3；count均为66049。索引存储是X-major，绘图时转置成以行对应+Y、列对应+X的栅格，并在拼接时舍弃共享边缘的重复样本。图层标签来自当前版本scene.xscene的terrain/layers/layer，不能跨版本按同一编号自动认定其自然属性相同。

## 二、共同高程色标的地形观察

两版统一Z色标的原始高程图分别呈现相对低平区、山地高值区、中央起伏地域及较明显的水陆分界式图像形态。由于两版空间范围不同，此处不以同一像素行列直接对比地物位置，更不据图像差异推断卡拉迪亚世界内部发生了海侵、造岛或地形抬升。

高程栅格分位数（场景Z单位）：原版最小−0.7219、10百分位0.0040、中位数4.4786、90百分位10.5106、最大23.0520；《战帆》最小−0.9000、10百分位−0.4004、中位数4.1191、90百分位13.0813、最大29.1090。这里统计的是整个矩形场景栅格的高度值，不是陆地高程分布；海面以下、未展示的远海地表、空白区域及极低平面样本均可能纳入分位数，因此不应把两个中位数直接解释为“大陆平均海拔”的变化。

预览图：https://drive.google.com/file/d/1ymJeiisRuBnoAnd3V3y6Hf46ddFIqLeS/view 。分析使用的转换代码与中间结果保留在本地分析环境，不修改用户游戏文件。

## 三、PHYM季节索引及图层定义

原版scene.xscene共8个terrain layer（按索引顺序）：0 default、1 flora_forest、2 rock、3 grass、4 dirt、5 dirt2、6 forest2、7 river。原版单季PHYM记录中，上述8种索引全部出现；各类约占全部记录的47.177%、0.001%、10.904%、18.730%、10.098%、7.536%、3.734%、1.821%。这里的百分比按每个257×257 tile的全部记录计算，包含相邻tile重复边界，不等于经过实地调查的自然土地覆盖比例。

《战帆》共7个terrain layer：0 default、1 default_1、2 rock、3 grass、4 dirt、5 dirt2、6 forest。其PHYM单季实际只出现索引1、2、3、5、6，比例分别约37.317%、10.077%、16.712%、35.328%、0.566%；索引0和4在PHYM记录中完全未出现。这反映当前NavalDLC地图的PHYM图层选用情况，但不等于渲染层或自然地理景观中不存在相应外观。

两版4个季节的PHYM记录均逐像素完全相同，夏—秋、夏—冬、夏—春的差异样本数均为0（每版按去重后的4096×4096样本栅格验证）。不能把这一结果推广为全年地表外观完全相同、全年不下雪或官方世界没有季节性；其他材质、动态天气与环境表现资源仍可能在此之外发挥作用。

材料绑定方面，原版“river”地形层夏季physics_material属性为soil；这也说明名称、物理材质标签与真实自然河道并不一一等价。另如原版“dirt”夏季physics_material文本为burning_jar_small，属于直接读取的配置异常/特殊标记，不能据名称造出任何自然地理解释。《战帆》rock等若干层夏季physics_material标注为soil，而原版rock是stone；它们是资源配置差异，不是自然岩石的地质学分类。

图像：https://drive.google.com/file/d/1R1iQz7c7tkFaAfCP7ITV6ds8zV9jbFC-/view 。

## 四、原版河流路径与PHYM第7层的空间符合程度

原版scene.xscene中的Paths容器包含20条路径；本轮仅选择其中名称以river开头的10条路径，避免把tigris、volga等内部标识未经验证就纳入同一命名组。根据相邻控制点进行线性插值，约每0.75场景单位生成一个采样点，总计2019个。将点投到PHYM夏季第7层的1/4分辨率栅格（约0.828场景单位/像素），用欧氏距离变换测量距最近layer-7像素的距离。这是路径/索引对应性检验，不是精确河面边界测量。

结果：2019个河流路径采样点中，91.83%距第7层不超过1场景单位，98.86%不超过3单位，99.41%不超过8单位。随机对照：在整张地图范围均匀抽取2019个点，相应比例约2.33%、4.71%、9.21%。更保守的背景检验把随机点限制在这10条路径的整体X/Y包围盒（X≈87.26—573.38，Y≈255.84—535.89），3单位内比例约11.34%，仍远低于河流路径的98.86%。抽样均使用固定随机种子20261022，仅用于描述性空间比较；相邻线性插值点并不独立，因此不据此计算伪独立样本显著性。

按路径分组时，10条河流路径距离layer-7不超过3单位的比例中，最低为river_emp_north的90.0%，其余9条全部至少98.6%。这一结果有力支持原版河流Paths与terrain中的river图层共同服务于河道表示，提示了直接利用场景路径定位原版河道的可行性。然而PHYM是地形物理层索引，不是完整的河流水面；不能直接把第7层的边缘当作河岸线，也不能由场景路径记录顺序推出真实水流方向。

图像：https://drive.google.com/file/d/1krIsrLA4fG5wkbVvjlQ8O0fH6HCvjAtP/view 。

## 五、跨版本研究的意义及限制

原版有river第7层，《战帆》没有同名图层；但两版仍有明显水体/河流表达，且DLC保留river_generator与独立river_triangles.bin、flowmap.dds。故合理的结论只是河道相关资源的实现方式及layer schema存在差异，不是《战帆》删除了自然河流，也不能把游戏文件变迁写成卡拉迪亚历史时期的河流消亡。

同时，原版terrain.node_size=53，DLC=65，两个场景的物理范围不同。任何比较真正的河谷位置、湖岸、水系连通性、山地屏障或分水岭，都必须先建立地物级地图配准，而不能把两幅4097×4097栅格看作天然对齐。高程样本已解码，下一步应从两版明确的聚落、场景路径、岸线或其他稳定地理节点建立控制点，并通过剔除机制数据产生的虚假地貌边界来验证。

本轮直接实证等级：两版原始scene.xscene/terrain.bin字段、PHYM四季record结构和索引、layer分布、16-bit HGHT样本经明确公式换算后的场景Z值、原版河流Paths与river layer的距离统计。研究性推论：原版Paths与PHYM river层存在功能性对应，值得进一步联系实际河流几何。仍待证问题：《战帆》river_triangles源网格与真实河流水面边界、两版大湖与山地的几何配准、Flowmap与世界XY的数值绑定、Map场景单位与世界内部地理距离的关系。

## 六、成果与复核资料

Google Drive 图件1（双版本统一Z色标）：https://drive.google.com/file/d/1ymJeiisRuBnoAnd3V3y6Hf46ddFIqLeS/view

Google Drive 图件2（双版本PHYM图层索引）：https://drive.google.com/file/d/1R1iQz7c7tkFaAfCP7ITV6ds8zV9jbFC-/view

Google Drive 图件3（原版河流路径与river层）：https://drive.google.com/file/d/1krIsrLA4fG5wkbVvjlQ8O0fH6HCvjAtP/view

本地成果：dual_height_common_scene_z.png、dual_phym_summer_index.png、original_river_layer_vs_paths.png、phym_index_distribution.png、phym_index_counts.csv、phym_season_differences.csv、scene_layer_index.csv、original_river_path_PHYM7_proximity.csv、analysis_summary.json；完整导出包CGEO-MAP-RES-005_analysis_bundle.zip。

再现时应明确保留两套版本标签以及两版高度范围；此前生成的两幅高程预览分别独立拉伸，本轮新增的统一色标图才适合比较高度值的可视等级，但仍不适合做未配准的像素差。

关联资料：CGEO-MAP-RES-003、CGEO-MAP-RES-004；同版本独立地形格式逆向说明https://github.com/davgor/MNBL-modding-repo/blob/23ba089566884dabe61164f47ae3d9e4f145da86/docs/formats/terrain-bin.md。

---

Google Drive原件：https://docs.google.com/document/d/1nj_dvB-V34xGh5ckDmEohtnzKOlYwu4FcOUErCOs2T8/edit

说明：本研究仅提交技术报告及派生统计，未向GitHub上传游戏原始资源。


## 同步数据附件

[PHYM单季各图层精确计数与比例（CSV）](CGEO-MAP-RES-005_phym_summer_counts.csv)。该数据是从两个版本各256个PHYM图块的完整夏季记录中计算的派生统计，不包含原始游戏二进制。
