# app/data_management/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.auth.routes import oauth2_scheme
from app.database import get_db
from app.models.mycological_data import MycologicalData
from app.schemas.mushroom_data import MycologicalDataInDB

router = APIRouter()

@router.get("/mycological-data", response_model=List[MycologicalData])
async def get_mycological_data(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    data = db.query(MycologicalData).all()
    return data

@router.post("/mycological-data", response_model=MycologicalData)
async def create_mycological_data(data: MycologicalData, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    db_object = MycologicalDataInDB(**data.dict())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object