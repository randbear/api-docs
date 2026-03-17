---
title: Seedream 5.0 Lite 图像生成
provider: volcengine
model_id: doubao-seedream-5-0-260128
task: text-to-image
---

# Seedream 5.0 Lite 图像生成

> 火山方舟豆包 Seedream 5.0 Lite 图像生成模型，支持文生图、图生图、多图融合、组图生成、联网搜索，最高 4K 分辨率。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `doubao-seedream-5-0-260128` |
| 任务类型 | text-to-image / image-to-image |
| 输入 | 文本（+ 可选图像，最多 14 张） |
| 输出 | 图像（URL，24小时有效） |
| 默认分辨率 | 2048×2048 |
| 分辨率范围 | 总像素 3,686,400~16,777,216，宽高比 1:16~16:1 |

## API 调用

### 端点

`POST https://ark.cn-beijing.volces.com/api/v3/images/generations`

### 请求头

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Content-Type | string | 是 | `application/json` |
| Authorization | string | 是 | `Bearer $ARK_API_KEY` |

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 取值范围 | 说明 |
|------|------|------|--------|----------|------|
| model | string | 是 | — | `doubao-seedream-5-0-260128` | 模型ID |
| prompt | string | 是 | — | 中文最长 300 字，英文最长 600 字 | 文本提示词 |
| image | string/array | 否 | — | 最多 14 张图片 URL 或 base64 | 输入图像列表（图生图/多图融合） |
| size | string | 否 | `2048x2048` | 方式1: `2K` / `4K`；方式2: 宽x高像素值，总像素 3,686,400~16,777,216 | 输出分辨率 |
| sequential_image_generation | string | 否 | `disabled` | `auto` / `disabled` | 组图生成模式 |
| sequential_image_generation_options.max_images | integer | 否 | 15 | 1~15 | 组图最大生成数量 |
| tools | array | 否 | — | `[{"type": "web_search"}]` | 联网搜索工具 |
| stream | boolean | 否 | false | true/false | 是否流式返回 |
| output_format | string | 否 | `jpeg` | `png` / `jpeg` | 生成图像的文件格式 |
| response_format | string | 否 | `url` | `url` / `b64_json` | 返回格式 |
| watermark | boolean | 否 | true | true/false | 是否添加水印 |
| optimize_prompt_options.mode | string | 否 | `standard` | `standard` | 提示词优化模式 |

### 输入图像要求

| 属性 | 要求 |
|------|------|
| 格式 | JPEG, PNG, WEBP, BMP, TIFF, GIF |
| 宽高比 | 1:16~16:1 |
| 宽高长度 | > 14px |
| 文件大小 | 最大 10MB |
| 总像素 | 最大 6000×6000（36,000,000 px） |
| 数量 | 最多 14 张 |

### 推荐分辨率（2K）

| 宽高比 | 分辨率 |
|--------|--------|
| 1:1 | 2048×2048 |
| 4:3 | 2304×1728 |
| 3:4 | 1728×2304 |
| 16:9 | 2848×1600 |
| 9:16 | 1600×2848 |
| 3:2 | 2496×1664 |
| 2:3 | 1664×2496 |
| 21:9 | 3136×1344 |

### 推荐分辨率（4K）

| 宽高比 | 分辨率 |
|--------|--------|
| 1:1 | 4096×4096 |
| 4:3 | 4704×3520 |
| 3:4 | 3520×4704 |
| 16:9 | 5504×3040 |
| 9:16 | 3040×5504 |
| 3:2 | 4992×3328 |
| 2:3 | 3328×4992 |
| 21:9 | 6240×2656 |

### 请求示例（文生图）

```bash
curl https://ark.cn-beijing.volces.com/api/v3/images/generations \
  -H "Authorization: Bearer $ARK_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "doubao-seedream-5-0-260128",
    "prompt": "一只可爱的猫咪坐在窗台上，阳光照射",
    "size": "2K",
    "watermark": false
  }'
```

### 请求示例（图生图）

```bash
curl https://ark.cn-beijing.volces.com/api/v3/images/generations \
  -H "Authorization: Bearer $ARK_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "doubao-seedream-5-0-260128",
    "prompt": "将背景改为日落海滩",
    "image": ["https://example.com/input.jpg"],
    "size": "2048x2048"
  }'
```

### 请求示例（联网搜索）

```bash
curl https://ark.cn-beijing.volces.com/api/v3/images/generations \
  -H "Authorization: Bearer $ARK_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "doubao-seedream-5-0-260128",
    "prompt": "今天北京的天气",
    "size": "2K",
    "tools": [{"type": "web_search"}]
  }'
```

### 响应参数

| 参数 | 类型 | 说明 |
|------|------|------|
| model | string | 本次请求使用的模型ID |
| created | integer | 请求创建时间的 Unix 时间戳（秒） |
| data | array | 输出图像信息数组，元素可能为图片信息或错误信息 |
| data[].url | string | 图片 URL（response_format 为 url 时返回，24小时有效） |
| data[].b64_json | string | 图片 base64（response_format 为 b64_json 时返回） |
| data[].size | string | 图像宽高像素值，如 `2048x2048` |
| data[].error | object | 某张图片生成失败时的错误信息 |
| data[].error.code | string | 错误码 |
| data[].error.message | string | 错误提示信息 |
| tools | array | 本次请求配置的工具列表 |
| usage.generated_images | integer | 成功生成的图片张数 |
| usage.output_tokens | integer | 生成图片花费的 token 数，计算公式 sum(宽×高)/256 取整 |
| usage.total_tokens | integer | 本次请求消耗的总 token 数（当前与 output_tokens 一致） |
| usage.tool_usage.web_search | integer | 联网搜索调用次数（仅开启联网搜索时返回） |

组图生成时，单张图片可能生成失败：

- **审核不通过**：不影响同请求内其他图片的生成，data 中对应元素为 error 对象
- **内部服务异常（500）**：终止后续图片生成

### 响应示例

```json
{
  "model": "doubao-seedream-5-0-260128",
  "created": 1234567890,
  "data": [
    {
      "url": "https://ark-content-generation-cn-beijing.tos-cn-beijing.volces.com/xxx.png",
      "size": "2048x2048"
    }
  ],
  "usage": {
    "generated_images": 1,
    "output_tokens": 16384,
    "total_tokens": 16384
  }
}
```

### 流式响应

当 `stream` 设为 `true` 时，采用 SSE（Server-Sent Events）方式即时返回每张图片的生成结果。流式响应格式详见[官方文档](https://www.volcengine.com/docs/82379/1824137)。

### Token 计算

输出 token = sum(宽 × 高) / 256

例如：生成 1 张 2048×2048 图片，token = 2048×2048/256 = 16384

## 计费

| 模型 | 价格 | 说明 |
|------|------|------|
| doubao-seedream-5.0-lite | 0.22 元/张 | 按成功输出图片数量计费 |

组图场景按实际生成的图片数量计费。因审核等原因未成功输出的图片不计费。图片 URL 24 小时内有效，请及时下载。

## 数据来源

- API 参考：https://www.volcengine.com/docs/82379/1541523
- 模型列表：https://www.volcengine.com/docs/82379/1330310
- 计费信息：https://www.volcengine.com/docs/82379/1544106
