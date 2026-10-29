# 地理研究库双端恢复记录

**日期：** 2026-10-29  
**仓库：** `Nobody-zz/awake-calradia-research-atlas`  
**主线规则：** GitHub `main` 持续更新；Google Drive 定期留档，不要求逐次提交后同步覆盖。

## 本轮已写入 GitHub main

1. `research/README.md`
   - 将规范索引标题从旧的 v1.1 标签纠正为 Drive 当前标题所示的“试行 v1.3”。
   - 将 HYD-001 索引从旧 v0.1 指针改为 v0.3，并链接 Drive 当前 v0.3 文档。
   - 增加 HUM-001 v0.4 正文与研究日志入口；明确 Drive 搜索返回的同编号 v0.1 目前不能覆盖 GitHub v0.4。
   - 将 RES-015 的 43.1%、3.2% 和城镇/港口锚点结论标记为待复核，而非由空壳正文独立证明。
   - 将“Drive 与 GitHub 已同步”改为尚待逐段核验的状态。

2. `research/geo/00/1KlBS4Lv27FR13ycc7hPqAWPhPinDcmzKVmLc1q8efeE.md`
   - 增加优先于历史快照的当前状态纠偏说明。
   - 将 HYD-001 v0.3、HUM-001 v0.4 登记为当前 GitHub 指针。
   - 明确区分 §六 的论文主证据等级 A/B/C/D/M 与 §十二历史截图审查的 V1/V2/U 观察标签；避免将截图段落中的 A 与主证据等级 A 混用。
   - 明确 RES-015 正文只有 453 字节，数值结论须待数据和脚本复核。

3. `research/source-archives/main-map-manifest.csv` 与 `research/source-archives/README.md`
   - 为已进入 GitHub 的 6 个 Native/War Sails 原始地图文件补上 Git blob SHA-1。
   - 保留其余 6 个文件的 Drive SHA-256 状态，并明确空白 blob 字段表示文件未进入 GitHub。
   - 解释 `SHA256SUMS.txt` 的覆盖范围，避免将 ZIP 校验和误称为已列出全部解压后二进制。

4. 根目录 `README.md`
   - 写明 GitHub main 持续更新、Google Drive 定期留档的正式工作规则，以及本轮已修复与待办事项。

## 已知未完成项（不将计划当作完成）

- **HUM-001：** GitHub 当前正文为 v0.4；Drive 搜索目前命中同编号 v0.1。进一步搜索未找到 Drive v0.4 文档，需查 Drive 修订历史/归档位置，确定两者关系。
- **HYD-001：** Drive 当前标题为 v0.3，GitHub 有 v0.3 Markdown 镜像；尚未完成逐段正文对照。
- **证据等级：** 本轮先在 GitHub 镜像中标明两套标签的作用域，尚未修改 Drive 规范原件。
- **RES-015：** 空壳正文与索引侧数字矛盾已显式标记；需要读取其 Drive 数据包、CSV 与脚本，复算后再恢复结论。
- **原始地图资源：** 12 个文件中 6 个已归档 GitHub，6 个仍只有 Drive 原件和 SHA-256。是否补齐需要可靠的二进制传输路径；不得伪造提交状态。
- **CLM-001：** Draft PR #1 仍为开放草稿，未合入 main；本轮不擅自合并。
- **Drive 定时归档：** 已建立每周五上午的归档任务。它将在后续运行中核对 main commit、生成带日期的 Drive 归档副本及清单；首次实际归档尚未执行，不能宣称已产生归档快照。

## 相关入口

- [研究总索引](../README.md)
- [HUM-001 v0.4](../03/HUM/CGEO-S-HUM-001.md)
- [HYD-001 GitHub 镜像](../03/HYD/1Cl-YL13V_bHN9qOnSgSJmQ40Y2AtOXk5O-xvFd8RYco.md)
- [Main_map 原始资源清单](../../source-archives/main-map-manifest.csv)
- [原始资源归档说明](../../source-archives/README.md)
