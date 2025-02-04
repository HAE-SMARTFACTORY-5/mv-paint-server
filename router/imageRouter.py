from fastapi import APIRouter, File, UploadFile, HTTPException
from dto import imageDto
import shutil
import os
import uuid

UPLOAD_DIR = "images" # 이미지 저장 위치
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif"} # 허용할 이미지 확장자 목록

api = APIRouter()

@api.post("/images/upload")
def upload_file(file: UploadFile = File(...)):
    # 이미지 파일 확장자 검증
    ext = os.path.splitext(file.filename)[1]  # 파일 확장자 추출
    if ext.lower() not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="허용하지 않는 이미지 확장자입니다.")

    # 이미지 업로드
    uniqueFilename = f"{uuid.uuid4()}{ext}"
    filePath = f"{UPLOAD_DIR}/{uniqueFilename}"
    
    with open(filePath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return imageDto.PathResponse(imagePath=filePath)
