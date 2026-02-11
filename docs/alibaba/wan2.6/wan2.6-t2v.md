---
title: Wan2.6 文生视频
provider: alibaba
model_id: wan2.6-t2v
task: 文生视频 (text-to-video)
---

# Wan2.6 文生视频

> 基于 Wan2.6 大模型的文本生成视频服务，支持 480P/720P/1080P 多种分辨率，视频时长 2-15 秒，支持音频输入与多镜头模式。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `wan2.6-t2v` |
| 任务类型 | 文生视频 (text-to-video) |
| 输入 | 文本提示词 |
| 输出 | 视频 (mp4) |
| 视频时长 | 2-15 秒（任意整数） |
| 视频分辨率 | 480P / 720P / 1080P（默认 1920*1080） |

### 支持的分辨率

| 分辨率等级 | 尺寸 |
|-----------|------|
| 480P | 832*480, 480*832, 624*624 |
| 720P | 1280*720, 720*1280, 960*960, 1088*832, 832*1088 |
| 1080P | 1920*1080（默认）, 1080*1920, 1440*1440, 1632*1248, 1248*1632 |

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
| model | string | 是 | - | 模型ID，固定为 `wan2.6-t2v` |
| input.prompt | string | 是 | - | 文本提示词，最长 1500 字符 |
| input.negative_prompt | string | 否 | - | 负向提示词，最长 500 字符 |
| input.audio_url | string | 否 | - | 音频 URL，支持 mp3/wav，时长 3-30 秒，≤15MB |
| parameters.size | string | 否 | `1920*1080` | 视频分辨率，格式为 `宽*高` |
| parameters.duration | integer | 否 | 5 | 视频时长，范围 2-15 秒 |
| parameters.prompt_extend | bool | 否 | true | 是否开启智能改写 |
| parameters.shot_type | string | 否 | `single` | 镜头模式：`single`（单镜头）/ `multi`（多镜头） |
| parameters.watermark | bool | 否 | false | 是否添加 AI 水印 |
| parameters.seed | integer | 否 | - | 随机种子，范围 [0, 2147483647] |

### 请求示例

```bash
curl 'https://dashscope.aliyuncs.com/api/v1/services/aigc/video-generation/video-synthesis' \
 -H 'X-DashScope-Async: enable' \
 -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
 -H 'Content-Type: application/json' \
 -d '{
  "model": "wan2.6-t2v",
  "input": {
    "prompt": "一只小猫在月光下奔跑",
    "negative_prompt": "低质量"
  },
  "parameters": {
    "size": "1280*720",
    "duration": 10,
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
    "duration": 10,
    "size": "1280*720",
    "output_video_duration": 10
  }
}
```

> 响应中的视频 URL 有效期为 24 小时，请及时下载保存。

## 计费

| 分辨率 | 价格 |
|--------|------|
| 720P | 0.6 元/秒 |
| 1080P | 1 元/秒 |
