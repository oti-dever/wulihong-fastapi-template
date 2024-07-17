# API 服务模板（FastAPI）

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

运行：

```bash
uvicorn main:app
```

测试 Git 钩子：

```bash
pre-commit run --all-files
```

## 部署

编辑 `.env.production` 文件配置环境变量，然后运行：

```bash
docker compose --env-file .env.production up -d
```
