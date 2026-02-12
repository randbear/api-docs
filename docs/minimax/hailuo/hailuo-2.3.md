---
title: MiniMax Hailuo-2.3 视频生成
provider: minimax
model_id: MiniMax-Hailuo-2.3
task: text-to-video
---

# MiniMax Hailuo-2.3 视频生成

> MiniMax 海螺 Hailuo-2.3 视频生成模型，支持文生视频和图生视频，更真实的肢体动作和场景动态，电影级运镜。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `MiniMax-Hailuo-2.3` |
| 任务类型 | text-to-video / image-to-video |
| 输入 | 文本 / 图像 + 文本 |
| 输出 | 视频（通过 file_id 下载） |
| 视频时长 | 6 或 10 秒（1080P 仅 6 秒） |
| 视频分辨率 | 768P / 1080P |

## 支持的功能

| 功能 | 说明 |
|------|------|
| 文生视频 (T2V) | 文本描述生成视频 |
| 图生视频 (I2V) | 指定首帧图像生成视频 |
| 运镜控制 | 支持 15 种镜头运动命令（用 `[]` 包裹） |

## API 调用

### 端点

**创建任务（文生视频）：**

`POST https://api.minimax.io/v1/video_generation`

**创建任务（图生视频）：**

`POST https://api.minimax.io/v1/video_generation`

**查询任务状态：**

`GET https://api.minimax.io/v1/query/video_generation?task_id={task_id}`

### 请求头

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Content-Type | string | 是 | `application/json` |
| Authorization | string | 是 | `Bearer $MINIMAX_API_KEY` |

### 请求参数（文生视频）

| 参数 | 类型 | 必填 | 默认值 | 取值范围 | 说明 |
|------|------|------|--------|----------|------|
| model | string | 是 | — | `MiniMax-Hailuo-2.3` | 模型ID |
| prompt | string | 是 | — | 最长 2000 字符 | 文本提示词，支持 `[]` 运镜命令 |
| prompt_optimizer | boolean | 否 | true | true/false | 自动优化提示词 |
| fast_pretreatment | boolean | 否 | false | true/false | 减少优化时间 |
| duration | integer | 否 | 6 | 6 或 10（1080P 仅 6） | 视频时长（秒） |
| resolution | string | 否 | — | `768P` / `1080P` | 视频分辨率 |
| callback_url | string | 否 | — | URL | 异步回调 URL |

### 请求参数（图生视频）

| 参数 | 类型 | 必填 | 默认值 | 取值范围 | 说明 |
|------|------|------|--------|----------|------|
| model | string | 是 | — | `MiniMax-Hailuo-2.3` | 模型ID |
| first_frame_image | string | 是 | — | URL 或 base64 | 首帧图像 |
| prompt | string | 否 | — | 最长 2000 字符 | 文本提示词 |
| prompt_optimizer | boolean | 否 | true | true/false | 自动优化提示词 |
| fast_pretreatment | boolean | 否 | false | true/false | 减少优化时间 |
| duration | integer | 否 | 6 | 6 或 10（1080P 仅 6） | 视频时长（秒） |
| resolution | string | 否 | — | `768P` / `1080P` | 视频分辨率 |
| callback_url | string | 否 | — | URL | 异步回调 URL |

### 输入图像要求

| 属性 | 要求 |
|------|------|
| 格式 | JPG, JPEG, PNG, WebP |
| 文件大小 | 最大 20MB |
| 分辨率 | 短边 > 300px |
| 宽高比 | 2:5 ~ 5:2 |

### 请求示例（文生视频）

```bash
curl -X POST 'https://api.minimax.io/v1/video_generation' \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "MiniMax-Hailuo-2.3",
    "prompt": "一位舞者在雨中起舞，灯光闪烁",
    "duration": 6,
    "resolution": "1080P"
  }'
```

### 请求示例（图生视频）

```bash
curl -X POST 'https://api.minimax.io/v1/video_generation' \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "MiniMax-Hailuo-2.3",
    "first_frame_image": "https://example.com/input.jpg",
    "prompt": "画面缓缓动起来，花瓣飘落",
    "duration": 6,
    "resolution": "1080P"
  }'
```

### 查询任务状态

```bash
curl -X GET 'https://api.minimax.io/v1/query/video_generation?task_id=176843862716480' \
  -H "Authorization: Bearer $MINIMAX_API_KEY"
```

### 响应示例（任务创建）

```json
{
  "task_id": "176843862716480",
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  }
}
```

### 响应示例（任务完成）

```json
{
  "task_id": "176843862716480",
  "status": "Success",
  "file_id": "176844028768320",
  "video_width": 1920,
  "video_height": 1080,
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  }
}
```

### 任务状态

| 状态 | 说明 |
|------|------|
| Preparing | 准备中 |
| Queueing | 排队中 |
| Processing | 生成中 |
| Success | 成功 |
| Fail | 失败 |

## 计费

| 分辨率 | 时长 | 价格（元/视频） |
|--------|------|------------------|
| 768P | 6s | 2.00 |
| 768P | 10s | 4.00 |
| 1080P | 6s | 3.50 |

生成失败或触发安全审核的视频不计费。视频通过 file_id 获取，请及时下载。

## 数据来源

- API 参考（文生视频）：https://platform.minimax.io/docs/api-reference/video-generation-t2v
- API 参考（图生视频）：https://platform.minimax.io/docs/api-reference/video-generation-i2v
- API 参考（查询任务）：https://platform.minimax.io/docs/api-reference/video-generation-query
- 计费信息：https://platform.minimaxi.com/docs/pricing/pay-as-you-go
