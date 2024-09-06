from pydantic import BaseModel
from datetime import datetime

class MycologicalDataInDB(BaseModel):
    id: int
    species: str
    strain: str
    collection_date: datetime
    location: str
    temperature: float
    humidity: float
    notes: str

    class Config:
        orm_mode = True