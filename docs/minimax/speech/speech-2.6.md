---
title: MiniMax Speech 2.6 语音合成
provider: minimax
model_id: speech-2.6-hd / speech-2.6-turbo
task: text-to-speech
---

# MiniMax Speech 2.6 语音合成

> MiniMax Speech 2.6 语音合成模型，优秀韵律和自然节奏，支持 fluent/whisper 情绪模式，40+ 语言。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `speech-2.6-hd`（高清，~60tps）/ `speech-2.6-turbo`（快速） |
| 任务类型 | text-to-speech |
| 输入 | 文本（最长 10000 字符，异步最长 5 万字符） |
| 输出 | 音频（MP3/PCM/FLAC/WAV） |
| 支持语言 | 40+ 语言 |
| 音色 | 300+ 系统音色 / 克隆音色 / 文生音色 |

## API 调用

### 同步语音合成

#### 端点

`POST https://api.minimaxi.com/v1/t2a_v2`

备用域名：`https://api-bj.minimaxi.com/v1/t2a_v2`

#### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 取值范围 | 说明 |
|------|------|------|--------|----------|------|
| model | string | 是 | — | `speech-2.6-hd` / `speech-2.6-turbo` | 模型ID |
| text | string | 是 | — | ≤10000 字符 | 合成文本，>3000 字符建议流式 |
| stream | boolean | 否 | false | true/false | 是否流式输出 |
| voice_setting | object | 是 | — | — | 音色设置 |
| voice_setting.voice_id | string | 是 | — | 系统/克隆/文生音色ID | 音色编号 |
| voice_setting.speed | float | 否 | 1.0 | 0.5 ~ 2.0 | 语速 |
| voice_setting.vol | float | 否 | 1.0 | (0, 10] | 音量 |
| voice_setting.pitch | integer | 否 | 0 | -12 ~ 12 | 语调 |
| voice_setting.emotion | string | 否 | auto | happy/sad/angry/fearful/disgusted/surprised/calm/fluent/whisper | 情绪 |
| audio_setting | object | 否 | — | — | 音频设置 |
| audio_setting.sample_rate | integer | 否 | 32000 | 8000/16000/22050/24000/32000/44100 | 采样率 |
| audio_setting.bitrate | integer | 否 | 128000 | 32000/64000/128000/256000 | 比特率（仅 MP3） |
| audio_setting.format | string | 否 | mp3 | mp3/pcm/flac/wav | 音频格式（wav 仅非流式） |
| audio_setting.channel | integer | 否 | 1 | 1/2 | 声道数 |
| subtitle_enable | boolean | 否 | false | true/false | 启用字幕 |
| output_format | string | 否 | hex | url/hex | 输出形式 |
| pronunciation_dict | object | 否 | — | — | 发音规则字典 |
| timbre_weights | array | 否 | — | 最多 4 种音色 | 音色混合权重 |
| language_boost | string | 否 | null | 语言代码/auto | 小语种识别增强 |
| voice_modify | object | 否 | — | — | 声音效果器 |
| voice_modify.pitch | integer | 否 | — | -100 ~ 100 | 音高调整 |
| voice_modify.intensity | integer | 否 | — | -100 ~ 100 | 强度调整 |
| voice_modify.timbre | integer | 否 | — | -100 ~ 100 | 音色调整 |
| voice_modify.sound_effects | string | 否 | — | spacious_echo/auditorium_echo/lofi_telephone/robotic | 音效 |
| text_normalization | boolean | 否 | false | true/false | 文本规范化 |
| latex_read | boolean | 否 | false | true/false | LaTeX 公式朗读 |
| aigc_watermark | boolean | 否 | false | true/false | 音频标识 |

#### 请求示例

```bash
curl -X POST https://api.minimaxi.com/v1/t2a_v2 \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "speech-2.6-hd",
    "text": "欢迎使用 MiniMax 语音合成服务。",
    "stream": false,
    "voice_setting": {
      "voice_id": "male-qn-qingse",
      "speed": 1,
      "vol": 1,
      "pitch": 0,
      "emotion": "calm"
    },
    "audio_setting": {
      "sample_rate": 32000,
      "bitrate": 128000,
      "format": "mp3",
      "channel": 1
    }
  }'
```

#### 响应示例

```json
{
  "data": {
    "audio": "<hex编码音频数据>",
    "status": 2
  },
  "extra_info": {
    "audio_length": 5200,
    "audio_sample_rate": 32000,
    "audio_size": 83200,
    "bitrate": 128000,
    "word_count": 18,
    "usage_characters": 15,
    "audio_format": "mp3",
    "audio_channel": 1
  },
  "trace_id": "...",
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  }
}
```

### 异步长文本语音合成

#### 端点

**创建任务：** `POST https://api.minimaxi.com/v1/t2a_async_v2`

**查询任务：** `GET https://api.minimaxi.com/v1/query/t2a_async_query_v2?task_id={task_id}`

#### 请求参数（创建任务）

| 参数 | 类型 | 必填 | 默认值 | 取值范围 | 说明 |
|------|------|------|--------|----------|------|
| model | string | 是 | — | `speech-2.6-hd` / `speech-2.6-turbo` | 模型ID |
| text | string | 二选一 | — | ≤5 万字符 | 待合成文本 |
| text_file_id | integer | 二选一 | — | ≤10 万字符 | 文本文件ID（txt/zip） |
| voice_setting | object | 是 | — | — | 音色设置（同同步接口） |
| audio_setting | object | 否 | — | — | 音频设置（同同步接口，不支持 wav） |
| pronunciation_dict | object | 否 | — | — | 发音字典 |
| language_boost | string | 否 | null | auto/语言代码 | 小语种增强 |
| voice_modify | object | 否 | — | — | 声音效果器 |
| aigc_watermark | boolean | 否 | false | — | 音频标识 |

#### 请求示例

```bash
curl -X POST https://api.minimaxi.com/v1/t2a_async_v2 \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "speech-2.6-hd",
    "text": "这是一段需要合成的长文本内容...",
    "voice_setting": {
      "voice_id": "audiobook_male_1",
      "speed": 1,
      "vol": 1,
      "pitch": 0
    },
    "audio_setting": {
      "audio_sample_rate": 32000,
      "bitrate": 128000,
      "format": "mp3"
    }
  }'
```

#### 任务状态

| 状态 | 说明 |
|------|------|
| Processing | 处理中 |
| Success | 完成 |
| Failed | 失败 |
| Expired | 已过期 |

查询频率限制：每秒最多 10 次。下载 URL 自生成起 9 小时内有效。

## 计费

### 按量付费

| 模型 | 价格 |
|------|------|
| speech-2.6-hd | ¥3.5/万字符 |
| speech-2.6-turbo | ¥2/万字符 |

计费单位：1 个汉字算 2 个字符，英文字母、标点、空格等算 1 个字符。

### 资源包

| 模型系列 | 套餐 | 价格 | 字符额度 | RPM | 赠送克隆音色 |
|----------|------|------|---------|-----|------------|
| HD | 月 | ¥630 | 200 万 | 60 | 10 个 |
| HD | 季度 | ¥5,950 | 2000 万 | 200 | 30 个 |
| HD | 年度 | ¥56,000 | 2 亿 | 500 | 300 个 |
| Turbo | 月 | ¥360 | 200 万 | 60 | 10 个 |
| Turbo | 季度 | ¥3,400 | 2000 万 | 200 | 30 个 |
| Turbo | 年度 | ¥32,000 | 2 亿 | 500 | 300 个 |

## 数据来源

- 同步语音合成 API：https://platform.minimaxi.com/docs/api-reference/speech-t2a-http
- 异步长文本 API：https://platform.minimaxi.com/docs/api-reference/speech-t2a-async-create
- 异步任务查询 API：https://platform.minimaxi.com/docs/api-reference/speech-t2a-async-query
- 计费信息：https://platform.minimaxi.com/docs/guides/pricing
