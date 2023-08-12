# PyCon Korea 2023 발표 <파이썬을 처음 사용하는 동료와 효율적으로 일하는 방법>

## 발표자료

- 발표자료는 [0417taehyun/Presentation](https://github.com/0417taehyun/Presentation) 레포지토리에서 확인 가능해요.

## 가상환경 구성 및 패키지 설치

- [Poetry] 패키지를 설치한 뒤, 해당 프로젝트에서 `poetry install` 명령어를 실행해보세요.
- `.venv` 디렉터리가 생성되고, 해당 디렉터리 내에 가상환경과 함께 필요한 패키지가 설치 돼요.
- 패키지 목록은 [`pyproject.toml`](./pyproject.toml) 파일에서 확인 가능해요.

## Makefile 파일

- Makefile 파일 내 작성된 명령어를 확인해보고 하나씩 실행해보세요.
- `make lint` 명령어를 통해 MyPy, Black, 그리고 Isort 패키지를 실행시켜보세요.
- `make run` 명령어를 통해 린팅 작업을 선행한 뒤 FastAPI 웹 프레임워크로 작성된 웹 서버를 실행시켜보세요.
- `make pre-commit` 명령어를 통해 커밋 이전에 작동될 훅을 설치하고 실행시켜보세요. 이때 [`.pre-commit-config.yaml`](./.pre-commit-config.yaml) 파일에서 실제 실행될 훅의 종류를 확인해보세요.


## 기타

- 관련 블로그 글은 미디엄에 작성된 [파이썬을 처음 사용하는 동료와 효율적으로 일하는 방법](https://medium.com/daangn/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84-%EC%B2%98%EC%9D%8C-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EB%8F%99%EB%A3%8C%EC%99%80-%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9C%BC%EB%A1%9C-%EC%9D%BC%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-bb52c3a433fa)에서 확인할 수 있어요.
