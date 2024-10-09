# FastAPI 服务模板

本项目是一个基于 FastAPI 的 API 服务模板，克隆项目：

```bash
git clone https://github.com/oti-dever/wulihong-fastapi-template.git
cd wulihong-fastapi-template
```

安装依赖：

```bash
uv sync
just i
```

开发：

```bash
just dev
```

生产运行：

```bash
just start
```

测试 Git 钩子：

```bash
just test-hooks
```

## 部署

本项目使用 Docker 多阶段构建镜像，并生成为动态链接库（共享库）来运行，一定程度上可保护源码并加快程序运行速度，但可能造成部分第三方库工作不正常。

根据 `.env.example` 编辑 `.env.production` 文件配置环境变量，然后运行：

```bash
docker compose --env-file .env.production up -d
```

这将自动构建镜像并运行容器。
