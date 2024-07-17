# API 服务模板（FastAPI）

本项目是一个基于 FastAPI 的 API 服务模板。

> 本项目使用 LF 格式行尾，请确保你的编辑器支持，推荐使用 VS Code。全局设置停止自动转换行尾：
>
> ```bash
> git config --global core.autocrlf false
> ```

克隆项目：

```bash
git clone https://github.com/oti-dever/wulihong-fastapi-template.git
cd wulihong-fastapi-template
```

创建虚拟环境：

```bash
python -m venv venv
```

下面的操作请在虚拟环境下工作，安装依赖：

```bash
poetry install --no-root
```

安装 Git 钩子：

```bash
pre-commit install
```

开发：

```bash
fastapi dev main.py --reload
# 或者
uvicorn main:app --reload
```

生产运行：

```bash
uvicorn main:app
```

测试 Git 钩子：

```bash
pre-commit run --all-files
```

## 部署

本项目使用 Docker 多阶段构建镜像，并生成为动态链接库（共享库）来运行，一定程度上可保护源码并加快程序运行速度，但可能造成部分第三方库工作不正常。

根据 `.env.example` 编辑 `.env.production` 文件配置环境变量，然后运行：

```bash
docker compose --env-file .env.production up -d
```

这将自动构建镜像并运行容器。
