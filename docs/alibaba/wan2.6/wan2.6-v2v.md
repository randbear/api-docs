---
title: 万相 2.6 视频生视频
provider: alibaba
model_id: wan2.6-r2v
task: reference-to-video
---

# 万相 2.6 视频生视频

> 阿里云百炼万相 2.6 参考生视频模型，支持参考图片/视频生成新视频，多角色交互，2~10 秒，720P/1080P。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `wan2.6-r2v`（标准版）/ `wan2.6-r2v-flash`（快速版） |
| 任务类型 | reference-to-video |
| 输入 | 文本 + 参考图片/视频（最多5个） |
| 输出 | 视频（URL，24小时有效） |
| 视频时长 | 2~10 秒 |
| 视频分辨率 | 720P、1080P |

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
| model | string | 是 | — | `wan2.6-r2v` / `wan2.6-r2v-flash` | 模型ID |
| input.prompt | string | 是 | — | 最长 1500 字符 | 文本提示词，用"character1"、"character2"引用参考文件 |
| input.negative_prompt | string | 否 | — | 最长 500 字符 | 反向提示词 |
| input.reference_urls | array | 是 | — | 0~5张图片 + 0~3个视频，总数≤5 | 参考图片/视频 URL 列表 |
| parameters.size | string | 否 | `1920*1080` | 见下方分辨率表 | 视频分辨率 |
| parameters.duration | integer | 否 | 5 | 2~10 | 视频时长（秒） |
| parameters.shot_type | string | 否 | `single` | `single` / `multi` | 单镜头/多镜头 |
| parameters.audio | boolean | 否 | true | true/false | 生成音频（仅 wan2.6-r2v-flash） |
| parameters.watermark | boolean | 否 | false | true/false | 添加"AI生成"水印 |
| parameters.seed | integer | 否 | 随机 | 0~2147483647 | 随机种子 |

### 参考文件要求

**图像：**

| 属性 | 要求 |
|------|------|
| 格式 | JPEG, JPG, PNG（无透明）, BMP, WEBP |
| 分辨率 | 240~5000 像素（宽和高） |
| 文件大小 | 最大 10MB |

**视频：**

| 属性 | 要求 |
|------|------|
| 格式 | MP4, MOV |
| 时长 | 1~30 秒 |
| 文件大小 | 最大 100MB |

### 支持的分辨率

**720P：**

| 宽高比 | 分辨率 |
|--------|--------|
| 16:9 | 1280×720 |
| 9:16 | 720×1280 |
| 1:1 | 960×960 |
| 4:3 | 1088×832 |
| 3:4 | 832×1088 |

**1080P：**

| 宽高比 | 分辨率 |
|--------|--------|
| 16:9 | 1920×1080 |
| 9:16 | 1080×1920 |
| 1:1 | 1440×1440 |
| 4:3 | 1632×1248 |
| 3:4 | 1248×1632 |

### 请求示例

```bash
curl -X POST 'https://dashscope.aliyuncs.com/api/v1/services/aigc/video-generation/video-synthesis' \
  -H 'X-DashScope-Async: enable' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "wan2.6-r2v-flash",
    "input": {
      "prompt": "character1 坐在沙发上开心地看电影",
      "reference_urls": ["https://example.com/video.mp4"]
    },
    "parameters": {
      "size": "1280*720",
      "duration": 5,
      "shot_type": "multi",
      "audio": true,
      "watermark": false
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
    "submit_time": "2025-12-16 00:25:59.869",
    "end_time": "2025-12-16 00:30:35.396",
    "video_url": "https://dashscope-result-sh.oss-accelerate.aliyuncs.com/xxx.mp4"
  },
  "usage": {
    "duration": 10.0,
    "size": "1280*720",
    "input_video_duration": 5,
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
| wan2.6-r2v-flash | 有声视频（audio=true） | 720P | 0.3 元/秒 | 50 秒 |
| wan2.6-r2v-flash | 有声视频（audio=true） | 1080P | 0.5 元/秒 | 50 秒 |
| wan2.6-r2v-flash | 无声视频（audio=false） | 720P | 0.15 元/秒 | 50 秒 |
| wan2.6-r2v-flash | 无声视频（audio=false） | 1080P | 0.25 元/秒 | 50 秒 |
| wan2.6-r2v | 有声视频 | 720P | 0.6 元/秒 | 50 秒 |
| wan2.6-r2v | 有声视频 | 1080P | 1 元/秒 | 50 秒 |

按成功生成的视频秒数计费。视频 URL 24 小时内有效，请及时下载。建议轮询间隔 15 秒，处理时间通常 1~5 分钟。

## 数据来源

- API 参考：https://help.aliyun.com/zh/model-studio/wan-video-to-video-api-reference
- 计费信息：https://help.aliyun.com/zh/model-studio/model-pricing
