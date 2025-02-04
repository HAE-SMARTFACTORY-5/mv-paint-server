from fastapi import APIRouter
from service import papercupService
from dto import papercupDto

api = APIRouter()

@api.get("")
def getAllPapercups() -> list[papercupDto.SimpleResponse]:
    return papercupService.findAllPapercup()

@api.get("/{papercupId}")
def getPapercupDetails(papercupId) -> papercupDto.DetailResponse:
    return papercupService.findByPapercupId(papercupId)

@api.post("")
def getPapercupDetails(saveRequest: papercupDto.SaveRequest) -> papercupDto.SimpleResponse:
    return papercupService.savePapercup(saveRequest)
