from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from domain.question import question_router

app = FastAPI()

origins = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
]
# cors 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(question_router.router)
