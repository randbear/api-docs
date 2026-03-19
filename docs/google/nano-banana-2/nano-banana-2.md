---
title: Nano Banana 2 图像生成
provider: google
model_id: gemini-3.1-flash-image-preview
task: text-to-image / image-to-image
---

# Nano Banana 2 图像生成

> Google Gemini 原生图像生成中的高效率预览模型，对应 `Gemini 3.1 Flash Image Preview`，适合快速交互式生成、图像编辑和高吞吐场景。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型别名 | Nano Banana 2 |
| 模型 ID | `gemini-3.1-flash-image-preview` |
| 任务类型 | text-to-image / image-to-image |
| 输入 | 文本；或文本 + 图片（`inline_data` base64） |
| 输出 | 默认返回文本 + 图片；可配置为仅返回图片 |
| 默认分辨率 | `1K` |
| 可选分辨率 | `512`、`1K`、`2K`、`4K` |
| 默认宽高比 | 有输入图时尽量匹配输入图；无输入图时默认为 `1:1` |
| 支持宽高比 | `1:1`、`1:4`、`1:8`、`2:3`、`3:2`、`3:4`、`4:1`、`4:3`、`4:5`、`5:4`、`8:1`、`9:16`、`16:9`、`21:9` |
| Grounding | 支持 Google Search 的 Web Search / Image Search |
| 水印 | 所有生成图片均包含 SynthID watermark |
| 发布状态 | Preview，官方说明可能调整，限流通常比稳定版更严格 |

## 能力与限制

- 支持文生图、图像编辑、局部替换、风格迁移、多图工作流和带搜索 grounding 的图像生成。
- 默认返回文本和图片混合结果；如只需要图片，可设置 `responseModalities` 为 `["IMAGE"]`。
- 官方建议该模型在单个工作流中最多支持 4 个角色相似度和最多 10 个对象保真。
- 不支持音频或视频输入。
- 使用 Google Search 的图片 grounding 时，当前不支持使用 Web 搜索得到的真实人物图片。

## API 调用

### 端点

`POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent`

### 请求头

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `x-goog-api-key` | string | 是 | Gemini API Key |
| `Content-Type` | string | 是 | 固定为 `application/json` |

### 请求参数

说明：REST 请求体使用 `generationConfig`；SDK 示例里对应字段名通常为 `config`。

| 参数 | 类型 | 必填 | 默认值 | 取值 / 示例 | 说明 |
|------|------|------|--------|-------------|------|
| `contents` | array | 是 | - | `[{ "parts": [...] }]` | 对话内容；单轮图像生成一般传 1 条 user 内容 |
| `contents[].role` | string | 否 | `user` | `user` | 角色；单轮请求通常可省略 |
| `contents[].parts[].text` | string | 条件必填 | - | 任意文本提示词 | 文本提示词 |
| `contents[].parts[].inline_data.mime_type` | string | 条件必填 | - | `image/png`、`image/jpeg` | 输入图片 MIME 类型 |
| `contents[].parts[].inline_data.data` | string | 条件必填 | - | base64 字符串 | 输入图片二进制的 base64 编码 |
| `generationConfig.responseModalities` | array<string> | 否 | `["TEXT","IMAGE"]` | `["IMAGE"]` | 控制返回文本、图片或两者 |
| `generationConfig.imageConfig.aspectRatio` | string | 否 | 跟随输入图或 `1:1` | `16:9` | 输出图片宽高比 |
| `generationConfig.imageConfig.imageSize` | string | 否 | `1K` | `512`、`1K`、`2K`、`4K` | 输出图片尺寸；`K` 必须大写，`512` 不带 `K` |
| `tools[].google_search.searchTypes.webSearch` | object | 否 | - | `{}` | 开启 Google Web Search grounding |
| `tools[].google_search.searchTypes.imageSearch` | object | 否 | - | `{}` | 开启 Google Image Search grounding |

### 输出分辨率对照

以下分辨率来自官方图像生成指南；`512` 仅 `gemini-3.1-flash-image-preview` 支持。

| 宽高比 | `512` | `1K` | `2K` | `4K` |
|------|------|------|------|------|
| `1:1` | `512x512` | `1024x1024` | `2048x2048` | `4096x4096` |
| `1:4` | `256x1024` | `512x2048` | `1024x4096` | `2048x8192` |
| `1:8` | `192x1536` | `384x3072` | `768x6144` | `1536x12288` |
| `2:3` | `424x632` | `848x1264` | `1696x2528` | `3392x5056` |
| `3:2` | `632x424` | `1264x848` | `2528x1696` | `5056x3392` |
| `3:4` | `448x600` | `896x1200` | `1792x2400` | `3584x4800` |
| `4:1` | `1024x256` | `2048x512` | `4096x1024` | `8192x2048` |
| `4:3` | `600x448` | `1200x896` | `2400x1792` | `4800x3584` |
| `4:5` | `464x576` | `928x1152` | `1856x2304` | `3712x4608` |
| `5:4` | `576x464` | `1152x928` | `2304x1856` | `4608x3712` |
| `8:1` | `1536x192` | `3072x384` | `6144x768` | `12288x1536` |
| `9:16` | `384x688` | `768x1376` | `1536x2752` | `3072x5504` |
| `16:9` | `688x384` | `1376x768` | `2752x1536` | `5504x3072` |
| `21:9` | `792x168` | `1584x672` | `3168x1344` | `6336x2688` |

### 请求示例：文生图

```bash
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {
          "text": "生成一张现代庭院的照片，画面中有一个数字 2 形状的泳池，整体构图严格等距视角。"
        }
      ]
    }],
    "generationConfig": {
      "responseModalities": ["IMAGE"],
      "imageConfig": {
        "aspectRatio": "16:9",
        "imageSize": "2K"
      }
    }
  }'
```

### 请求示例：图像编辑

```bash
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {
          "text": "基于输入图片，把蓝色沙发改成复古棕色切斯特菲尔德沙发，其余家具、抱枕和灯光保持不变。"
        },
        {
          "inline_data": {
            "mime_type": "image/png",
            "data": "<BASE64_IMAGE_DATA>"
          }
        }
      ]
    }],
    "generationConfig": {
      "responseModalities": ["TEXT", "IMAGE"]
    }
  }'
```

### 请求示例：启用 Google Search Grounding

```bash
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {
          "text": "使用 Google 搜索和图片搜索，为凤尾绿咬鹃生成一张 3:2 的自然风格壁纸。"
        }
      ]
    }],
    "tools": [
      {
        "google_search": {
          "searchTypes": {
            "webSearch": {},
            "imageSearch": {}
          }
        }
      }
    ],
    "generationConfig": {
      "responseModalities": ["IMAGE"]
    }
  }'
```

### Grounding 展示要求

- 如果展示 Image Search 引用源，必须提供来源网页链接，且应链接到包含该图片的网页，而不是图片文件本身。
- 如果同时展示源图片，必须保证用户可以一跳直达来源网页，不能通过中间图片查看器绕行。
- API 会在 `groundingMetadata` 中返回用于归因的来源信息、图片 URL 和搜索入口渲染内容。

### 响应结构示例（节选）

以下示例根据官方 `generateContent` 响应结构整理，重点展示图像生成常用字段：

```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Here is your generated image."
          },
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "<BASE64_IMAGE_DATA>"
            }
          }
        ]
      }
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 123,
    "candidatesTokenCount": 1680,
    "totalTokenCount": 1803
  },
  "modelVersion": "gemini-3.1-flash-image-preview",
  "responseId": "example-response-id"
}
```

## 计费

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

### 按单张图片估算

以下按官方 pricing 页的图像 token 口径计算：

| 分辨率 | 图像 token / 张 | 标准调用单价 | Batch 单价 |
|------|----------------|-------------|-----------|
| `512` | `747` | `$0.045 / 张` | `$0.022 / 张` |
| `1K` | `1120` | `$0.067 / 张` | `$0.034 / 张` |
| `2K` | `1680` | `$0.101 / 张` | `$0.050 / 张` |
| `4K` | `2520` | `$0.151 / 张` | `$0.076 / 张` |

### 官方差异说明

- 图像生成指南的“分辨率表”中给出的 `2K` 和 `4K` token 数，与 pricing 页中的计费 token 数不一致。
- 本文档的价格换算以 pricing 页为准，因为该页是官方定价依据；分辨率尺寸则仍采用图像生成指南中的尺寸表。

## 限流与稳定性

- 官方公开 rate limits 页未给出该模型标准调用的固定 RPM / IPM 数值，只说明实际限额取决于项目 tier，并建议在 AI Studio 查看当前项目的实时限额。
- Preview 模型可能在正式稳定前发生变化，且限流通常更严格。
- Batch API 的 `enqueued tokens` 上限中，`Gemini 3.1 Flash Image Preview` 的公开值为：Tier 1 `1,000,000`、Tier 2 `250,000,000`、Tier 3 `750,000,000`。

## 数据来源

- 图像生成指南：https://ai.google.dev/gemini-api/docs/image-generation
- 定价：https://ai.google.dev/gemini-api/docs/pricing
- 限流：https://ai.google.dev/gemini-api/docs/rate-limits
- `generateContent` API 参考：https://ai.google.dev/api/generate-content
