---
title: Seedream 4.5 图像生成
provider: volcengine
model_id: doubao-seedream-4-5-251128
task: text-to-image
---

# Seedream 4.5 图像生成

> 火山方舟豆包 Seedream 4.5 图像生成模型，支持文生图、图生图、多图融合、组图生成，最高 4K 分辨率。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `doubao-seedream-4-5-251128` |
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
| model | string | 是 | — | `doubao-seedream-4-5-251128` | 模型ID |
| prompt | string | 是 | — | 中文最长 300 字，英文最长 600 字 | 文本提示词 |
| image | array | 否 | — | 最多 14 张图片 URL 或 base64 | 输入图像列表（图生图/多图融合） |
| size | string | 否 | `2048x2048` | 总像素 3,686,400~16,777,216 | 输出分辨率（宽x高） |
| seed | integer | 否 | 随机 | -1~2147483647 | 随机种子，-1 为随机 |
| sequential_image_generation | string | 否 | `auto` | `auto` / `disabled` | 组图生成模式 |
| sequential_image_generation_options.max_images | integer | 否 | 15 | 1~15 | 组图最大生成数量 |
| stream | boolean | 否 | false | true/false | 是否流式返回 |
| response_format | string | 否 | `url` | `url` / `b64_json` | 返回格式 |
| watermark | boolean | 否 | true | true/false | 是否添加水印 |
| optimize_prompt_options.mode | string | 否 | — | `standard` / `fast` | 提示词优化模式 |

### 输入图像要求

| 属性 | 要求 |
|------|------|
| 格式 | JPEG, PNG, WEBP, BMP, TIFF, GIF |
| 分辨率 | 最大 6000×6000 像素 |
| 文件大小 | 最大 10MB |
| 数量 | 最多 14 张 |

### 推荐分辨率（1K）

| 宽高比 | 分辨率 |
|--------|--------|
| 1:1 | 2048×2048 |
| 4:3 | 2304×1728 |
| 3:4 | 1728×2304 |
| 16:9 | 2560×1440 |
| 9:16 | 1440×2560 |
| 3:2 | 2496×1664 |
| 2:3 | 1664×2496 |
| 21:9 | 3024×1296 |

### 推荐分辨率（4K）

| 宽高比 | 分辨率 |
|--------|--------|
| 1:1 | 4096×4096 |
| 4:3 | 3520×4704 |
| 3:4 | 4704×3520 |
| 16:9 | 5504×3040 |
| 9:16 | 3040×5504 |
| 3:2 | 3328×4992 |
| 2:3 | 4992×3328 |
| 21:9 | 6240×2656 |

### 请求示例（文生图）

```bash
curl -X POST 'https://ark.cn-beijing.volces.com/api/v3/images/generations' \
  -H "Authorization: Bearer $ARK_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "doubao-seedream-4-5-251128",
    "prompt": "一只可爱的猫咪坐在窗台上，阳光照射",
    "size": "2048x2048",
    "response_format": "url"
  }'
```

### 请求示例（图生图）

```bash
curl -X POST 'https://ark.cn-beijing.volces.com/api/v3/images/generations' \
  -H "Authorization: Bearer $ARK_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "doubao-seedream-4-5-251128",
    "prompt": "将背景改为日落海滩",
    "image": ["https://example.com/input.jpg"],
    "size": "2048x2048"
  }'
```

### 响应示例

```json
{
  "model": "doubao-seedream-4-5-251128",
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

### Token 计算

输出 token = sum(宽 × 高) / 256

例如：生成 1 张 2048×2048 图片，token = 2048×2048/256 = 16384

## 计费

| 模型 | 价格 | 说明 |
|------|------|------|
| doubao-seedream-4.5 | 0.25 元/张 | 按成功输出图片数量计费 |

组图场景按实际生成的图片数量计费。因审核等原因未成功输出的图片不计费。图片 URL 24 小时内有效，请及时下载。

## 数据来源

- API 参考：https://www.volcengine.com/docs/82379/1541523
- 计费信息：https://www.volcengine.com/docs/82379/1544106
