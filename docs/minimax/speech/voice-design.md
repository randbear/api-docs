---
title: MiniMax 语音设计（文生音）
provider: minimax
model_id: voice_design
task: voice-design
---

# MiniMax 语音设计（文生音）

> MiniMax 语音设计 API，通过文字描述生成个性化音色，生成的音色可用于所有 Speech 系列模型的语音合成。

## 功能信息

| 属性 | 值 |
|------|-----|
| 任务类型 | voice-design（文生音） |
| 输入 | 音色描述文本 + 试听文本 |
| 输出 | 音色 ID + 试听音频 |

## API 调用

### 端点

`POST https://api.minimaxi.com/v1/voice_design`

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| prompt | string | 是 | — | 音色描述 |
| preview_text | string | 是 | — | 试听文本（≤500 字符） |
| voice_id | string | 否 | 自动生成 | 自定义音色 ID |
| aigc_watermark | boolean | 否 | false | 是否添加音频标识 |

### 请求示例

```bash
curl -X POST https://api.minimaxi.com/v1/voice_design \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "讲述悬疑故事的播音员，声音低沉富有磁性，语速时快时慢，营造紧张神秘的氛围。",
    "preview_text": "夜深了，古屋里只有他一人。窗外传来若有若无的脚步声，他屏住呼吸，慢慢地走向那扇吱呀作响的门……"
  }'
```

### 响应示例

```json
{
  "voice_id": "ttv-voice-2025060717322425-xxxxxxxx",
  "trial_audio": "<hex编码音频>",
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  }
}
```

## 计费

| 项目 | 价格 |
|------|------|
| 音色设计 | ¥9.9/音色（首次使用该音色合成时收费） |
| 试听 | ¥2/万字符 |

生成的音色 ID 可在所有 Speech 系列模型中作为 `voice_id` 使用。

## 数据来源

- 语音设计 API：https://platform.minimaxi.com/docs/api-reference/voice-design-design
