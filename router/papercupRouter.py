from fastapi import APIRouter
from service import papercupService
from dto.papercupResponse import PapercupResponse

api = APIRouter()

@api.get("/papercups")
def getAllPapercups() -> list[PapercupResponse]:
    return papercupService.findAllPapercup()