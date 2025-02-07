from pydantic import NaiveDatetime, BaseModel
from typing import Optional, List

class SimpleResponse(BaseModel):
    papercupId: int
    errorStatus: bool
    createdAt: NaiveDatetime

class DetailResponse(BaseModel):
    papercupId: int
    errorStatus: bool
    imageUrl: str
    errorType: Optional[List] = None
    createdAt: NaiveDatetime

class StatisticsResponse(BaseModel):
    totalCount: int
    normalCount: int
    errorCount: int

class SaveRequest(BaseModel):
    imageUrl: str
    errorType: Optional[List] = None