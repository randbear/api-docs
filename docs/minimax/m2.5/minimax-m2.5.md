---
title: MiniMax M2.5 文本生成
provider: minimax
model_id: MiniMax-M2.5
task: chat
---

# MiniMax M2.5 文本生成

> MiniMax 当前旗舰文本模型，面向复杂编程、Agent 工作流和复杂任务场景，支持 204,800 tokens 上下文窗口，官方标注输出速度约 100 tps。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `MiniMax-M2.5` |
| 任务类型 | 对话（Chat）/ 文本生成 / Agent |
| 输入 | 文本 / 工具调用结果 |
| 输出 | 文本 / 推理内容 |
| 上下文窗口 | 204,800 tokens |
| 输出速度 | 约 100 tps |
| 多模态输入 | 暂不支持图片 / 文档 |

## 支持的能力

| 能力 | 支持 |
|------|------|
| 深度思考 | 是 |
| 流式输出 | 是 |
| 工具调用 | 是 |
| Anthropic 兼容 | 是（官方推荐） |
| OpenAI 兼容 | 是 |
| 图片 / 文档输入 | 否 |

## API 调用

### 推荐方式

官方推荐通过 Anthropic 兼容接口调用，也支持 OpenAI 兼容接口。若需要直接发送 HTTP 请求，官方仍提供 `POST /v1/text/chatcompletion_v2`，但该接口已标记为 deprecated。

### 端点

| 接口 | 端点 | 说明 |
|------|------|------|
| Anthropic 兼容 | `https://api.minimax.io/anthropic` | 官方推荐的兼容基址 |
| OpenAI 兼容 | `https://api.minimax.io/v1` | OpenAI SDK 兼容基址 |
| 标准 HTTP | `POST https://api.minimax.io/v1/text/chatcompletion_v2` | 官方 API 参考提供，已标记 deprecated |

### 请求头

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Authorization | string | 是 | `Bearer $MINIMAX_API_KEY` |
| Content-Type | string | 是 | 固定为 `application/json` |

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| model | string | 是 | - | 模型 ID，`MiniMax-M2.5` |
| messages | object[] | 是 | - | 对话消息列表；兼容接口支持文本与工具调用结果，不支持图片 / 文档输入 |
| stream | boolean | 否 | false | 是否启用流式输出 |
| max_tokens | integer | 否 | - | 已 deprecated，建议改用 `max_completion_tokens` |
| max_completion_tokens | integer | 否 | - | 生成输出的最大 token 数，范围 `x >= 1` |
| temperature | number | 否 | 推荐 1.0 | 随机度控制，范围 `(0, 1]` |
| top_p | number | 否 | 0.95 | 核采样参数，范围 `(0, 1]` |
| tool_choice | string | 否 | auto | 工具调用策略，支持 `none` / `auto` |
| tools | object[] | 否 | - | 工具定义列表 |
| stream_options | object | 否 | - | 流式输出选项 |
| mask_sensitive_info | boolean | 否 | false | 是否对输出中的敏感信息打码 |

`response_format` 在官方文档中标注仅 `MiniMax-Text-01` 支持，因此不适用于 `MiniMax-M2.5`。

### 请求示例

```bash
curl -X POST 'https://api.minimax.io/v1/text/chatcompletion_v2' \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "MiniMax-M2.5",
    "messages": [
      {
        "role": "user",
        "name": "user",
        "content": "请写一个 Python 函数，返回斐波那契数列前 10 项。"
      }
    ],
    "max_completion_tokens": 1000,
    "temperature": 1,
    "top_p": 0.95
  }'
```

### 响应示例

```json
{
  "id": "04ecb5d9b1921ae0fb0e8da9017a5474",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "role": "assistant",
        "name": "MiniMax AI",
        "content": "下面是一个返回前 10 项斐波那契数列的 Python 函数。",
        "reasoning_content": "...omitted"
      }
    }
  ],
  "created": 1755153113,
  "model": "MiniMax-M2.5",
  "object": "chat.completion",
  "usage": {
    "total_tokens": 249,
    "prompt_tokens": 26,
    "completion_tokens": 223,
    "completion_tokens_details": {
      "reasoning_tokens": 214
    }
  },
  "base_resp": {
    "status_code": 0,
    "status_msg": ""
  }
}
```

### 多轮与工具调用注意事项

- 在多轮函数调用对话中，必须把模型完整响应追加回对话历史，避免推理链中断。
- 使用 OpenAI 兼容接口时，可以通过 `reasoning_split=true` 将思考内容拆分到 `reasoning_details` 字段。
- 使用 Anthropic 兼容接口时，应保留完整 `response.content` 列表，其中可能包含 `thinking`、`text`、`tool_use` 和 `tool_result` 内容块。

## 计费

按 token 计费，单位为美元 / 百万 tokens。

| 项目 | 价格 |
|------|------|
| 输入 | $0.3 / M tokens |
| 输出 | $1.2 / M tokens |
| Prompt Cache 读取 | $0.03 / M tokens |
| Prompt Cache 写入 | $0.375 / M tokens |

计费说明：

- 计费项为输入与输出 token 数。
- 官方估算约 1000 tokens 对应 1600 个中文字符，实际消耗以真实请求为准。

## 速率限制

| 指标 | 限制 |
|------|------|
| RPM | 500 |
| TPM | 20,000,000 |

## 数据来源

- 文本生成指南：https://platform.minimax.io/docs/guides/text-generation
- Compatible Anthropic API：https://platform.minimax.io/docs/api-reference/text-anthropic-api
- Compatible OpenAI API：https://platform.minimax.io/docs/api-reference/text-openai-api
- Text Generation（deprecated HTTP 接口）：https://platform.minimax.io/docs/api-reference/text-post
- Pay as You Go：https://platform.minimax.io/docs/guides/pricing-paygo
- Rate Limits：https://platform.minimax.io/docs/guides/rate-limits
