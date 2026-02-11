---
title: 万相 2.6 文生图
provider: alibaba
model_id: wan2.6-t2i
task: text-to-image
---

# 万相 2.6 文生图

> 阿里云百炼万相 2.6 文生图模型，支持自由尺寸选择，最高 1440x1440 分辨率，支持同步和异步调用。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `wan2.6-t2i` |
| 任务类型 | text-to-image |
| 输入 | 文本提示词（最长 2100 字符） |
| 输出 | 图像（URL，24小时有效） |
| 分辨率范围 | 总像素 1,638,400~2,073,600，宽高比 1:4~4:1 |

## API 调用

### 端点

**同步调用（仅 wan2.6）：**

`POST https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation`

**异步调用：**

`POST https://dashscope.aliyuncs.com/api/v1/services/aigc/image-generation/generation`

**查询任务结果：**

`GET https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}`

### 请求头

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Content-Type | string | 是 | `application/json` |
| Authorization | string | 是 | `Bearer sk-xxxx` |
| X-DashScope-Async | string | 异步时必填 | 设为 `enable` |

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 取值范围 | 说明 |
|------|------|------|--------|----------|------|
| model | string | 是 | — | `wan2.6-t2i` | 模型ID |
| input.messages | array | 是 | — | 单条消息 | 包含一条 user 消息 |
| input.messages[].role | string | 是 | — | `user` | 角色 |
| input.messages[].content | array | 是 | — | 单个 text 元素 | 内容数组 |
| input.messages[].content[].text | string | 是 | — | 最长 2100 字符 | 正向提示词 |
| parameters.size | string | 否 | `1280*1280` | 总像素 1,638,400~2,073,600，宽高比 1:4~4:1 | 输出分辨率，格式 `宽*高` |
| parameters.n | integer | 否 | 4 | 1~4 | 生成图片数量 |
| parameters.negative_prompt | string | 否 | — | 最长 500 字符 | 反向提示词 |
| parameters.prompt_extend | boolean | 否 | true | true/false | 启用提示词优化 |
| parameters.watermark | boolean | 否 | false | true/false | 添加"AI生成"水印 |
| parameters.seed | integer | 否 | 随机 | 0~2147483647 | 随机种子 |

### 推荐分辨率

| 宽高比 | 分辨率 |
|--------|--------|
| 1:1 | 1280×1280 |
| 3:4 | 1104×1472 |
| 4:3 | 1472×1104 |
| 9:16 | 960×1696 |
| 16:9 | 1696×960 |

### 请求示例（同步）

```bash
curl -X POST 'https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -d '{
    "model": "wan2.6-t2i",
    "input": {
      "messages": [
        {
          "role": "user",
          "content": [
            {"text": "一只小猫在月光下奔跑"}
          ]
        }
      ]
    },
    "parameters": {
      "size": "1280*1280",
      "n": 1,
      "prompt_extend": true
    }
  }'
```

### 请求示例（异步）

```bash
curl -X POST 'https://dashscope.aliyuncs.com/api/v1/services/aigc/image-generation/generation' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H 'X-DashScope-Async: enable' \
  -d '{
    "model": "wan2.6-t2i",
    "input": {
      "messages": [
        {
          "role": "user",
          "content": [
            {"text": "一只小猫在月光下奔跑"}
          ]
        }
      ]
    },
    "parameters": {
      "size": "1280*1280",
      "n": 1,
      "prompt_extend": true
    }
  }'
```

### 查询任务结果

```bash
curl -X GET 'https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY"
```

### 响应示例（同步）

```json
{
  "output": {
    "choices": [
      {
        "finish_reason": "stop",
        "message": {
          "role": "assistant",
          "content": [
            {
              "image": "https://dashscope-result-bj.oss-cn-beijing.aliyuncs.com/xxx.png",
              "type": "image"
            }
          ]
        }
      }
    ],
    "finished": true
  },
  "usage": {
    "image_count": 1,
    "size": "1280*1280"
  },
  "request_id": "815505c6-7c3d-49d7-b197-xxxxx"
}
```

### 响应示例（异步任务创建）

```json
{
  "output": {
    "task_status": "PENDING",
    "task_id": "0385dc79-5ff8-4d82-bcb6-xxxxxx"
  },
  "request_id": "4909100c-7b5a-9f92-bfe5-xxxxxx"
}
```

### 任务状态

| 状态 | 说明 |
|------|------|
| PENDING | 排队中 |
| RUNNING | 处理中 |
| SUCCEEDED | 成功 |
| FAILED | 失败 |
| CANCELED | 已取消 |
| UNKNOWN | 未知/已过期 |

## 计费

| 模型 | 价格 | 免费额度 |
|------|------|----------|
| wan2.6-t2i | 0.20 元/张 | 50 张 |

按成功生成的图片张数计费。图片 URL 24 小时内有效，请及时下载。

## 数据来源

- API 参考：https://help.aliyun.com/zh/model-studio/text-to-image-v2-api-reference
- 计费信息：https://help.aliyun.com/zh/model-studio/model-pricing
