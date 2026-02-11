---
title: Wan2.6 图生图
provider: alibaba
model_id: wan2.6-image
task: 图生图 (image-to-image)
---

# Wan2.6 图生图

> 基于 Wan2.6 大模型的图片编辑与多图融合服务，支持单图编辑和多图融合。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `wan2.6-image` |
| 任务类型 | 图生图 (image-to-image) |
| 输入 | 文本提示词 + 图片（URL 或 Base64） |
| 输出 | 编辑后的图片 |
| 最大分辨率 | 1280x1280（最大 1,638,400 像素） |

### 支持的分辨率

| 分辨率 | 比例 |
|--------|------|
| 1280×1280 | 1:1 |
| 800×1200 | 2:3 |
| 1200×800 | 3:2 |
| 960×1280 | 3:4 |
| 1280×960 | 4:3 |
| 720×1280 | 9:16 |
| 1280×720 | 16:9 |
| 1344×576 | 21:9 |

## API 调用

### 端点

```
POST https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| model | string | 是 | - | 模型ID，固定为 `wan2.6-image` |
| messages | array | 是 | - | 消息数组，包含 role 和 content |
| text | string | 是 | - | 提示词，最长 2000 字符 |
| image | string | 否 | - | 输入图片的 URL 或 Base64 编码 |
| size | string | 否 | - | 图片尺寸，格式为 `宽*高`，如 `1280*1280` |
| n | integer | 否 | 4 | 生成图片数量，范围 1-4 |
| negative_prompt | string | 否 | - | 负向提示词，最长 500 字符 |
| prompt_extend | bool | 否 | true | 是否开启智能改写 |
| watermark | bool | 否 | false | 是否添加 AI 水印 |
| seed | integer | 否 | - | 随机种子，范围 [0, 2147483647] |
| enable_interleave | bool | 否 | false | 图片编辑模式必须设为 `false`；设为 `true` 时为图文交错模式 |
| max_images | integer | 否 | 5 | 图文交错模式下最大图片数，范围 1-5（仅 `enable_interleave=true` 时生效） |

### 请求示例

**单图编辑：**

```bash
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $DASHSCOPE_API_KEY" \
--data '{
  "model": "wan2.6-image",
  "input": {
    "messages": [{
      "role": "user",
      "content": [
        {"text": "参考图片的风格，生成一幅日落风景画"},
        {"image": "https://example.com/reference.png"}
      ]
    }]
  },
  "parameters": {
    "size": "1280*1280",
    "n": 1,
    "enable_interleave": false,
    "prompt_extend": true,
    "watermark": false
  }
}'
```

### 响应示例

```json
{
  "output": {
    "choices": [
      {
        "message": {
          "role": "assistant",
          "content": [
            {
              "image": "https://dashscope-result.oss-cn-beijing.aliyuncs.com/xxx/result.png"
            }
          ]
        }
      }
    ]
  },
  "request_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

> 响应中的图片 URL 有效期为 24 小时，请及时下载保存。

## 计费

| 计费项 | 价格 |
|--------|------|
| 图片生成 | 0.2 元/张 |
