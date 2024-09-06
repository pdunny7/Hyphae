from sqlalchemy import Column, Integer, String, DateTime, Float
from app.database import Base

class MycologicalData(Base):
    __tablename__ = "mycological_data"

    id = Column(Integer, primary_key=True, index=True)
    species = Column(String, index=True)
    strain = Column(String, index=True)
    collection_date = Column(DateTime)
    location = Column(String)
    temperature = Column(Float)
    humidity = Column(Float)
    notes = Column(String)