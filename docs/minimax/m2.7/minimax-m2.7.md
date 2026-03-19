---
title: MiniMax M2.7 文本生成
provider: minimax
model_id: MiniMax-M2.7
task: chat
---

# MiniMax M2.7 文本生成

> MiniMax 当前主力文本模型之一，官方描述为“Beginning the journey of recursive self-improvement”，强调真实工程任务、专业办公交付和更强的角色交互能力。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型 ID | `MiniMax-M2.7` |
| 任务类型 | 对话（Chat）/ 文本生成 / Agent |
| 输入 | 文本 / 工具调用结果 |
| 输出 | 文本 / 推理内容 |
| 上下文窗口 | 204,800 tokens |
| 输出速度 | 约 60 tps |
| 多模态输入 | 暂不支持图片 / 文档 |

## 支持的能力

| 能力 | 支持 |
|------|------|
| 深度思考 | 是 |
| 流式输出 | 是 |
| 工具调用 | 是 |
| Prompt Caching | 是（Anthropic 兼容接口） |
| Anthropic 兼容 | 是（官方推荐） |
| OpenAI 兼容 | 是 |
| 图片 / 文档输入 | 否 |

## 适用场景

根据官方 models 与 AI coding tools 页面，`MiniMax-M2.7` 重点面向以下场景：

- 真实工程任务
- 专业办公交付
- 角色感更强的多轮交互
- 代码理解、代码生成与推理任务

## API 调用

### 推荐方式

官方当前推荐优先使用 Anthropic 兼容接口，也支持 OpenAI 兼容接口。

### 端点

| 接口 | 基础地址 | 说明 |
|------|------|------|
| Anthropic 兼容 | `https://api.minimax.io/anthropic` | 官方推荐 |
| OpenAI 兼容 | `https://api.minimax.io/v1` | 适合 OpenAI SDK / Chat Completions 生态 |
| 中国大陆可选地址 | `https://api.minimaxi.com/anthropic` / `https://api.minimaxi.com/v1` | 官方在 M2.7 coding tools 指南中给出的中国区地址 |

### 请求头

OpenAI 兼容接口通常使用以下请求头：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Authorization | string | 是 | `Bearer $MINIMAX_API_KEY` |
| Content-Type | string | 是 | 固定为 `application/json` |

### 请求参数

以下参数表以官方 Anthropic 兼容接口支持矩阵为准；OpenAI 兼容接口调用时，字段名与 OpenAI Chat Completions 生态保持一致。

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| model | string | 是 | - | 模型 ID，`MiniMax-M2.7` |
| messages | object[] | 是 | - | 消息列表；支持文本与工具调用结果，不支持图片 / 文档输入 |
| max_tokens | integer | 否 | - | 最大生成 token 数 |
| stream | boolean | 否 | false | 是否启用流式输出 |
| system | string | 否 | - | System prompt |
| temperature | number | 否 | 推荐 1 | 随机度，范围 `(0.0, 1.0]` |
| tool_choice | string / object | 否 | auto | 工具选择策略 |
| tools | object[] | 否 | - | 工具定义列表 |
| top_p | number | 否 | - | Nucleus sampling 参数 |
| metadata | object | 否 | - | 元数据 |
| thinking | object / boolean | 否 | - | 推理内容控制；官方标记为 Fully Supported |
| reasoning_split | boolean | 否 | false | OpenAI 兼容接口的附加参数；为 `true` 时将推理内容拆分到 `reasoning_details` |

以下参数在 Anthropic 兼容接口中会被忽略：

- `top_k`
- `stop_sequences`
- `service_tier`
- `mcp_servers`
- `context_management`
- `container`

### 消息内容类型支持

| 类型 | 支持状态 | 说明 |
|------|------|------|
| `text` | 支持 | 文本消息 |
| `tool_use` | 支持 | 工具调用 |
| `tool_result` | 支持 | 工具返回结果 |
| `thinking` | 支持 | 推理内容 |
| `image` | 不支持 | 图片输入暂不支持 |
| `document` | 不支持 | 文档输入暂不支持 |

### 请求示例

说明：官方兼容文档主要提供 SDK 示例，没有直接给出 curl 版本。下面 REST 路径按官方给出的 OpenAI 兼容基础地址 `https://api.minimax.io/v1` 和 Chat Completions 标准接口约定整理。

```bash
curl -X POST 'https://api.minimax.io/v1/chat/completions' \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "MiniMax-M2.7",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "请写一个 Python 函数，返回斐波那契数列前 10 项。"
      }
    ],
    "temperature": 1,
    "stream": false,
    "reasoning_split": true
  }'
```

### 响应示例

说明：官方 OpenAI 兼容文档展示的是 SDK 读取方式，而非原始 HTTP JSON。下面示例按官方示例中出现的 `choices[].message.content` 与 `choices[].message.reasoning_details` 字段整理。

```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "下面是一个返回前 10 项斐波那契数列的 Python 函数。",
        "reasoning_details": [
          {
            "text": "先分析需求，再生成代码。"
          }
        ]
      },
      "finish_reason": "stop"
    }
  ],
  "model": "MiniMax-M2.7"
}
```

### 多轮与工具调用注意事项

- 使用 Anthropic 兼容接口时，必须把完整 `response.content` 列表追加回历史消息，包含 `thinking`、`text`、`tool_use` 等内容块。
- 使用 OpenAI 兼容接口时，必须把完整 assistant message 追加回历史消息，包含 `tool_calls` 字段。
- 若 OpenAI 兼容接口启用 `reasoning_split=true`，则 `reasoning_details` 也必须完整保留并传回下一轮。
- 若不启用 `reasoning_split`，模型思考内容会放进 `content` 字段中的 `<think>...</think>` 标签，不能裁剪或改写。

## 计费

MiniMax 平台支持 `Token Plan` 和 `Pay-As-You-Go` 两种计费方式；官方说明最终计费模式取决于你使用的 API Key。以下价格为官方按量计费页公开值。

| 项目 | 价格 |
|------|------|
| 输入 | $0.3 / M tokens |
| 输出 | $1.2 / M tokens |
| Prompt Cache 读取 | $0.06 / M tokens |
| Prompt Cache 写入 | $0.375 / M tokens |

计费说明：

- 计费项为输入与输出 token 数。
- 官方估算约 1000 tokens 对应 1600 个中文字符。
- Prompt caching 缓存内容生命周期为 5 分钟；命中后会自动刷新生命周期，且不额外收费。

## 速率限制

| 指标 | 限制 |
|------|------|
| RPM | 500 |
| TPM | 20,000,000 |

## 数据来源

- Models：https://platform.minimax.io/docs/guides/models-intro
- M2.7 for AI Coding Tools：https://platform.minimax.io/docs/guides/text-ai-coding-tools
- Compatible Anthropic API：https://platform.minimax.io/docs/api-reference/text-anthropic-api
- Compatible OpenAI API：https://platform.minimax.io/docs/api-reference/text-openai-api
- Pay as You Go：https://platform.minimax.io/docs/guides/pricing-paygo
- Explicit Prompt Caching (Anthropic API)：https://platform.minimax.io/docs/api-reference/anthropic-api-compatible-cache
- Rate Limits：https://platform.minimax.io/docs/guides/rate-limits
