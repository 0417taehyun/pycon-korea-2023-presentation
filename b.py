"""
원래는 아래와 같이 작성되어 있었어요.

import datetime
import requests
a: str = "abcdefg" + "hijk"

Black 패키지 및 Isort 패키지에 의해 아래와 같이 수정되었어요.
requests 패키지의 경우 내부적으로 타입 힌트가 존재하지 않아 MyPy 패키지에서 타입을 검사하는 과정에서 오류를 발생시키기 때문에 주석을 통해 무시했어요.
스텁(Stub)을 설치하여 이를 해결할 수 있는데, 관련해서 아래 공식 문서를 확인하면 좋아요.
Types from libraries(https://mypy.readthedocs.io/en/stable/getting_started.html?highlight=requests#types-from-libraries)
"""

import datetime

import requests  # type: ignore

a: str = (
    "abcdefg" + "hijklmnop"
)
