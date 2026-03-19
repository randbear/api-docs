---
title: MiniMax 语音克隆
provider: minimax
model_id: voice_clone
task: voice-clone
---

# MiniMax 语音克隆

> MiniMax 语音克隆 API，上传 10 秒 ~ 5 分钟音频即可快速复刻音色，克隆音色可用于所有 Speech 系列模型的语音合成。

## 功能信息

| 属性 | 值 |
|------|-----|
| 任务类型 | voice-clone |
| 输入 | 音频文件（10 秒 ~ 5 分钟） |
| 输出 | 克隆音色 ID + 试听音频 |
| 音色有效期 | 7 天内未调用将被自动删除 |

## API 调用

### 流程

1. 上传音频文件 → 获取 `file_id`
2. 调用克隆接口 → 获取克隆音色 ID
3. 使用克隆音色 ID 进行语音合成

### 端点

**上传音频：** `POST https://api.minimaxi.com/v1/voice_cloning/upload`

**执行克隆：** `POST https://api.minimaxi.com/v1/voice_clone`

### 请求参数（执行克隆）

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| file_id | integer | 是 | — | 上传音频获得的文件 ID |
| voice_id | string | 是 | — | 克隆音色的 ID |
| clone_prompt | object | 否 | — | 包含示例音频和文本 |
| text | string | 否 | — | 试听文本（≤1000 字符） |
| model | string | 否 | — | 试听用合成模型 |
| language_boost | string | 否 | — | 小语种识别增强 |
| need_noise_reduction | boolean | 否 | — | 是否降噪 |
| need_volume_normalization | boolean | 否 | — | 是否音量归一化 |
| aigc_watermark | boolean | 否 | — | 是否添加音频标识 |

### 请求示例

```bash
curl -X POST https://api.minimaxi.com/v1/voice_clone \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "file_id": 123456789,
    "voice_id": "CustomVoice001",
    "text": "这是一段试听文本",
    "model": "speech-2.8-hd"
  }'
```

### 响应示例

```json
{
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  },
  "demo_audio": "试听音频链接"
}
```

## 计费

| 项目 | 价格 |
|------|------|
| 快速复刻 | ¥9.9/音色（首次使用该音色合成时收费） |
| 试听 | 按选定模型的语音合成价格计费 |

资源包套餐赠送快速克隆音色数量（月 10 个，季度 30 个，年度 300 个）。

## 使用说明

- 上传音频时长：10 秒 ~ 5 分钟
- 克隆音色 7 天内未被调用将被系统自动删除
- 克隆后的音色 ID 可在所有 Speech 系列模型中使用

## 数据来源

- 上传音频 API：https://platform.minimaxi.com/docs/api-reference/voice-cloning-uploadcloneaudio
- 克隆执行 API：https://platform.minimaxi.com/docs/api-reference/voice-cloning-clone
