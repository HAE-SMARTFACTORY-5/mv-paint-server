from fastapi import HTTPException
import mysql.connector
from infra.database import getDbConnection
from dto.papercupResponse import PapercupResponse


def findAll():
    query = '''
        SELECT *
        FROM papercup
        ORDER BY papercup.created_at DESC
    '''
    try:
        connection = getDbConnection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(query)
        results = cursor.fetchall()

        return [
            PapercupResponse(
                papercupId=row['papercup_id'], 
                errorStatus=row['error_status'],
                imageUrl=row['image_url'],
                colorType=row['color_type'],
                createdAt=row['created_at'],
            ) for row in results
        ]
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error findAllPapercup(): {e}")
    finally:
        cursor.close
        connection.close