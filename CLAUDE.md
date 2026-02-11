# AI API Docs 项目指令

## 项目概述

收集和整理 AI API 文档，以统一 markdown 格式保存，发布为 AI 友好的静态网站。

## 文档模板

### 图像生成模型 (Text-to-Image / Image-to-Image)

```markdown
---
title: {模型名称}
provider: {provider}
model_id: {model_id}
task: {text-to-image|image-to-image}
---

# {模型名称}

> {一句话描述}

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `{model_id}` |
| 任务类型 | {task} |
| 输入 | {input_type} |
| 输出 | {output_type} |
| 最大分辨率 | {max_resolution} |

## API 调用

### 端点

`POST {endpoint}`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| ... | ... | ... | ... |

### 请求示例

\`\`\`bash
curl ...
\`\`\`

### 响应示例

\`\`\`json
{ ... }
\`\`\`

## 计费

| 分辨率 | 价格 |
|--------|------|
| ... | ... |
```

### 视频生成模型 (Text-to-Video / Image-to-Video / Video-to-Video)

```markdown
---
title: {模型名称}
provider: {provider}
model_id: {model_id}
task: {text-to-video|image-to-video|video-to-video}
---

# {模型名称}

> {一句话描述}

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型ID | `{model_id}` |
| 任务类型 | {task} |
| 输入 | {input_type} |
| 输出 | {output_type} |
| 视频时长 | {duration} |
| 视频分辨率 | {resolution} |

## API 调用

### 端点

`POST {endpoint}`

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| ... | ... | ... | ... |

### 请求示例

\`\`\`bash
curl ...
\`\`\`

### 异步获取结果

\`\`\`bash
curl ...
\`\`\`

### 响应示例

\`\`\`json
{ ... }
\`\`\`

## 计费

| 分辨率 | 时长 | 价格 |
|--------|------|------|
| ... | ... | ... |
```

## 部署

- 平台：Cloudflare Pages
- 项目名：api-docs
- 站点 URL：https://api-docs-9dh.pages.dev
- CF 账号：Xiatian.zhang@gmail.com（account_id: `452198ca3aab06cd501178fe329902e1`）
- 生产分支：main
- 部署命令：`CLOUDFLARE_ACCOUNT_ID=452198ca3aab06cd501178fe329902e1 npx wrangler pages deploy site --project-name api-docs --branch main`

## 规范

- 所有文档使用中文
- 代码示例使用 curl
- API 参数表格完整列出所有参数
- 计费信息从官方定价页获取
- 文件路径：`docs/<provider>/<model-family>/<model>.md`
