---
title: 万相2.5图像编辑
provider: alibaba
model_id: wan2.5-i2i-preview
task: 图像编辑
---

# 万相2.5图像编辑

> 基于输入图像和文本提示词进行图像编辑或多图融合，支持单图编辑与多图合成。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `wan2.5-i2i-preview` |
| 任务类型 | 图像编辑 (image editing) |
| 输入 | 文本提示词 + 图像（最多 3 张） |
| 输出 | 编辑后的图像 |
| 最大分辨率 | 5000×5000（每边 384~5000 像素，文件 ≤10MB） |

## API 调用

### 端点

```
POST https://dashscope.aliyuncs.com/api/v1/services/aigc/image2image/image-synthesis
```

> 必须携带请求头 `X-DashScope-Async: enable`，仅支持异步调用。

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| model | string | 是 | - | 固定为 `wan2.5-i2i-preview` |
| input.prompt | string | 是 | - | 文本提示词，最长 2000 字符 |
| input.images | string[] | 是 | - | 图像 URL 列表，最多 3 张。支持格式：JPEG、JPG、PNG（无透明通道）、BMP、WEBP |
| input.negative_prompt | string | 否 | - | 反向提示词，最长 500 字符 |
| parameters.size | string | 否 | `"1280*1280"` | 输出图片尺寸，格式为 `"宽*高"` |
| parameters.n | integer | 否 | 4 | 生成图片数量，范围 1~4 |
| parameters.watermark | bool | 否 | false | 是否添加水印 |
| parameters.prompt_extend | bool | 否 | true | 是否自动扩展提示词 |
| parameters.seed | integer | 否 | - | 随机种子，范围 [0, 2147483647] |

### 请求示例

```bash
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/image2image/image-synthesis' \
  -H 'X-DashScope-Async: enable' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "wan2.5-i2i-preview",
    "input": {
      "prompt": "将花卉连衣裙换成复古蕾丝长裙",
      "images": ["https://example.com/image.jpg"]
    },
    "parameters": {"n": 1, "prompt_extend": true}
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
    "results": [
      {
        "url": "https://...png",
        "orig_prompt": "...",
        "actual_prompt": "..."
      }
    ],
    "task_metrics": {
      "TOTAL": 1,
      "SUCCEEDED": 1,
      "FAILED": 0
    }
  },
  "usage": {
    "image_count": 1
  }
}
```

## 计费

| 计费项 | 价格 |
|--------|------|
| 图片生成 | 0.2 元/张 |
