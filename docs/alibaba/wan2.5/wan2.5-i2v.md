---
title: 万相 2.5 图生视频
provider: alibaba
model_id: wan2.5-i2v-preview
task: image-to-video
---

# 万相 2.5 图生视频

> 阿里云百炼万相 2.5 图生视频模型，支持 5/10 秒视频生成，480P/720P/1080P，支持音频。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `wan2.5-i2v-preview` |
| 任务类型 | image-to-video |
| 输入 | 图像 + 文本提示词（可选） |
| 输出 | 视频（URL，24小时有效） |
| 视频时长 | 5 或 10 秒 |
| 视频分辨率 | 480P、720P、1080P |

## API 调用

### 端点

**创建任务（仅支持异步）：**

`POST https://dashscope.aliyuncs.com/api/v1/services/aigc/video-generation/video-synthesis`

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
| model | string | 是 | — | `wan2.5-i2v-preview` | 模型ID |
| input.prompt | string | 否 | — | 最长 1500 字符 | 文本提示词 |
| input.negative_prompt | string | 否 | — | 最长 500 字符 | 反向提示词 |
| input.img_url | string | 是 | — | URL / file:// / base64 | 输入图像 |
| input.audio_url | string | 否 | — | wav/mp3，3~30秒，最大15MB | 音频文件 URL |
| parameters.resolution | string | 否 | 1080P | `480P` / `720P` / `1080P` | 视频分辨率 |
| parameters.duration | integer | 否 | 5 | 5 或 10 | 视频时长（秒） |
| parameters.prompt_extend | boolean | 否 | true | true/false | 启用提示词优化 |
| parameters.watermark | boolean | 否 | false | true/false | 添加"AI生成"水印 |
| parameters.seed | integer | 否 | 随机 | 0~2147483647 | 随机种子 |

### 输入图像要求

| 属性 | 要求 |
|------|------|
| 格式 | JPEG, JPG, PNG（无透明）, BMP, WEBP |
| 分辨率 | 360~2000 像素（宽和高） |
| 文件大小 | 最大 10MB |

### 音频文件要求

| 属性 | 要求 |
|------|------|
| 格式 | WAV, MP3 |
| 时长 | 3~30 秒 |
| 文件大小 | 最大 15MB |
| 处理规则 | 超过 duration 参数则截断，不足则静音填充 |

### 请求示例

```bash
curl -X POST 'https://dashscope.aliyuncs.com/api/v1/services/aigc/video-generation/video-synthesis' \
  -H 'X-DashScope-Async: enable' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "wan2.5-i2v-preview",
    "input": {
      "prompt": "画面中的人物缓缓转头微笑",
      "img_url": "https://example.com/input.png"
    },
    "parameters": {
      "resolution": "720P",
      "duration": 5,
      "prompt_extend": true
    }
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
  "request_id": "2ca1c497-f9e0-449d-9a3f-xxxxxx",
  "output": {
    "task_id": "af6efbc0-4bef-4194-8246-xxxxxx",
    "task_status": "SUCCEEDED",
    "submit_time": "2025-09-25 11:07:28.590",
    "end_time": "2025-09-25 11:17:11.650",
    "video_url": "https://dashscope-result-sh.oss-cn-shanghai.aliyuncs.com/xxx.mp4"
  },
  "usage": {
    "duration": 5,
    "output_video_duration": 5,
    "video_count": 1,
    "SR": 720
  }
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

| 模型 | 类型 | 分辨率 | 价格 | 免费额度 |
|------|------|--------|------|----------|
| wan2.5-i2v-preview | 有声视频 | 480P | 0.3 元/秒 | 50 秒 |
| wan2.5-i2v-preview | 有声视频 | 720P | 0.6 元/秒 | 50 秒 |
| wan2.5-i2v-preview | 有声视频 | 1080P | 1 元/秒 | 50 秒 |

按成功生成的视频秒数计费。视频 URL 24 小时内有效，请及时下载。建议轮询间隔 15 秒，处理时间通常 1~5 分钟。

## 数据来源

- API 参考：https://help.aliyun.com/zh/model-studio/image-to-video-api-reference
- 计费信息：https://help.aliyun.com/zh/model-studio/model-pricing
