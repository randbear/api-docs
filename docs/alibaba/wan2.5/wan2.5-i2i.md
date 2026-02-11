---
title: 万相 2.5 图像编辑
provider: alibaba
model_id: wan2.5-i2i-preview
task: image-editing
---

# 万相 2.5 图像编辑

> 阿里云百炼万相 2.5 图像编辑模型，支持单图编辑和多图融合（最多3张），异步调用。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `wan2.5-i2i-preview` |
| 任务类型 | image-editing |
| 输入 | 文本 + 图像（1~3张） |
| 输出 | 图像（URL，24小时有效） |
| 分辨率范围 | 768×768~1280×1280，宽高比 1:4~4:1 |

## API 调用

### 端点

**创建任务（异步）：**

`POST https://dashscope.aliyuncs.com/api/v1/services/aigc/image2image/image-synthesis`

**查询任务结果：**

`GET https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}`

### 请求头

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Content-Type | string | 是 | `application/json` |
| Authorization | string | 是 | `Bearer sk-xxxx` |
| X-DashScope-Async | string | 是 | 必须设为 `enable` |

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 取值范围 | 说明 |
|------|------|------|--------|----------|------|
| model | string | 是 | — | `wan2.5-i2i-preview` | 模型ID |
| input.prompt | string | 是 | — | 最长 2000 字符 | 文本指令 |
| input.images | array | 是 | — | 最多 3 张图片 URL | 输入图像列表（HTTPS/HTTP URL 或 base64） |
| input.negative_prompt | string | 否 | — | 最长 500 字符 | 反向提示词 |
| parameters.size | string | 否 | `1280*1280` | 768×768~1280×1280，宽高比 1:4~4:1 | 输出分辨率 |
| parameters.n | integer | 否 | 4 | 1~4 | 生成图片数量 |
| parameters.prompt_extend | boolean | 否 | true | true/false | 启用提示词优化 |
| parameters.watermark | boolean | 否 | false | true/false | 添加"AI生成"水印 |
| parameters.seed | integer | 否 | 随机 | 0~2147483647 | 随机种子 |

### 输入图像要求

| 属性 | 要求 |
|------|------|
| 格式 | JPEG, JPG, PNG（无透明）, BMP, WEBP |
| 分辨率 | 384~5000 像素（宽和高） |
| 文件大小 | 最大 10MB |
| 数量 | 1~3 张 |

### 推荐分辨率

| 宽高比 | 分辨率 |
|--------|--------|
| 1:1 | 1280×1280 或 1024×1024 |
| 2:3 | 800×1200 |
| 3:2 | 1200×800 |
| 3:4 | 960×1280 |
| 9:16 | 720×1280 |
| 16:9 | 1280×720 |

### 请求示例（单图编辑）

```bash
curl -X POST 'https://dashscope.aliyuncs.com/api/v1/services/aigc/image2image/image-synthesis' \
  -H 'X-DashScope-Async: enable' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "wan2.5-i2i-preview",
    "input": {
      "prompt": "把花裙子换成复古蕾丝长裙",
      "images": ["https://example.com/image.webp"]
    },
    "parameters": {"n": 1}
  }'
```

### 请求示例（多图融合）

```bash
curl -X POST 'https://dashscope.aliyuncs.com/api/v1/services/aigc/image2image/image-synthesis' \
  -H 'X-DashScope-Async: enable' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "wan2.5-i2i-preview",
    "input": {
      "prompt": "把图1的钟表放到图2桌子上的花瓶旁边",
      "images": ["https://example.com/clock.jpg", "https://example.com/table.jpg"]
    },
    "parameters": {"n": 1}
  }'
```

### 查询任务结果

```bash
curl -X GET 'https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY"
```

### 响应示例（任务创建）

```json
{
  "output": {
    "task_status": "PENDING",
    "task_id": "0385dc79-5ff8-4d82-bcb6-xxxxxx"
  },
  "request_id": "4909100c-7b5a-9f92-bfe5-xxxxxx"
}
```

### 响应示例（任务完成）

```json
{
  "output": {
    "task_id": "7f4836cd-1c47-41b3-b3a4-xxxxxx",
    "task_status": "SUCCEEDED",
    "results": [
      {
        "url": "https://dashscope-result-sh.oss-cn-shanghai.aliyuncs.com/xxx.png",
        "orig_prompt": "原始指令",
        "actual_prompt": "优化后的指令"
      }
    ],
    "task_metrics": {"TOTAL": 1, "SUCCEEDED": 1, "FAILED": 0}
  },
  "usage": {"image_count": 1}
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
| wan2.5-i2i-preview | 0.220177 元/张 | 50 张 |

按成功生成的图片张数计费。图片 URL 24 小时内有效，请及时下载。处理时间约 30~60 秒。

## 数据来源

- API 参考：https://help.aliyun.com/zh/model-studio/wan2-5-image-edit-api-reference
- 计费信息：https://help.aliyun.com/zh/model-studio/model-pricing
