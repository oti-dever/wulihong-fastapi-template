i:
  pre-commit install && uv export > requirements.txt

dev:
  uvicorn main:app --reload

start:
  uvicorn main:app

test-hooks:
  pre-commit run --all-files
