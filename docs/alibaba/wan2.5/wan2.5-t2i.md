---
title: 万相 2.5 文生图
provider: alibaba
model_id: wan2.5-t2i-preview
task: text-to-image
---

# 万相 2.5 文生图

> 阿里云百炼万相 2.5 文生图模型，支持扩展尺寸（如 768×2700），异步调用，512~1440 像素。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `wan2.5-t2i-preview` |
| 任务类型 | text-to-image |
| 输入 | 文本提示词（最长 2100 字符） |
| 输出 | 图像（URL，24小时有效） |
| 分辨率范围 | 宽/高 512~1440 像素 |

## API 调用

### 端点

**创建任务（异步）：**

`POST https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis`

**查询任务结果：**

`GET https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}`

### 请求头

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| Content-Type | string | 是 | `application/json` |
| Authorization | string | 是 | `Bearer sk-xxxx` |
| X-DashScope-Async | string | 是 | 必须设为 `enable` |

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 取值范围 | 说明 |
|------|------|------|--------|----------|------|
| model | string | 是 | — | `wan2.5-t2i-preview` | 模型ID |
| input.prompt | string | 是 | — | 最长 2100 字符 | 正向提示词 |
| input.negative_prompt | string | 否 | — | 最长 500 字符 | 反向提示词 |
| parameters.size | string | 否 | `1024*1024` | 宽/高 512~1440 像素 | 输出分辨率，格式 `宽*高` |
| parameters.n | integer | 否 | 4 | 1~4 | 生成图片数量 |
| parameters.prompt_extend | boolean | 否 | true | true/false | 启用提示词优化 |
| parameters.watermark | boolean | 否 | false | true/false | 添加"AI生成"水印 |
| parameters.seed | integer | 否 | 随机 | 0~2147483647 | 随机种子 |

### 请求示例

```bash
curl -X POST 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis' \
  -H 'X-DashScope-Async: enable' \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "wan2.5-t2i-preview",
    "input": {
      "prompt": "一只小猫在月光下奔跑",
      "negative_prompt": "低质量"
    },
    "parameters": {
      "size": "1024*1024",
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

### 响应示例（任务创建）

```json
{
  "output": {
    "task_status": "PENDING",
    "task_id": "0385dc79-5ff8-4d82-bcb6-xxxxxx"
  },
  "request_id": "4909100c-7b5a-9f92-bfe5-xxxxxx"
}
```

### 响应示例（任务完成）

```json
{
  "request_id": "2ddf53fa-699a-4267-9446-xxxxxx",
  "output": {
    "task_id": "3cd3fa4e-53ee-4136-9cab-xxxxxx",
    "task_status": "SUCCEEDED",
    "results": [
      {
        "url": "https://dashscope-result-bj.oss-cn-beijing.aliyuncs.com/xxx.png",
        "orig_prompt": "原始提示词",
        "actual_prompt": "优化后的提示词"
      }
    ],
    "task_metrics": {"TOTAL": 1, "SUCCEEDED": 1, "FAILED": 0}
  },
  "usage": {"image_count": 1}
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
| wan2.5-t2i-preview | 0.20 元/张 | 50 张 |

按成功生成的图片张数计费。图片 URL 24 小时内有效，请及时下载。

## 数据来源

- API 参考：https://help.aliyun.com/zh/model-studio/text-to-image-v2-api-reference
- 计费信息：https://help.aliyun.com/zh/model-studio/model-pricing
