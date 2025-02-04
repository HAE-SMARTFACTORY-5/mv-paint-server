from fastapi import HTTPException
import mysql.connector
from infra.database import getDbConnection
from dto import papercupDto


def findAll():
    query = '''
        SELECT *
        FROM papercup as pc
        ORDER BY pc.created_at DESC
    '''
    try:
        connection = getDbConnection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(query)
        results = cursor.fetchall()

        return [
            papercupDto.SimpleResponse(
                papercupId=row['papercup_id'], 
                errorStatus=row['error_status'],
                createdAt=row['created_at'],
            ) for row in results
        ]
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error findAllPapercup(): {e}")
    finally:
        cursor.close
        connection.close

def findById(papercupId):
    query = '''
        SELECT *
        FROM papercup as pc
        WHERE pc.papercup_id = %s
    '''
    try:
        connection = getDbConnection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(query, [papercupId])
        result = cursor.fetchone()

        return papercupDto.DetailResponse(
                papercupId=result['papercup_id'], 
                errorStatus=result['error_status'],
                imageUrl=result['image_url'],
                colorType=result['color_type'],
                createdAt=result['created_at'],
            )
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error findByPapercupId(): {e}")
    finally:
        cursor.close
        connection.close