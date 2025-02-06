from fastapi import APIRouter
from service import papercupService
from dto import papercupDto

api = APIRouter()

@api.get("", summary="종이컵 데이터 리스트 조회", description="최신순으로 조회. limit 없음")
def getAllPapercups() -> list[papercupDto.SimpleResponse]:
    return papercupService.findAllPapercup()

@api.get("/detail/{papercupId}", summary="종이컵 데이터 상세조회")
def getPapercupDetails(papercupId: int) -> papercupDto.DetailResponse:
    return papercupService.findByPapercupId(papercupId)

@api.get("/statistics", summary="종이컵 정상/불량 개수 조회")
def getPapercupDetails() -> papercupDto.StatisticsResponse:
    return papercupService.getStatisticalData()

@api.post("", summary="종이컵 데이터 저장", description="errorType이 없을 경우 null로 전달")
def getPapercupDetails(saveRequest: papercupDto.SaveRequest) -> papercupDto.SimpleResponse:
    return papercupService.savePapercup(saveRequest)
