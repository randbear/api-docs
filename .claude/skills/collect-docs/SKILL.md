# collect-docs Skill

收集 AI 模型 API 文档并以统一格式保存。

## 使用方式

```
/collect-docs <provider> <model> [url]
```

## 流程

1. **获取文档**：使用 WebSearch 搜索或 WebFetch 抓取指定 URL 的文档内容
2. **提取信息**：按 CLAUDE.md 中定义的模板提取以下信息：
   - 模型 ID 和基本信息
   - API 端点和请求参数
   - 请求/响应示例
   - 计费信息
3. **写入文件**：写入 `docs/<provider>/<model-family>/<model>.md`
4. **更新索引**：
   - 更新 `docs/llms.txt` 添加新条目
   - 更新 `docs/index.md` 如需要
   - 更新 `mkdocs.yml` nav 如需要

## 参数

- `provider`：厂商名称（如 alibaba）
- `model`：模型标识（如 wan2.6-t2i）
- `url`（可选）：文档 URL，未提供则自动搜索

## 模板

参考项目根目录 `CLAUDE.md` 中的文档模板。

## 注意事项

- 所有文档使用中文
- API 示例使用 curl
- 确保参数表格完整
- 计费信息需从官方定价页获取
