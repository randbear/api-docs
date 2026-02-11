---
title: Wan2.6 图生视频
provider: alibaba
model_id: wan2.6-i2v / wan2.6-i2v-flash
task: 图生视频 (image-to-video)
---

# Wan2.6 图生视频

> 基于 Wan2.6 大模型的图片生成视频服务，以图片作为首帧生成视频，支持 720P/1080P 分辨率，视频时长 2-15 秒。Flash 版本支持自动生成音频。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `wan2.6-i2v`（标准版）/ `wan2.6-i2v-flash`（快速版，支持音频生成） |
| 任务类型 | 图生视频 (image-to-video) |
| 输入 | 图片（首帧）+ 可选文本提示词 |
| 输出 | 视频 (mp4) |
| 视频时长 | 2-15 秒 |
| 视频分辨率 | 720P / 1080P（默认 1080P） |

### 支持的图片格式

JPEG, JPG, PNG（不支持透明通道）, BMP, WEBP

图片要求：短边 360-2000px，文件大小 ≤10MB。

## API 调用

### 端点

**创建任务（必须使用异步模式）：**

```
POST https://dashscope.aliyuncs.com/api/v1/services/aigc/video-generation/video-synthesis
```

> 请求头必须包含 `X-DashScope-Async: enable` 以启用异步模式。

**查询任务结果：**

```
GET https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}
```

> 建议每 15 秒轮询一次，QPS 限制为 20。结果链接有效期 24 小时。

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| model | string | 是 | - | 模型ID：`wan2.6-i2v` 或 `wan2.6-i2v-flash` |
| input.img_url | string | 是 | - | 首帧图片 URL 或 Base64，短边 360-2000px，≤10MB |
| input.prompt | string | 否 | - | 文本提示词，最长 1500 字符 |
| input.negative_prompt | string | 否 | - | 负向提示词，最长 500 字符 |
| input.audio_url | string | 否 | - | 音频 URL，支持 mp3/wav，时长 3-30 秒，≤15MB |
| input.template | string | 否 | - | 视频特效模板（使用后 prompt 失效） |
| parameters.resolution | string | 否 | `1080P` | 视频分辨率：`720P` / `1080P` |
| parameters.duration | integer | 否 | 5 | 视频时长，范围 2-15 秒 |
| parameters.prompt_extend | bool | 否 | true | 是否开启智能改写 |
| parameters.shot_type | string | 否 | `single` | 镜头模式：`single` / `multi`（仅 wan2.6-i2v） |
| parameters.audio | bool | 否 | true | 是否自动生成音频（仅 wan2.6-i2v-flash） |
| parameters.watermark | bool | 否 | false | 是否添加 AI 水印 |
| parameters.seed | integer | 否 | - | 随机种子，范围 [0, 2147483647] |

### 请求示例

```bash
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/video-generation/video-synthesis' \
 -H 'X-DashScope-Async: enable' \
 -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
 -H 'Content-Type: application/json' \
 -d '{
  "model": "wan2.6-i2v",
  "input": {
    "prompt": "一只猫在草地上奔跑",
    "img_url": "https://example.com/image.png"
  },
  "parameters": {
    "resolution": "1080P",
    "duration": 5,
    "prompt_extend": true
  }
}'
```

### 异步获取结果

```bash
curl -X GET \
 'https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}' \
 -H "Authorization: Bearer $DASHSCOPE_API_KEY"
```

### 响应示例

**创建任务响应：**

```json
{
  "output": {
    "task_status": "PENDING",
    "task_id": "xxx"
  },
  "request_id": "xxx"
}
```

**查询结果（成功）：**

```json
{
  "output": {
    "task_id": "xxx",
    "task_status": "SUCCEEDED",
    "video_url": "https://...mp4",
    "orig_prompt": "..."
  },
  "usage": {
    "duration": 5,
    "size": "1080P",
    "output_video_duration": 5
  }
}
```

> 响应中的视频 URL 有效期为 24 小时，请及时下载保存。

## 计费

| 分辨率 | 价格 |
|--------|------|
| 720P | 0.6 元/秒 |
| 1080P | 1 元/秒 |
