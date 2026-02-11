---
title: 万相 2.6 图生图
provider: alibaba
model_id: wan2.6-image
task: image-to-image
---

# 万相 2.6 图生图

> 阿里云百炼万相 2.6 图像编辑模型，支持单图编辑、多图融合（最多4张），以及图文混合输出模式。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `wan2.6-image` |
| 任务类型 | image-to-image |
| 输入 | 文本 + 图像（1~4张） |
| 输出 | 图像（URL，24小时有效） |
| 分辨率范围 | 总像素 768×768~1280×1280，宽高比 1:4~4:1 |

## API 调用

### 端点

**同步调用：**

`POST https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation`

**异步调用（同一端点，加异步头）：**

`POST https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation`

**查询任务结果：**

`GET https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}`

### 请求头

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Content-Type | string | 是 | `application/json` |
| Authorization | string | 是 | `Bearer sk-xxxx` |
| X-DashScope-Async | string | 异步时必填 | 设为 `enable` |
| X-DashScope-Sse | string | 流式时必填 | 设为 `enable`（仅 enable_interleave=true 时） |

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 取值范围 | 说明 |
|------|------|------|--------|----------|------|
| model | string | 是 | — | `wan2.6-image` | 模型ID |
| input.messages | array | 是 | — | 单条消息 | 包含一条 user 消息 |
| input.messages[].role | string | 是 | — | `user` | 角色 |
| input.messages[].content | array | 是 | — | 1个text + 0~4个image | 内容数组 |
| input.messages[].content[].text | string | 是 | — | 最长 2000 字符 | 正向提示词 |
| input.messages[].content[].image | string | 条件必填 | — | URL 或 base64 | 输入图像 |
| parameters.negative_prompt | string | 否 | — | 最长 500 字符 | 反向提示词 |
| parameters.size | string | 否 | — | 总像素 768×768~1280×1280，宽高比 1:4~4:1 | 输出分辨率 |
| parameters.enable_interleave | boolean | 否 | false | true/false | false=图像编辑模式，true=图文混合输出 |
| parameters.n | integer | 否 | 4（编辑）/ 1（混合） | 编辑:1~4，混合:必须为1 | 生成图片数量 |
| parameters.max_images | integer | 否 | 5 | 1~5 | 图文混合模式最大图片数 |
| parameters.prompt_extend | boolean | 否 | true | true/false | 启用提示词优化（仅编辑模式） |
| parameters.watermark | boolean | 否 | false | true/false | 添加"AI生成"水印 |
| parameters.seed | integer | 否 | 随机 | 0~2147483647 | 随机种子 |
| parameters.stream | boolean | 否 | false | true/false | 流式输出（图文混合模式必须为 true） |

### 输入图像要求

| 属性 | 要求 |
|------|------|
| 格式 | JPEG, JPG, PNG（无透明）, BMP, WEBP |
| 分辨率 | 384~5000 像素（宽和高） |
| 文件大小 | 最大 10MB |
| 数量 | 编辑模式：1~4张（必须），混合模式：0~1张 |

### 推荐分辨率

| 宽高比 | 分辨率 |
|--------|--------|
| 1:1 | 1280×1280 或 1024×1024 |
| 2:3 | 800×1200 |
| 3:2 | 1200×800 |
| 3:4 | 960×1280 |
| 4:3 | 1280×960 |
| 9:16 | 720×1280 |
| 16:9 | 1280×720 |

### 请求示例（图像编辑）

```bash
curl -X POST 'https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -d '{
    "model": "wan2.6-image",
    "input": {
      "messages": [
        {
          "role": "user",
          "content": [
            {"text": "参考图片1的风格和图片2的背景，生成番茄炒蛋"},
            {"image": "https://example.com/style.png"},
            {"image": "https://example.com/background.webp"}
          ]
        }
      ]
    },
    "parameters": {
      "prompt_extend": true,
      "watermark": false,
      "n": 1,
      "enable_interleave": false,
      "size": "1280*1280"
    }
  }'
```

### 请求示例（图文混合输出，流式）

```bash
curl -X POST 'https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H 'X-DashScope-Sse: enable' \
  -d '{
    "model": "wan2.6-image",
    "input": {
      "messages": [
        {
          "role": "user",
          "content": [
            {"text": "给我3张辣椒炒肉的教程图"}
          ]
        }
      ]
    },
    "parameters": {
      "max_images": 3,
      "size": "1280*1280",
      "stream": true,
      "enable_interleave": true
    }
  }'
```

### 查询任务结果（异步模式）

```bash
curl -X GET 'https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY"
```

### 响应示例（同步/编辑模式）

```json
{
  "output": {
    "choices": [
      {
        "finish_reason": "stop",
        "message": {
          "content": [
            {
              "image": "https://dashscope-result-bj.oss-cn-beijing.aliyuncs.com/xxx.png",
              "type": "image"
            }
          ],
          "role": "assistant"
        }
      }
    ],
    "finished": true
  },
  "usage": {
    "image_count": 1,
    "size": "1280*1280"
  },
  "request_id": "a3f4befe-cacd-49c9-8298-xxxxxx"
}
```

### 任务状态

| 状态 | 说明 |
|------|------|
| PENDING | 排队中 |
| RUNNING | 处理中 |
| SUCCEEDED | 成功 |
| FAILED | 失败 |
| CANCELED | 已取消 |
| UNKNOWN | 未知/已过期 |

## 计费

| 模型 | 价格 | 免费额度 |
|------|------|----------|
| wan2.6-image | 0.20 元/张 | 50 张 |

按成功生成的图片张数计费。图片 URL 24 小时内有效，请及时下载。

## 数据来源

- API 参考：https://help.aliyun.com/zh/model-studio/wan-image-generation-api-reference
- 计费信息：https://help.aliyun.com/zh/model-studio/model-pricing
