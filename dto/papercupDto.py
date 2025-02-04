from pydantic import NaiveDatetime, BaseModel
from typing import Optional

class SimpleResponse(BaseModel):
    papercupId: int
    errorStatus: bool
    createdAt: NaiveDatetime

class DetailResponse(BaseModel):
    papercupId: int
    errorStatus: bool
    imageUrl: str
    errorType: list
    createdAt: NaiveDatetime

class SaveRequest(BaseModel):
    imageUrl: str
    errorType: list