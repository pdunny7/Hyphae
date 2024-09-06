# app/data_management/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.routes import oauth2_scheme
from app.database import get_db
from app.models.mycological_data import MycologicalData

router = APIRouter()

@router.get("/mycological-data")
async def get_mycological_data(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    data = db.query(MycologicalData).all()
    return {"data": data}

@router.post("/mycological-data")
async def create_mycological_data(data: MycologicalData, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    db.add(data)
    db.commit()
    db.refresh(data)
    return {"message": "Data created successfully", "data": data}
