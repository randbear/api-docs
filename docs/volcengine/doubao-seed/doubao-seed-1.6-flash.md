---
title: doubao-seed-1.6-flash 对话模型
provider: volcengine
model_id: doubao-seed-1-6-flash-250828
task: chat
---

# doubao-seed-1.6-flash 对话模型

> 豆包 seed 1.6 极速版模型，成本最低，支持深度思考、视觉定位、多模态理解，适合高吞吐量场景。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `doubao-seed-1-6-flash-250828` |
| 任务类型 | 对话（Chat） |
| 输入 | 文本 / 图片 / 视频 |
| 输出 | 文本 |
| 上下文窗口 | 256k tokens |
| 最大输入 | 224k tokens |
| 最大回答 | 32k tokens（默认 4k） |
| 最大思维链 | 32k tokens |

## 支持的能力

| 能力 | 支持 |
|------|------|
| 深度思考 | 是 |
| 文本生成 | 是 |
| 视觉定位 | 是 |
| 多模态理解（图片/视频） | 是 |
| 工具调用（Function Calling） | 是 |
| 结构化输出（JSON Schema） | 是 |
| 上下文缓存 | 是 |

## API 调用

### 端点

`POST https://ark.cn-beijing.volces.com/api/v3/chat/completions`

### 请求头

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Content-Type | string | 是 | `application/json` |
| Authorization | string | 是 | `Bearer $ARK_API_KEY` |

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| model | string | 是 | — | `doubao-seed-1-6-flash-250828` |
| messages | object[] | 是 | — | 消息列表（system/user/assistant/tool） |
| thinking | object | 否 | `{"type":"enabled"}` | 深度思考模式：`enabled`/`disabled`/`auto` |
| stream | boolean | 否 | false | 是否流式返回 |
| stream_options | object | 否 | null | 流式选项，`include_usage` 等 |
| max_tokens | integer | 否 | 4096 | 模型回答最大长度（token） |
| max_completion_tokens | integer | 否 | — | 最大输出长度（含思维链），范围 [0, 65536] |
| reasoning_effort | string | 否 | medium | 思考深度：`minimal`/`low`/`medium`/`high` |
| temperature | float | 否 | 1 | 采样温度 |
| top_p | float | 否 | 0.7 | 核采样概率阈值 |
| stop | string/string[] | 否 | null | 停止序列，最多 4 个 |
| frequency_penalty | float | 否 | 0 | 频率惩罚系数，范围 [-2.0, 2.0] |
| presence_penalty | float | 否 | 0 | 存在惩罚系数，范围 [-2.0, 2.0] |
| response_format | object | 否 | `{"type":"text"}` | 回答格式：`text`/`json_object`/`json_schema` |
| tools | object[] | 否 | null | 工具列表（Function Calling） |
| tool_choice | string/object | 否 | auto | 工具选择：`none`/`auto`/`required`/指定函数 |
| parallel_tool_calls | boolean | 否 | true | 是否允许并行工具调用 |
| logprobs | boolean | 否 | false | 是否返回对数概率（深度思考模式不支持） |
| top_logprobs | integer | 否 | 0 | 每个位置返回的最可能 token 数 |
| service_tier | string | 否 | auto | TPM 保障包：`auto`/`default` |

### 请求示例

```bash
curl -X POST 'https://ark.cn-beijing.volces.com/api/v3/chat/completions' \
  -H "Authorization: Bearer $ARK_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "doubao-seed-1-6-flash-250828",
    "messages": [
      {"role": "system", "content": "你是一个有用的助手。"},
      {"role": "user", "content": "你好，请介绍一下你自己。"}
    ]
  }'
```

### 响应示例

```json
{
  "id": "chatcmpl-xxx",
  "model": "doubao-seed-1-6-flash-250828",
  "object": "chat.completion",
  "created": 1700000000,
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "你好！我是豆包..."
      }
    }
  ],
  "usage": {
    "prompt_tokens": 20,
    "completion_tokens": 50,
    "total_tokens": 70,
    "prompt_tokens_details": {"cached_tokens": 0},
    "completion_tokens_details": {"reasoning_tokens": 0}
  }
}
```

## 计费

按 token 用量计费，单位：元/百万 token。价格根据输入长度分层：

| 输入长度（千 token） | 输入单价 | 输出单价 |
|----------------------|----------|----------|
| [0, 32] | 0.15 | 1.50 |
| (32, 128] | 0.30 | 3.00 |
| (128, 256] | 0.60 | 6.00 |

上下文缓存：

| 项目 | 单价（元/百万 token） |
|------|----------------------|
| 缓存存储 | 0.017 / 小时 |
| 缓存输入 | 0.03 |

## 速率限制

| 指标 | 限制 |
|------|------|
| RPM | 30,000 |
| TPM | 5,000,000 |

## 数据来源

- Chat API 参考：https://www.volcengine.com/docs/82379/1494384
- 模型列表：https://www.volcengine.com/docs/82379/1330310
- 模型价格：https://www.volcengine.com/docs/82379/1544106
