# app/main.py
from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.data_management.routes import router as data_router
from app.database import engine
from app.models import user, mycological_data

user.Base.metadata.create_all(bind=engine)
mycological_data.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hyphae API")

app.include_router(auth_router, prefix="/auth", tags=["authentication"])
app.include_router(data_router, prefix="/data", tags=["data management"])

@app.get("/")
async def root():
    return {"message": "Welcome to Hyphae API"}
