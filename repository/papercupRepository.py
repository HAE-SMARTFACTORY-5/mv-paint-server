from fastapi import HTTPException
import mysql.connector
from dto import papercupDto


def findAll(connection):
    query = '''
        SELECT *
        FROM papercup as pc
        ORDER BY pc.created_at DESC
    '''
    try:
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
        raise HTTPException(status_code=500, detail=f"Error findAllPapercup() in papercupRepository: {e}")
    finally:
        cursor.close

def findById(papercupId, connection):
    query = '''
        SELECT *
        FROM papercup as pc
        WHERE pc.papercup_id = %s
    '''
    try:
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

def save(saveRequest, errorStatus, connection):
    query = '''
        INSERT INTO papercup (error_status, image_url, color_type)
        VALUES (%s, %s, %s)
    '''
    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(query, [errorStatus, saveRequest.imageUrl, saveRequest.colorType])
        
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error findByPapercupId(): {e}")
    finally:
        cursor.close
        connection.close

def findResent(connection):
    query = '''
        SELECT *
        FROM papercup as pc
        ORDER BY pc.created_at DESC
        LIMIT 1
    '''
    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(query)
        result = cursor.fetchone()
        
        return  papercupDto.SimpleResponse(
            papercupId=result['papercup_id'], 
            errorStatus=result['error_status'],
            createdAt=result['created_at'],
        )
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error findByPapercupId(): {e}")
    finally:
        cursor.close
        connection.close