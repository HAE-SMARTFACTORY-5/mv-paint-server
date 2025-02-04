from pydantic import NaiveDatetime, BaseModel
from typing import Optional

class SimpleResponse(BaseModel):
    papercupId: int
    errorStatus: bool
    createdAt: NaiveDatetime