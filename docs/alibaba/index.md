# 阿里云百炼

阿里云大模型服务平台百炼（Model Studio）提供的万相系列视觉生成模型。

## 平台信息

| 属性 | 值 |
|------|-----|
| 厂商 | 阿里云 |
| 平台 | 大模型服务平台百炼 |
| API Base URL | `https://dashscope.aliyuncs.com` |
| 认证方式 | `Authorization: Bearer $DASHSCOPE_API_KEY` |
| 文档 | [help.aliyun.com/zh/model-studio](https://help.aliyun.com/zh/model-studio/) |

## 万相 2.6 系列

最新一代视觉生成模型，支持多镜头叙事、音频同步等高级功能。

| 模型 | 任务 | 模型ID | 文档 |
|------|------|--------|------|
| 文生图 | text-to-image | `wan2.6-t2i` | [查看](wan2.6/wan2.6-t2i.md) |
| 图生图 | image-to-image | `wan2.6-image` | [查看](wan2.6/wan2.6-i2i.md) |
| 文生视频 | text-to-video | `wan2.6-t2v` | [查看](wan2.6/wan2.6-t2v.md) |
| 图生视频 | image-to-video | `wan2.6-i2v` / `wan2.6-i2v-flash` | [查看](wan2.6/wan2.6-i2v.md) |
| 视频生视频 | reference-to-video | `wan2.6-r2v` / `wan2.6-r2v-flash` | [查看](wan2.6/wan2.6-v2v.md) |

## 万相 2.5 系列

上一代视觉生成模型，提供稳定的图像和视频生成能力。

| 模型 | 任务 | 模型ID | 文档 |
|------|------|--------|------|
| 文生图 | text-to-image | `wan2.5-t2i-preview` | [查看](wan2.5/wan2.5-t2i.md) |
| 图像编辑 | image-editing | `wan2.5-i2i-preview` | [查看](wan2.5/wan2.5-i2i.md) |
| 文生视频 | text-to-video | `wan2.5-t2v-preview` | [查看](wan2.5/wan2.5-t2v.md) |
| 图生视频 | image-to-video | `wan2.5-i2v-preview` | [查看](wan2.5/wan2.5-i2v.md) |

## 计费概览

### 图像生成

| 模型 | 价格 | 免费额度 |
|------|------|----------|
| wan2.6-t2i | 0.20 元/张 | 50 张 |
| wan2.6-image（图生图） | 0.20 元/张 | 50 张 |
| wan2.5-t2i-preview | 0.20 元/张 | 50 张 |
| wan2.5-i2i-preview | 0.220177 元/张 | 50 张 |

### 视频生成

| 模型 | 类型 | 分辨率 | 价格 | 免费额度 |
|------|------|--------|------|----------|
| wan2.6-t2v | — | 720P | 0.6 元/秒 | 50 秒 |
| wan2.6-t2v | — | 1080P | 1 元/秒 | 50 秒 |
| wan2.6-i2v | 有声视频 | 720P | 0.6 元/秒 | 50 秒 |
| wan2.6-i2v | 有声视频 | 1080P | 1 元/秒 | 50 秒 |
| wan2.6-i2v-flash | 有声（audio=true） | 720P / 1080P | 0.3 / 0.5 元/秒 | 50 秒 |
| wan2.6-i2v-flash | 无声（audio=false） | 720P / 1080P | 0.15 / 0.25 元/秒 | 50 秒 |
| wan2.6-r2v | 有声视频 | 720P | 0.6 元/秒 | 50 秒 |
| wan2.6-r2v | 有声视频 | 1080P | 1 元/秒 | 50 秒 |
| wan2.6-r2v-flash | 有声（audio=true） | 720P / 1080P | 0.3 / 0.5 元/秒 | 50 秒 |
| wan2.6-r2v-flash | 无声（audio=false） | 720P / 1080P | 0.15 / 0.25 元/秒 | 50 秒 |
| wan2.5-t2v-preview | — | 480P / 720P / 1080P | 0.3 / 0.6 / 1 元/秒 | 50 秒 |
| wan2.5-i2v-preview | 有声视频 | 480P / 720P / 1080P | 0.3 / 0.6 / 1 元/秒 | 50 秒 |

数据来源：[阿里云百炼模型定价](https://help.aliyun.com/zh/model-studio/model-pricing)
