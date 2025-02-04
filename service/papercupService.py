from fastapi import HTTPException
from repository import papercupRepository
from infra.database import getDbConnection
import traceback
import logging
import json

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def findAllPapercup():
    try:
        connection = getDbConnection()
        response = papercupRepository.findAll(connection)
        connection.commit()
        return response
    except:
        connection.rollback()
        logging.error(traceback.extract_stack())
        raise HTTPException(status_code=500, detail=f"Error findAllPapercup() in papercupService: {traceback.format_exc()}")
    finally:
        connection.close

def findByPapercupId(papercupId):
    try:
        connection = getDbConnection()
        response = papercupRepository.findById(papercupId, connection)
        connection.commit()
        return response
    except:
        connection.rollback()
        logging.error(traceback.extract_stack())
        raise HTTPException(status_code=500, detail=f"Error findAllPapercup() in papercupService: {traceback.format_exc()}")
    finally:
        connection.close
    

def savePapercup(saveRequest):
    # 불량 상태 설정
    errorStatus = False
    if saveRequest.errorType == None:
        errorStatus = True

    try:
        connection = getDbConnection()
        papercupRepository.save(saveRequest, errorStatus, connection)
        response = papercupRepository.findResent(connection)
        connection.commit()
        return response
    except:
        connection.rollback()
        logging.error(traceback.extract_stack())
        raise HTTPException(status_code=500, detail=f"Error findAllPapercup() in papercupService: {traceback.format_exc()}")
    finally:
        connection.close