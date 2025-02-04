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
    colorType: Optional[str] = None
    createdAt: NaiveDatetime

class SaveRequest(BaseModel):
    imageUrl: str
    colorType: Optional[str] = None