---
title: Wan2.6 参考生视频
provider: alibaba
model_id: wan2.6-r2v-flash / wan2.6-r2v
task: 参考生视频 (reference-to-video)
---

# Wan2.6 参考生视频

> 基于 Wan2.6 大模型的参考生视频服务，支持以图片和视频作为参考素材生成新视频，支持 720P/1080P 分辨率，视频时长 2-10 秒。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `wan2.6-r2v-flash` / `wan2.6-r2v` |
| 任务类型 | 参考生视频 (reference-to-video) |
| 输入 | 参考素材（图片 0-5 张 + 视频 0-3 个，总计 ≤5）+ 文本提示词 |
| 输出 | 视频 (mp4) |
| 视频时长 | 2-10 秒 |
| 视频分辨率 | 720P / 1080P（默认 1920*1080） |

### 支持的分辨率

| 分辨率等级 | 尺寸 |
|-----------|------|
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
| model | string | 是 | - | 模型ID：`wan2.6-r2v-flash` 或 `wan2.6-r2v` |
| input.prompt | string | 是 | - | 文本提示词，最长 1500 字符 |
| input.reference_urls | array[string] | 是 | - | 参考素材 URL 列表（图片 0-5 张，视频 0-3 个，总计 ≤5） |
| input.negative_prompt | string | 否 | - | 负向提示词，最长 500 字符 |
| parameters.size | string | 否 | `1920*1080` | 视频分辨率，格式为 `宽*高` |
| parameters.duration | integer | 否 | 5 | 视频时长，范围 2-10 秒 |
| parameters.shot_type | string | 否 | `single` | 镜头模式：`single`（单镜头）/ `multi`（多镜头） |
| parameters.audio | bool | 否 | true | 是否自动生成音频（仅 wan2.6-r2v-flash） |
| parameters.watermark | bool | 否 | false | 是否添加 AI 水印 |
| parameters.seed | integer | 否 | - | 随机种子，范围 [0, 2147483647] |

### 请求示例

```bash
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/video-generation/video-synthesis' \
-H 'X-DashScope-Async: enable' \
-H "Authorization: Bearer $DASHSCOPE_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
  "model": "wan2.6-r2v-flash",
  "input": {
    "prompt": "character1在沙发上开心地看电影",
    "reference_urls": ["https://example.com/video.mp4"]
  },
  "parameters": {
    "size": "1280*720",
    "duration": 5,
    "shot_type": "multi"
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
    "size": "1280*720",
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
