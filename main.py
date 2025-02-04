from fastapi import FastAPI
from router import papercupRouter
from router import imageRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

app = FastAPI()
app.include_router(papercupRouter.api, prefix='/papercups')
app.include_router(imageRouter.api, prefix='/images')

# 저장 폴더가 없으면 생성
UPLOAD_DIR = "images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 저장된 이미지 파일 접근 허용
app.mount("/static/images", StaticFiles(directory="images"), name="static-images")

# CORS 설정
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000)