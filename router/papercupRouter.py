from fastapi import APIRouter
from service import papercupService
from dto import papercupDto

api = APIRouter()

@api.get("/papercups")
def getAllPapercups() -> list[papercupDto.SimpleResponse]:
    return papercupService.findAllPapercup()

@api.get("/papercups/{papercupId}")
def getPapercupDetails(papercupId) -> papercupDto.DetailResponse:
    return papercupService.findByPapercupId(papercupId)

@api.post("/papercups")
def getPapercupDetails(saveRequest: papercupDto.SaveRequest) -> papercupDto.SimpleResponse:
    return papercupService.savePapercup(saveRequest)
