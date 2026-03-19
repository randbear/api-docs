# Google AI

Google AI for Developers 提供 Gemini API，支持文本、图像、视频、音频等多模态能力。本仓库当前仅收录 `Nano Banana 2`，即 `Gemini 3.1 Flash Image Preview`。

## 平台信息

| 属性 | 值 |
|------|-----|
| 厂商 | Google |
| 平台 | Gemini API / Google AI for Developers |
| API Base URL | `https://generativelanguage.googleapis.com` |
| 认证方式 | `x-goog-api-key: $GEMINI_API_KEY` |
| 文档 | [ai.google.dev/gemini-api/docs](https://ai.google.dev/gemini-api/docs) |

## Nano Banana 系列

| 模型 | 任务 | 模型 ID | 说明 | 文档 |
|------|------|--------|------|------|
| Nano Banana 2 | text-to-image / image-to-image | `gemini-3.1-flash-image-preview` | 高效率预览图像模型，支持文生图、图像编辑、Google Search grounding 和最高 4K 输出 | [查看](nano-banana-2/nano-banana-2.md) |

## 计费概览

### 标准调用

| 项目 | 价格 |
|------|------|
| 输入（text / image） | `$0.50 / 1M tokens` |
| 输出（text and thinking） | `$3.00 / 1M tokens` |
| 输出（images） | `$60.00 / 1M image tokens` |
| Google Search Grounding | 每月前 `5,000` 次 prompts 免费，之后 `$14 / 1,000` search queries |

### Batch 调用

| 项目 | 价格 |
|------|------|
| 输入（text / image） | `$0.25 / 1M tokens` |
| 输出（text and thinking） | `$1.50 / 1M tokens` |
| 输出（images） | `$30.00 / 1M image tokens` |

## 备注

- 该模型为 Preview 状态，官方明确说明能力、定价或限流可能在稳定前调整。
- 标准调用的实时 rate limit 需在 AI Studio 查看；公开文档只披露了与 tier 相关的说明和 Batch enqueued tokens 上限。

数据来源：[Google Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing)、[Google Gemini API Rate Limits](https://ai.google.dev/gemini-api/docs/rate-limits)
