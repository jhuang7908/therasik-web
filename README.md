# Therasik 官网

Therasik 中文官网静态站点，用于 [www.therasik.com](https://www.therasik.com)。

## 内容

- **index.html** — 首页
- **Therasik_Antibody_Page.html** — 抗体可开发性评估
- **Therasik_CART_Page.html** — 智慧 CAR-T 设计
- **Therasik_Bispecific_Page.html** — 双特异抗体设计
- **images/** — 站点图片资源

## 部署（GitHub Pages）

1. 仓库 **Settings → Pages**
2. Source 选 **Deploy from a branch**
3. Branch 选 **main**（或默认分支），Folder 选 **/ (root)**
4. 自定义域名：**Custom domain** 填 `www.therasik.com`，保存后在域名服务商添加 CNAME：`www` → `jhuang7908.github.io`

## 与 InSynBio-AI-Research 的关系

本仓库仅包含 Therasik 官网页面，与 [InSynBio-AI-Research](https://github.com/jhuang7908/InSynBio-AI-Research) 代码库分离，便于独立发布与解析 www.therasik.com。
