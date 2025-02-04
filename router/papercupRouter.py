from fastapi import APIRouter
from service import papercupService
from dto import papercupDto

api = APIRouter()

@api.get("/papercups")
def getAllPapercups() -> list[papercupDto.SimpleResponse]:
    return papercupService.findAllPapercup()