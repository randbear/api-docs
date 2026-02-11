# 火山方舟（豆包）

火山引擎旗下火山方舟大模型服务平台提供的豆包系列视觉生成模型。

## 平台信息

| 属性 | 值 |
|------|-----|
| 厂商 | 火山引擎（字节跳动） |
| 平台 | 火山方舟大模型服务平台 |
| API Base URL | `https://ark.cn-beijing.volces.com` |
| 认证方式 | `Authorization: Bearer $ARK_API_KEY` |
| 文档 | [volcengine.com/docs/82379](https://www.volcengine.com/docs/82379/1099455) |

## Seedance 系列（视频生成）

| 模型 | 任务 | 模型ID | 默认分辨率 | 文档 |
|------|------|--------|------------|------|
| Seedance 1.5 Pro | t2v / i2v / 音频 / Draft | `doubao-seedance-1-5-pro-251215` | 720p | [查看](seedance/seedance-1.5-pro.md) |
| Seedance 1.0 Pro | t2v / i2v（首帧/首尾帧） | `doubao-seedance-1-0-pro-250528` | 1080p | [查看](seedance/seedance-1.0-pro.md) |
| Seedance 1.0 Pro Fast | t2v / i2v（首帧） | `doubao-seedance-1-0-pro-fast-251015` | 1080p | [查看](seedance/seedance-1.0-pro-fast.md) |
| Seedance 1.0 Lite T2V | t2v | `doubao-seedance-1-0-lite-t2v-250428` | 720p | [查看](seedance/seedance-1.0-lite-t2v.md) |
| Seedance 1.0 Lite I2V | i2v（首帧/首尾帧/参考图） | `doubao-seedance-1-0-lite-i2v-250428` | 720p | [查看](seedance/seedance-1.0-lite-i2v.md) |

## Seedream 系列（图像生成）

| 模型 | 任务 | 模型ID | 文档 |
|------|------|--------|------|
| Seedream 4.5 | t2i / i2i / 组图 | `doubao-seedream-4-5-251128` | [查看](seedream/seedream-4.5.md) |
| Seedream 4.0 | t2i / i2i / 组图 | `doubao-seedream-4-0-250828` | [查看](seedream/seedream-4.0.md) |

## 计费概览

### 图像生成

| 模型 | 价格 |
|------|------|
| doubao-seedream-4.5 | 0.25 元/张 |
| doubao-seedream-4.0 | 0.2 元/张 |

### 视频生成（按 token 单价）

| 模型 | 类型 | 在线推理（元/百万token） | 离线推理（元/百万token） |
|------|------|--------------------------|--------------------------|
| doubao-seedance-1.5-pro | 有声 | 16.00 | 8.00 |
| doubao-seedance-1.5-pro | 无声 | 8.00 | 4.00 |
| doubao-seedance-1.0-pro | — | 15.00 | 7.50 |
| doubao-seedance-1.0-pro-fast | — | 4.20 | 2.10 |
| doubao-seedance-1.0-lite | — | 10.00 | 5.00 |

视频 token 计算公式：(宽 × 高 × 帧率 × 时长) / 1024

数据来源：[火山方舟模型价格](https://www.volcengine.com/docs/82379/1544106)
