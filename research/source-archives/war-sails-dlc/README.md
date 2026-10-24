# War Sails DLC — Main_map 原始资源

此目录记录用户于 2026-10-25 提供的《战帆》（War Sails）DLC `Main_map` 资源。原版 Native 资源保存在 Google Drive 的另一个文件夹中；两套文件不得混放、覆盖或互相替代。

## 原始文件存放位置

- Google Drive 文件夹：[War Sails DLC — Main_map 原始资源（2026-10-25）](https://drive.google.com/drive/folders/1NONLB02YC62RM5D_-JUcFV0QbnkgeIIW)
- 同级 Native 原版资料文件夹：[原始资料库](https://drive.google.com/drive/folders/17y4EwetqNlFBW1Zf_d_CP4yrdyjmr8Rm)

## 文件清单与校验值

校验值在本轮对话的实际上传文件字节上计算。后续从 Drive 下载后，应重新计算 SHA-256 并与此表比对。Drive 成功保存不等于 GitHub 已保存全部二进制原件。

| 文件 | 字节数 | SHA-256 | Google Drive |
|---|---:|---|---|
| `atmosphere.xml` | 4,941 | `8375ecccc7a721b5d32e8e4fbc59e00b3a2182202d334a79cd01972668533f6d` | [打开](https://drive.google.com/file/d/1eUzroRSVkax0tXhnNijg6urHNkKpZrS2/view) |
| `flora.bin` | 7,253,409 | `7996acbbcbfc09ed9cc8e3fc88fe74de2008cbc736c42e584a2efc3742a2d884` | [打开](https://drive.google.com/file/d/1LIl_-vUUqFEmVGPoB7PHazFdBkrfA7FJ/view) |
| `flowmap.dds` | 1,048,704 | `22d11e2e488535c95f1ab80abefe9da1fd85b186a80d5f4346b13212ec31deea` | [打开](https://drive.google.com/file/d/1oKvUIWLHkU7ZU0-5lBUAWqhWXfqpLFkH/view) |
| `navmesh.bin` | 926,074 | `f8b4b846eb930fbfb64da64bf9c9c191a5aee2f825bfce7d1a59deaa21b0175f` | [打开](https://drive.google.com/file/d/1L3zJ41J1w6pSbu5p06FlzZDAUiNXV6EF/view) |
| `river_triangles.bin` | 1,057,044 | `24fefdbe74302bb2f678db7b4533f00524c9f153613114d88db9187a3252ab24` | [打开](https://drive.google.com/file/d/17A4leaS8ba8yX5T-yJQLlvWamOCOd2Gj/view) |
| `scene.xscene` | 21,127,988 | `1fb8bb08210a377fb727dc9e69454f0368254f28f317cb81c5db2569e3862ebc` | [打开](https://drive.google.com/file/d/1iM3fBTTuoS9l0xj_-k3jqtrPmB_me1oR/view) |
| `terrain.bin` | 28,336,976 | `56c3a0663fb2bf8404210772e187dcd707eb64d8b7e9b5496dfb509bdc3ea9fd` | [打开](https://drive.google.com/file/d/1JVKDyLKOfWuphEdy4gdchScbFdu4ftPw/view) |

## 归档规则

1. 文件名前缀和文件夹均明确标识 `WarSails`，与 Native 原版隔离。
2. 原件保持原样；研究过程中生成的解码数据、截图、网格、派生栅格另存到 `derived/` 或对应分析目录，不覆盖本目录的源文件。
3. 本 GitHub 目录目前作为清单、来源记录和 Drive 索引。大体积二进制原件已存入 Google Drive；GitHub 连接器无法可靠提交本轮大体积二进制，故不声称本目录包含全部原件。
4. 比较 Native 与 War Sails 时，应先核验哈希、文件结构和版本来源，再讨论地图几何差异。