i:
  uv sync && pre-commit install

export:
  uv export > requirements.txt

dev:
  uvicorn main:app --reload

start:
  uvicorn main:app

run-hooks:
  pre-commit run --all-files

test: run-hooks
  ruff check

remove-hooks:
  pre-commit uninstall
