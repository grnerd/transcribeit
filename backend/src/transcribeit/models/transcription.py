from typing import Optional
from pydantic import BaseModel

class TranscriptionRequest(BaseModel):
    url: str

class TranscriptionResponse(BaseModel):
    success: bool = False
    message: str
    data: Optional[str]