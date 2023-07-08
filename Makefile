# 간단하게 사용 방법을 확인하기 위해 Makefile 파일 내에는 발표 때 보여드린 migrate 명령어를 제거 했어요.

.PHONY: lint
lint:
	poetry run mypy . && poetry run black . && poetry run isort .

.PHONY: run
run:
	make lint && poetry run uvicorn main:app --reload

.PHONY: pre-commit
pre-commit:
	poetry run pre-commit install && poetry run pre-commit run
