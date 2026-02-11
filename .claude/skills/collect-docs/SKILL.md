---
name: collect-docs
description: 收集 AI 模型 API 文档并以统一格式保存，支持单模型和批量模式。Use when user invokes /collect-docs or asks to "收集文档", "添加模型文档", "collect docs".
argument-hint: <provider> [model-family] [model] [url]
---

# collect-docs Skill

收集 AI 模型 API 文档并以统一格式保存。

## 使用方式

```
# 单个模型
/collect-docs alibaba wan2.6-t2i

# 指定多个模型
/collect-docs alibaba wan2.6-t2i wan2.6-i2v wan2.5-t2v

# 整个模型族
/collect-docs alibaba wan2.6

# 整个厂商
/collect-docs alibaba

# 指定文档 URL
/collect-docs alibaba wan2.6-t2i url=https://help.aliyun.com/zh/...
```

## 参数

- `provider`：厂商名称（如 alibaba）
- `model...`：一个或多个模型标识（如 wan2.6-t2i wan2.6-i2v），也可以是模型族名（如 wan2.6）
- `url=`（可选）：官方文档 URL，未提供则自动搜索

## 流程

### 单模型模式

1. **获取文档**：WebFetch 抓取官方文档页面（url 参数或自动搜索）
2. **提取信息**：按 CLAUDE.md 模板提取：模型ID、API 端点、请求参数（类型/必填/默认值/取值范围）、请求响应示例、计费
3. **交叉验证**：关键信息（计费、参数默认值）至少从两个官方页面确认
4. **写入文件**：`docs/<provider>/<model-family>/<model>.md`
5. **更新索引**：更新 `docs/llms.txt`、`mkdocs.yml` nav、provider index

### 批量模式

1. **搜索模型列表**：从官方文档站搜索该模型族/厂商下的所有模型
2. **列出计划**：向用户展示找到的模型列表，确认后再执行
3. **逐个收集**：对每个模型执行单模型流程
4. **统一更新索引**：所有模型完成后一次性更新 llms.txt、mkdocs.yml、provider index

## 模板

参考项目根目录 `CLAUDE.md` 中的文档模板。

## 数据来源规则

- **只允许从厂商官方文档获取信息**，禁止使用第三方博客、论坛、百科等
- 官方来源白名单示例：
  - 阿里云：`help.aliyun.com`、`dashscope.aliyuncs.com`
  - 其他厂商：对应的官方帮助中心 / API 文档站点
- WebSearch 仅用于定位官方文档 URL，不使用搜索结果中的摘要内容
- 如果官方文档中找不到某项信息（如定价），标注为"请参考官方最新定价"，不要猜测或使用非官方数据

## 注意事项

- 所有文档使用中文
- API 示例使用 curl
- 确保参数表格完整，列出所有参数
- 每个文档底部注明数据来源的官方 URL
