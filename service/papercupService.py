from fastapi import HTTPException
from repository import papercupRepository
from infra.database import getDbConnection
from dto import papercupDto
import logging


logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def findAllPapercup():
    try:
        connection = getDbConnection()
        response = papercupRepository.findAll(connection)
        connection.commit()
        return response
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error findAllPapercup() in papercupService: {e}")
    finally:
        connection.close

def findByPapercupId(papercupId):
    try:
        connection = getDbConnection()
        response = papercupRepository.findById(papercupId, connection)
        connection.commit()
        return response
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error findByPapercupId() in papercupService: {e}")
    finally:
        connection.close
    

def savePapercup(saveRequest):
    # 불량 상태 설정
    errorStatus = False
    if saveRequest.errorType != None:
        errorStatus = True

    try:
        connection = getDbConnection()
        papercupRepository.save(saveRequest, errorStatus, connection)
        response = papercupRepository.findResent(connection)
        connection.commit()
        return response
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error savePapercup() in papercupService: {e}")
    finally:
        connection.close

def getStatisticalData():
    try:
        connection = getDbConnection()
        totalPapercups = papercupRepository.findAll(connection)
        nomalPapercups = list(filter(lambda papercup: papercup.errorStatus == False, totalPapercups))
        errorPapercups = list(filter(lambda papercup: papercup.errorStatus == True, totalPapercups))
        response = papercupDto.StatisticsResponse(totalCount=len(totalPapercups), normalCount=len(nomalPapercups), errorCount=len(errorPapercups))
        connection.commit()
        return response
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error getStatisticalData() in papercupService: {e}")
    finally:
        connection.close