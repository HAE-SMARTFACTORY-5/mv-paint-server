from pydantic import NaiveDatetime, BaseModel
from typing import Optional

class PapercupResponse(BaseModel):
    papercupId: int
    errorStatus: bool
    imageUrl: str
    colorType: Optional[str] = None
    createdAt: NaiveDatetime