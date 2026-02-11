---
title: Seedance 1.0 Lite 图生视频
provider: volcengine
model_id: doubao-seedance-1-0-lite-i2v-250428
task: image-to-video
---

# Seedance 1.0 Lite 图生视频

> 火山方舟豆包 Seedance 1.0 Lite 图生视频模型，支持首帧、首尾帧、参考图（最多4张）生成视频，默认 720p。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `doubao-seedance-1-0-lite-i2v-250428` |
| 任务类型 | image-to-video |
| 输入 | 图像 + 文本 |
| 输出 | 视频（URL，24小时有效） |
| 视频时长 | 2~12 秒 |
| 视频分辨率 | 480p / 720p / 1080p |
| 默认分辨率 | 720p |

## 支持的功能

| 功能 | 说明 |
|------|------|
| 图生视频 - 首帧 (i2v) | 指定首帧图像生成视频 |
| 图生视频 - 首尾帧 (i2v) | 指定首尾帧图像生成视频 |
| 图生视频 - 参考图 (i2v) | 指定 1~4 张参考图像生成视频 |

## API 调用

### 端点

**创建任务：**

`POST https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks`

**查询任务结果：**

`GET https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks/{id}`

### 请求头

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Content-Type | string | 是 | `application/json` |
| Authorization | string | 是 | `Bearer $ARK_API_KEY` |

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 取值范围 | 说明 |
|------|------|------|--------|----------|------|
| model | string | 是 | — | `doubao-seedance-1-0-lite-i2v-250428` | 模型ID |
| content | array | 是 | — | — | 输入内容列表 |
| content[].type | string | 是 | — | `text` / `image_url` | 内容类型 |
| content[].text | string | 条件 | — | — | 文本提示词（type=text 时） |
| content[].image_url.url | string | 条件 | — | URL 或 base64 | 图像 URL（type=image_url 时） |
| content[].role | string | 条件 | — | `first_frame` / `last_frame` / `reference_image` | 图像角色 |
| resolution | string | 否 | `720p` | `480p` / `720p` / `1080p` | 视频分辨率 |
| ratio | string | 否 | — | `16:9` / `4:3` / `1:1` / `3:4` / `9:16` / `21:9` | 宽高比 |
| duration | integer | 否 | — | 2~12 | 视频时长（秒） |
| frames | integer | 否 | — | 29~289（满足 25+4n） | 视频帧数 |
| seed | integer | 否 | 随机 | -1~4294967295 | 随机种子 |
| camera_fixed | boolean | 否 | — | true/false | 是否固定镜头 |
| watermark | boolean | 否 | false | true/false | 是否添加水印 |
| return_last_frame | boolean | 否 | false | true/false | 是否返回尾帧图像 |
| service_tier | string | 否 | `default` | `default` / `flex` | 服务等级（flex 价格为 50%） |
| callback_url | string | 否 | — | URL | 任务完成回调 URL |
| execution_expires_after | integer | 否 | 172800 | — | 任务超时阈值（秒） |

### 输入图像要求

| 属性 | 要求 |
|------|------|
| 格式 | JPEG, PNG, WEBP, BMP, TIFF, GIF |
| 宽高比 | 0.4~2.5 |
| 分辨率 | 300~6000 像素（宽和高） |
| 文件大小 | 最大 30MB |

### 请求示例（首帧图生视频）

```bash
curl -X POST 'https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks' \
  -H "Authorization: Bearer $ARK_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "doubao-seedance-1-0-lite-i2v-250428",
    "content": [
      {"type": "text", "text": "画面中的人物缓缓转头微笑"},
      {"type": "image_url", "image_url": {"url": "https://example.com/first.jpg"}, "role": "first_frame"}
    ],
    "resolution": "720p",
    "ratio": "16:9",
    "duration": 5
  }'
```

### 请求示例（参考图生视频）

```bash
curl -X POST 'https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks' \
  -H "Authorization: Bearer $ARK_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "doubao-seedance-1-0-lite-i2v-250428",
    "content": [
      {"type": "text", "text": "参考图中的角色在城市街道上行走"},
      {"type": "image_url", "image_url": {"url": "https://example.com/ref1.jpg"}, "role": "reference_image"},
      {"type": "image_url", "image_url": {"url": "https://example.com/ref2.jpg"}, "role": "reference_image"}
    ],
    "resolution": "720p",
    "ratio": "16:9",
    "duration": 5
  }'
```

### 查询任务结果

```bash
curl -X GET 'https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks/{id}' \
  -H "Authorization: Bearer $ARK_API_KEY" \
  -H 'Content-Type: application/json'
```

### 响应示例（任务完成）

```json
{
  "id": "cgt-2025******-****",
  "model": "doubao-seedance-1-0-lite-i2v-250428",
  "status": "succeeded",
  "content": {
    "video_url": "https://ark-content-generation-cn-beijing.tos-cn-beijing.volces.com/xxx.mp4"
  },
  "usage": {
    "completion_tokens": 108900,
    "total_tokens": 108900
  },
  "created_at": 1743414619,
  "updated_at": 1743415231,
  "seed": 123456,
  "resolution": "720p",
  "ratio": "16:9",
  "duration": 5,
  "framespersecond": 24,
  "service_tier": "default"
}
```

### 任务状态

| 状态 | 说明 |
|------|------|
| queued | 排队中 |
| running | 处理中 |
| succeeded | 成功 |
| failed | 失败 |
| cancelled | 已取消（24h 自动删除） |
| expired | 已超时 |

### Token 用量计算

正常视频：(宽 × 高 × 帧率 × 时长) / 1024

准确用量以 API 返回的 usage 字段为准。

## 计费

| 类型 | 在线推理（元/百万token） | 离线推理（元/百万token） |
|------|--------------------------|--------------------------|
| 视频 | 10.00 | 5.00 |

视频 URL 24 小时内有效，请及时下载。任务 ID 7 天内有效。使用 service_tier=flex 可享受 50% 价格折扣。

## 数据来源

- API 参考（创建任务）：https://www.volcengine.com/docs/82379/1520757
- API 参考（查询任务）：https://www.volcengine.com/docs/82379/1521309
- 计费信息：https://www.volcengine.com/docs/82379/1544106
