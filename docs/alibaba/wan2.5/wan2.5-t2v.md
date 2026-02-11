---
title: 万相 2.5 文生视频
provider: alibaba
model_id: wan2.5-t2v-preview
task: text-to-video
---

# 万相 2.5 文生视频

> 阿里云百炼万相 2.5 文生视频模型，支持 5/10 秒视频生成，480P/720P/1080P 分辨率。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `wan2.5-t2v-preview` |
| 任务类型 | text-to-video |
| 输入 | 文本提示词（最长 1500 字符） |
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
| model | string | 是 | — | `wan2.5-t2v-preview` | 模型ID |
| input.prompt | string | 是 | — | 最长 1500 字符 | 文本提示词 |
| input.negative_prompt | string | 否 | — | 最长 500 字符 | 反向提示词 |
| input.audio_url | string | 否 | — | wav/mp3，3~30秒，最大15MB | 音频文件 URL |
| parameters.size | string | 否 | 模型默认 | 480P/720P/1080P 各比例 | 视频分辨率 |
| parameters.duration | integer | 否 | 5 | 5 或 10 | 视频时长（秒） |
| parameters.prompt_extend | boolean | 否 | true | true/false | 启用提示词优化 |
| parameters.watermark | boolean | 否 | false | true/false | 添加"AI生成"水印 |
| parameters.seed | integer | 否 | 随机 | 0~2147483647 | 随机种子 |

### 请求示例

```bash
curl -X POST 'https://dashscope.aliyuncs.com/api/v1/services/aigc/video-generation/video-synthesis' \
  -H 'X-DashScope-Async: enable' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "wan2.5-t2v-preview",
    "input": {
      "prompt": "一只小猫在月光下奔跑",
      "negative_prompt": "低质量"
    },
    "parameters": {
      "size": "1280*720",
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
  "request_id": "caa62a12-8841-41a6-8af2-xxxxxx",
  "output": {
    "task_id": "eff1443c-ccab-4676-aad3-xxxxxx",
    "task_status": "SUCCEEDED",
    "submit_time": "2025-09-29 14:18:52.331",
    "end_time": "2025-09-29 14:23:39.407",
    "video_url": "https://dashscope-result-sh.oss-accelerate.aliyuncs.com/xxx.mp4"
  },
  "usage": {
    "duration": 5,
    "size": "1280*720",
    "output_video_duration": 5,
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

| 模型 | 分辨率 | 价格 | 免费额度 |
|------|--------|------|----------|
| wan2.5-t2v-preview | 480P | 0.3 元/秒 | 50 秒 |
| wan2.5-t2v-preview | 720P | 0.6 元/秒 | 50 秒 |
| wan2.5-t2v-preview | 1080P | 1 元/秒 | 50 秒 |

按成功生成的视频秒数计费。视频 URL 24 小时内有效，请及时下载。建议轮询间隔 15 秒，处理时间通常 1~5 分钟。

## 数据来源

- API 参考：https://help.aliyun.com/zh/model-studio/text-to-video-api-reference
- 计费信息：https://help.aliyun.com/zh/model-studio/model-pricing
