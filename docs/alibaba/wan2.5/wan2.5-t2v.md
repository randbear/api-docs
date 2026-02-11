---
title: 万相2.5文生视频
provider: alibaba
model_id: wan2.5-t2v-preview
task: 文生视频
---

# 万相2.5文生视频

> 通过文本描述生成高质量视频，支持 480P/720P/1080P 多种分辨率和 5 秒或 10 秒时长。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `wan2.5-t2v-preview` |
| 任务类型 | 文生视频 (text-to-video) |
| 输入 | 文本提示词 |
| 输出 | 视频 (mp4) |
| 视频时长 | 5 秒或 10 秒 |
| 视频分辨率 | 480P / 720P / 1080P（默认 1080P） |

## API 调用

### 端点

```
POST https://dashscope.aliyuncs.com/api/v1/services/aigc/video-generation/video-synthesis
```

> 必须携带请求头 `X-DashScope-Async: enable`，仅支持异步调用。

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| model | string | 是 | - | 固定为 `wan2.5-t2v-preview` |
| input.prompt | string | 是 | - | 文本提示词，最长 1500 字符 |
| input.negative_prompt | string | 否 | - | 反向提示词，最长 500 字符 |
| input.audio_url | string | 否 | - | 音频 URL，支持 mp3/wav 格式，时长 3~30 秒，文件 ≤15MB |
| parameters.size | string | 否 | `"1920*1080"` | 视频尺寸，格式为 `"宽*高"`。可选值见下方分辨率表 |
| parameters.duration | integer | 否 | 5 | 视频时长（秒），可选 5 或 10 |
| parameters.prompt_extend | bool | 否 | true | 是否自动扩展提示词 |
| parameters.watermark | bool | 否 | false | 是否添加水印 |
| parameters.seed | integer | 否 | - | 随机种子，范围 [0, 2147483647] |

**可选分辨率：**

| 分辨率等级 | 可选尺寸 |
|-----------|---------|
| 480P | `832*480`、`480*832`、`624*624` |
| 720P | `1280*720`、`720*1280`、`960*960`、`1088*832`、`832*1088` |
| 1080P | `1920*1080`（默认）、`1080*1920`、`1440*1440`、`1632*1248`、`1248*1632` |

### 请求示例

```bash
curl 'https://dashscope.aliyuncs.com/api/v1/services/aigc/video-generation/video-synthesis' \
 -H 'X-DashScope-Async: enable' \
 -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
 -H 'Content-Type: application/json' \
 -d '{
  "model": "wan2.5-t2v-preview",
  "input": {
    "prompt": "一只小猫在月光下奔跑"
  },
  "parameters": {
    "size": "1280*720",
    "duration": 5,
    "prompt_extend": true
  }
}'
```

### 异步获取结果

提交请求后会返回 `task_id`，通过以下接口轮询任务状态（建议每 15 秒轮询一次）：

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
        "url": "https://...mp4"
      }
    ]
  },
  "usage": {
    "video_count": 1,
    "video_duration": 5
  }
}
```

## 计费

| 分辨率 | 价格 |
|--------|------|
| 720P | 0.6 元/秒 |
| 1080P | 1 元/秒 |
