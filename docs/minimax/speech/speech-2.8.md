---
title: MiniMax Speech 2.8 语音合成
provider: minimax
model_id: speech-2.8-hd / speech-2.8-turbo
task: text-to-speech
---

# MiniMax Speech 2.8 语音合成

> MiniMax 最新一代语音合成模型，精准还原真实语气细节，支持语气词标签插入，40+ 语言，300+ 系统音色。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `speech-2.8-hd`（高清）/ `speech-2.8-turbo`（快速，~100tps） |
| 任务类型 | text-to-speech |
| 输入 | 文本（最长 10000 字符，异步最长 5 万字符） |
| 输出 | 音频（MP3/PCM/FLAC/WAV） |
| 支持语言 | 40+ 语言 |
| 音色 | 300+ 系统音色 / 克隆音色 / 文生音色 |

## 特色功能

- **语气词标签**：在文本中插入语气词，如 `(laughs)`、`(sighs)`、`(coughs)` 等
- **情绪控制**：支持 happy/sad/angry/fearful/disgusted/surprised/calm/fluent/whisper
- **音色混合**：最多混合 4 种音色，自定义权重
- **声音效果器**：调节音高、强度、音色，支持回声/电话/机器人等音效
- **发音字典**：自定义特殊词汇的发音规则
- **LaTeX 朗读**：支持 LaTeX 公式的语音朗读

### 支持的语气词标签

`(laughs)` `(chuckle)` `(coughs)` `(clear-throat)` `(groans)` `(breath)` `(pant)` `(inhale)` `(exhale)` `(gasps)` `(sniffs)` `(sighs)` `(snorts)` `(burps)` `(lip-smacking)` `(humming)` `(hissing)` `(emm)` `(sneezes)`

## API 调用

### 同步语音合成

#### 端点

`POST https://api.minimaxi.com/v1/t2a_v2`

备用域名：`https://api-bj.minimaxi.com/v1/t2a_v2`

#### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 取值范围 | 说明 |
|------|------|------|--------|----------|------|
| model | string | 是 | — | `speech-2.8-hd` / `speech-2.8-turbo` | 模型ID |
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
    "model": "speech-2.8-hd",
    "text": "今天是不是很开心呀(laughs)，当然了！",
    "stream": false,
    "voice_setting": {
      "voice_id": "male-qn-qingse",
      "speed": 1,
      "vol": 1,
      "pitch": 0,
      "emotion": "happy"
    },
    "audio_setting": {
      "sample_rate": 32000,
      "bitrate": 128000,
      "format": "mp3",
      "channel": 1
    },
    "subtitle_enable": false
  }'
```

#### 响应示例（非流式）

```json
{
  "data": {
    "audio": "<hex编码音频数据>",
    "status": 2
  },
  "extra_info": {
    "audio_length": 9900,
    "audio_sample_rate": 32000,
    "audio_size": 160323,
    "bitrate": 128000,
    "word_count": 52,
    "usage_characters": 26,
    "audio_format": "mp3",
    "audio_channel": 1
  },
  "trace_id": "01b8bf9bb7433cc75c18eee6cfa8fe21",
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  }
}
```

#### 响应示例（流式）

```json
{
  "data": {
    "audio": "<hex编码音频片段>",
    "status": 1
  },
  "base_resp": {
    "status_code": 0
  }
}
```

最后一个流式片段 `status` 为 2，附带 `extra_info`。

### 异步长文本语音合成

#### 端点

**创建任务：** `POST https://api.minimaxi.com/v1/t2a_async_v2`

**查询任务：** `GET https://api.minimaxi.com/v1/query/t2a_async_query_v2?task_id={task_id}`

#### 请求参数（创建任务）

| 参数 | 类型 | 必填 | 默认值 | 取值范围 | 说明 |
|------|------|------|--------|----------|------|
| model | string | 是 | — | `speech-2.8-hd` / `speech-2.8-turbo` | 模型ID |
| text | string | 二选一 | — | ≤5 万字符 | 待合成文本 |
| text_file_id | integer | 二选一 | — | ≤10 万字符 | 文本文件ID（txt/zip） |
| voice_setting | object | 是 | — | — | 音色设置（同同步接口） |
| audio_setting | object | 否 | — | — | 音频设置（同同步接口，不支持 wav） |
| pronunciation_dict | object | 否 | — | — | 发音字典 |
| language_boost | string | 否 | null | auto/语言代码 | 小语种增强 |
| voice_modify | object | 否 | — | — | 声音效果器 |
| aigc_watermark | boolean | 否 | false | — | 音频标识 |

#### 请求示例（创建任务）

```bash
curl -X POST https://api.minimaxi.com/v1/t2a_async_v2 \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "speech-2.8-hd",
    "text": "真正的危险不是计算机开始像人一样思考(sighs)，而是人开始像计算机一样思考。",
    "language_boost": "auto",
    "voice_setting": {
      "voice_id": "audiobook_male_1",
      "speed": 1,
      "vol": 1,
      "pitch": 0
    },
    "audio_setting": {
      "audio_sample_rate": 32000,
      "bitrate": 128000,
      "format": "mp3",
      "channel": 2
    }
  }'
```

#### 响应示例（创建任务）

```json
{
  "task_id": "95157322514444",
  "task_token": "eyJhbGciOiJSUz...",
  "file_id": 95157322514444,
  "usage_characters": 101,
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  }
}
```

#### 请求示例（查询任务）

```bash
curl -X GET "https://api.minimaxi.com/v1/query/t2a_async_query_v2?task_id=95157322514444" \
  -H "Authorization: Bearer $MINIMAX_API_KEY"
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
| speech-2.8-hd | ¥3.5/万字符 |
| speech-2.8-turbo | ¥2/万字符 |

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

## 错误码

| 状态码 | 说明 |
|--------|------|
| 0 | 成功 |
| 1000 | 未知错误 |
| 1004 | 鉴权失败 |
| 1042 | 非法字符超过 10% |

## 数据来源

- 同步语音合成 API：https://platform.minimaxi.com/docs/api-reference/speech-t2a-http
- 异步长文本 API：https://platform.minimaxi.com/docs/api-reference/speech-t2a-async-create
- 异步任务查询 API：https://platform.minimaxi.com/docs/api-reference/speech-t2a-async-query
- 计费信息：https://platform.minimaxi.com/docs/guides/pricing
