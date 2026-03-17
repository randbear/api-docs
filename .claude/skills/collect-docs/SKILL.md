---
name: collect-docs
description: 收集 AI 模型 API 官方文档并按统一 Markdown 模板保存。用于用户提到“collect docs”“收集文档”“添加模型文档”或直接调用 /collect-docs 时。
argument-hint: <provider> [model-family] [model ...] [url=<official-doc-url>]
---

# collect-docs

收集 AI 模型 API 文档，并整理为项目内统一格式的 Markdown。

## 用法

```text
# 单个模型
/collect-docs alibaba wan2.6-t2i

# 指定多个模型
/collect-docs alibaba wan2.6-t2i wan2.6-i2v wan2.5-t2v

# 整个模型族
/collect-docs alibaba wan2.6

# 整个厂商
/collect-docs alibaba

# 指定官方文档 URL
/collect-docs alibaba wan2.6-t2i url=https://help.aliyun.com/zh/...
```

## 参数

- `provider`: 厂商名称，例如 `alibaba`
- `model-family`: 模型族名称，例如 `wan2.6`
- `model ...`: 一个或多个模型标识，例如 `wan2.6-t2i wan2.6-i2v`
- `url=`: 可选。指定官方文档 URL；未提供时先搜索官方文档入口

## 工作流

### 单模型模式

1. 获取文档：优先使用 `url=` 指定的官方页面；否则搜索并定位官方文档。
2. 提取信息：按仓库根目录 `CLAUDE.md` 中的模板提取模型信息、端点、请求参数、请求示例、响应示例、计费信息。
3. 交叉验证：关键字段至少在两个官方页面间互相确认。重点检查计费、默认值、分辨率、时长、异步接口等容易变化的内容。
4. 写入文件：保存到 `docs/<provider>/<model-family>/<model>.md`。
5. 更新索引：同步更新 `docs/llms.txt`、`mkdocs.yml` 导航以及 provider 索引页。

### 批量模式

1. 从官方文档中收集该厂商或模型族下的模型列表。
2. 先向用户展示准备收集的模型清单。
3. 逐个执行单模型流程。
4. 全部完成后统一更新索引文件。

## 文档模板

优先读取仓库根目录的 `CLAUDE.md`。如果不存在，再沿用当前仓库已存在的同类文档结构和字段顺序。

## 数据源规则

- 只允许使用厂商官方文档、官方帮助中心、官方 API 参考页。
- 搜索仅用于定位官方 URL，不直接使用搜索摘要或第三方转载内容。
- 如果官方文档缺少某项信息，明确标注“请参考官方最新说明”，不要猜测。
- 对“最新价格”“支持分辨率”“速率限制”这类易变信息必须再次核验。

## 输出要求

- 文档正文使用中文。
- API 示例优先使用 `curl`。
- 参数表尽量完整，标明类型、是否必填、默认值和说明。
- 文档底部列出所用官方来源 URL。
- 如信息存在冲突，明确说明差异和判断依据。
