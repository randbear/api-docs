---
title: 万相2.5文生图
provider: alibaba
model_id: wan2.5-t2i-preview
task: 文生图
---

# 万相2.5文生图

> 通过文本描述生成高质量图像，支持多种分辨率和批量生成。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `wan2.5-t2i-preview` |
| 任务类型 | 文生图 (text-to-image) |
| 输入 | 文本提示词 |
| 输出 | 图像 |
| 最大分辨率 | 1440×1440（宽高均在 512~1440 像素之间） |

## API 调用

### 端点

```
POST https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis
```

> 必须携带请求头 `X-DashScope-Async: enable`，仅支持异步调用。

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| model | string | 是 | - | 固定为 `wan2.5-t2i-preview` |
| input.prompt | string | 是 | - | 文本提示词，最长 2100 字符 |
| input.negative_prompt | string | 否 | - | 反向提示词，最长 500 字符 |
| parameters.size | string | 否 | `"1024*1024"` | 图片尺寸，格式为 `"宽*高"`，宽高均需在 [512, 1440] 之间。常用值：`1024*1024`（1:1）、`768*1024`（3:4）、`1024*768`（4:3）、`1280*1280` |
| parameters.n | integer | 否 | 1 | 生成图片数量，范围 1~4 |
| parameters.seed | integer | 否 | - | 随机种子，范围 [0, 2147483647] |

### 请求示例

```bash
curl -X POST https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis \
 -H 'X-DashScope-Async: enable' \
 -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
 -H 'Content-Type: application/json' \
 -d '{
  "model": "wan2.5-t2i-preview",
  "input": {
    "prompt": "一间有着精致窗户的花店，漂亮的木质门，摆放着花朵",
    "negative_prompt": "人物"
  },
  "parameters": {
    "size": "1280*1280",
    "n": 1
  }
}'
```

### 异步获取结果

提交请求后会返回 `task_id`，通过以下接口轮询任务状态（建议每 10 秒轮询一次）：

```
GET https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}
```

```bash
curl -X GET "https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}" \
 -H "Authorization: Bearer $DASHSCOPE_API_KEY"
```

> 结果链接有效期为 24 小时。

### 响应示例

创建任务响应：

```json
{
  "output": {
    "task_status": "PENDING",
    "task_id": "xxx"
  },
  "request_id": "xxx"
}
```

任务完成响应：

```json
{
  "output": {
    "task_id": "xxx",
    "task_status": "SUCCEEDED",
    "finished": true,
    "choices": [
      {
        "message": {
          "role": "assistant",
          "content": [
            {
              "image": "https://...png",
              "type": "image"
            }
          ]
        }
      }
    ]
  },
  "usage": {
    "image_count": 1,
    "size": "1280*1280"
  }
}
```

## 计费

| 计费项 | 价格 |
|--------|------|
| 图片生成 | 0.2 元/张 |
