"""
원래는 아래와 같이 작성되어 있었어요.

from fastapi import FastAPI

app: FastAPI FastAPI()

Black 패키지에 의해 아래와 같이 수정되었어요.
"""


from fastapi import FastAPI

app: FastAPI = FastAPI()
