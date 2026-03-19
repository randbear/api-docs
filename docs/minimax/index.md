# MiniMax

MiniMax 开放平台提供文本生成、视频生成、语音、图像、音乐等多模态能力。当前仓库已收录 M2.7、M2.5 文本模型与 Hailuo 视频模型。

## 平台信息

| 属性 | 值 |
|------|-----|
| 厂商 | MiniMax |
| 平台 | MiniMax 开放平台 |
| API Base URL | `https://api.minimax.io` |
| 认证方式 | `Authorization: Bearer $MINIMAX_API_KEY` |
| 文档 | [platform.minimax.io/docs](https://platform.minimax.io/docs) |

## M2 系列（文本生成）

| 模型 | 任务 | 模型ID | 上下文窗口 | 文档 |
|------|------|--------|------------|------|
| MiniMax-M2.7 | 对话 / 文本生成 / Agent | `MiniMax-M2.7` | 204,800 tokens | [查看](m2.7/minimax-m2.7.md) |
| MiniMax-M2.5 | 对话 / 文本生成 / Agent | `MiniMax-M2.5` | 204,800 tokens | [查看](m2.5/minimax-m2.5.md) |

## 文本计费概览

| 模型 | 输入 | 输出 | Prompt Cache 读取 | Prompt Cache 写入 | 限流 |
|------|------|------|-------------------|-------------------|------|
| MiniMax-M2.7 | $0.3 / M tokens | $1.2 / M tokens | $0.06 / M tokens | $0.375 / M tokens | 500 RPM / 20,000,000 TPM |
| MiniMax-M2.5 | $0.3 / M tokens | $1.2 / M tokens | $0.03 / M tokens | $0.375 / M tokens | 500 RPM / 20,000,000 TPM |

## Hailuo 系列（视频生成）

| 模型 | 任务 | 模型ID | 分辨率 | 文档 |
|------|------|--------|--------|------|
| Hailuo-02 | T2V / I2V / FL2V | `MiniMax-Hailuo-02` | 512P/768P/1080P | [查看](hailuo/hailuo-02.md) |
| Hailuo-2.3 | T2V / I2V | `MiniMax-Hailuo-2.3` | 768P/1080P | [查看](hailuo/hailuo-2.3.md) |
| Hailuo-2.3-Fast | I2V | `MiniMax-Hailuo-2.3-Fast` | 768P/1080P | [查看](hailuo/hailuo-2.3-fast.md) |

## 计费概览

| 模型 | 分辨率 | 时长 | 价格（元/视频） |
|------|--------|------|------------------|
| Hailuo-2.3-Fast | 768P | 6s | 1.35 |
| Hailuo-2.3-Fast | 768P | 10s | 2.25 |
| Hailuo-2.3-Fast | 1080P | 6s | 2.31 |
| Hailuo-2.3 / Hailuo-02 | 768P | 6s | 2.00 |
| Hailuo-2.3 / Hailuo-02 | 768P | 10s | 4.00 |
| Hailuo-2.3 / Hailuo-02 | 1080P | 6s | 3.50 |
| Hailuo-02 | 512P | 6s | 0.60 |
| Hailuo-02 | 512P | 10s | 1.00 |

生成失败或触发安全审核的视频不计费。

数据来源：[MiniMax 按量计费](https://platform.minimax.io/docs/guides/pricing-paygo)
