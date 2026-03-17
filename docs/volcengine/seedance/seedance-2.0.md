---
title: Seedance 2.0 视频生成
provider: volcengine
model_id: doubao-seedance-2-0-260128
task: text-to-video
---

# Seedance 2.0 视频生成

> 火山方舟豆包 Seedance 2.0 视频生成模型，支持音频、视频、图像、文本混合参考，具备多模态生视频、视频延长、视频编辑、首尾帧生视频等能力。当前仅支持体验中心免费体验，暂不支持正式 API 调用。

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `doubao-seedance-2-0-260128` |
| 控制台展示名 | `Doubao-Seedance-2.0` |
| 任务类型 | text-to-video / image-to-video / video-to-video |
| 输入 | 文本 / 图像 / 音频 / 视频 |
| 输出 | 视频 |
| 调用状态 | 仅体验中心可用，API 暂未开放 |

## 支持的功能

| 功能 | 说明 |
|------|------|
| 多模态生视频 | 支持文本、图像、音频、视频多模态输入生成视频 |
| 视频延长 | 支持对已生成视频进行延长 |
| 视频编辑 | 支持对视频进行编辑处理 |
| 首尾帧生视频 | 根据首帧和尾帧图片生成过渡视频 |
| 虚拟人像库 | 可在体验中心检索虚拟人像素材并引用资产 ID / URI |
| 模板库 | 体验中心提供模板库，可一键生成并查看模板示例代码 |
| 免费体验 | 当前仅支持在控制台体验中心免费额度内体验 |

## API 调用

### 端点

截至 2026-03-11，火山引擎官方文档说明：

> **Seedance 2.0 模型目前仅支持控制台体验中心在免费额度内体验，暂不支持 API 调用，敬请期待。**

API 开放后预计将使用以下端点（参考 Seedance 1.x 系列）：

`POST https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks`

### 当前可用入口

| 入口 | 地址 | 说明 |
|------|------|------|
| 模型详情（控制台） | `https://console.volcengine.com/ark/region:ark+cn-beijing/model/detail?Id=doubao-seedance-2-0` | 官方控制台模型详情入口，需要登录 |
| AI 体验中心 | `https://exp.volcengine.com/` | 可直接体验 Seedance 2.0 与相关模板 |
| 虚拟人像库文档 | `https://www.volcengine.com/docs/82379/2223965` | 说明虚拟人像库、模板库和体验中心操作方式 |

### 请求参数（参考 Seedance 1.x 系列）

API 开放后预计将支持以下参数：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| model | string | 是 | 模型ID，如 `doubao-seedance-2-0-260128` |
| content | object[] | 是 | 输入内容，支持文本、图片、视频、音频 |
| callback_url | string | 否 | 回调通知地址 |
| return_last_frame | boolean | 否 | 是否返回尾帧图像，默认 false |
| service_tier | string | 否 | 服务等级，default 或 flex |
| execution_expires_after | integer | 否 | 任务超时时间（秒），默认 172800 |
| resolution | string | 否 | 视频分辨率：480p、720p、1080p |
| ratio | string | 否 | 宽高比：16:9、4:3、1:1、3:4、9:16、21:9、adaptive |
| duration | integer | 否 | 视频时长（秒），支持 2~12 秒 |
| seed | integer | 否 | 随机种子，默认 -1 |
| camera_fixed | boolean | 否 | 是否固定摄像头，默认 false |
| watermark | boolean | 否 | 是否包含水印，默认 false |

### content 对象结构

| 字段 | 类型 | 说明 |
|------|------|------|
| type | string | 内容类型：text、image_url、draft_task |
| text | string | 文本提示词（type=text 时） |
| image_url | object | 图片对象（type=image_url 时） |
| image_url.url | string | 图片URL或Base64编码 |
| role | string | 图片用途：first_frame、last_frame、reference_image |

### 请求示例

```bash
curl -X POST https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks \
  -H “Content-Type: application/json” \
  -H “Authorization: Bearer $ARK_API_KEY” \
  -d '{
    “model”: “doubao-seedance-2-0-260128”,
    “content”: [
        {
            “type”: “text”,
            “text”: “写实风格，晴朗的蓝天之下，一大片白色的雏菊花田，镜头逐渐拉近”
        }
    ],
    “ratio”: “16:9”,
    “duration”: 5,
    “watermark”: false
}'
```

### 响应示例

```json
{
  “id”: “cgt-2025******-****”
}
```

### 异步获取结果

使用查询视频生成任务 API 获取结果：

`GET https://ark.cn-beijing.volces.com/api/v3/contents/generations/tasks/{task_id}`

## 使用说明

### 虚拟人像库

| 项目 | 说明 |
|------|------|
| 素材类型 | 虚拟人物图片 |
| 可获取信息 | 资产 ID、URI、人物标签、小传 |
| 使用方式 | 在体验中心输入框中以 `@素材名` 形式引用 |
| 限制 | 当前暂不支持使用真实人物形象生成视频 |

### 图片要求

| 项目 | 要求 |
|------|------|
| 图片格式 | jpeg、png、webp、bmp、tiff、gif、heic、heif |
| 宽高比 | (0.4, 2.5) |
| 宽高像素 | (300, 6000) px |
| 大小 | 小于 30 MB |

### 提示词建议

- 支持中英文，建议中文不超过500字，英文不超过1000词
- 字数过多信息容易分散，模型可能忽略细节
- 更多提示词技巧请参考官方 Seedance 提示词指南

## 计费

根据控制台模型详情页面显示的定价信息：

| 计费类型 | 价格 |
|------|------|
| 包含视频输入 | 28 元/百万tokens |
| 不含视频输入 | 46 元/百万tokens |
| 控制台体验中心 | 免费额度内体验 |

> 注意：以上为控制台展示的预计定价，正式 API 开放后请以官方最新公告为准。

## 数据来源

- 控制台模型详情（需登录）：https://console.volcengine.com/ark/region:ark+cn-beijing/model/detail?Id=doubao-seedance-2-0
- 创建视频生成任务 API：https://www.volcengine.com/docs/82379/1520757
- 查询视频生成任务 API：https://www.volcengine.com/docs/82379/1521309
- 视频生成 SDK 示例：https://www.volcengine.com/docs/82379/1366799
- AI 体验中心入口：https://exp.volcengine.com/
