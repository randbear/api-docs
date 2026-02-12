# MiniMax（海螺）

MiniMax 开放平台提供的海螺 Hailuo 系列视频生成模型。

## 平台信息

| 属性 | 值 |
|------|-----|
| 厂商 | MiniMax |
| 平台 | MiniMax 开放平台 |
| API Base URL | `https://api.minimax.io` |
| 认证方式 | `Authorization: Bearer $MINIMAX_API_KEY` |
| 文档 | [platform.minimax.io/docs](https://platform.minimax.io/docs/api-reference/video-generation-t2v) |

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

数据来源：[MiniMax 按量计费](https://platform.minimaxi.com/docs/pricing/pay-as-you-go)
