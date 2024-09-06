# app/main.py
from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.data_management.routes import router as data_router

app = FastAPI(title="Hyphae API")

app.include_router(auth_router, prefix="/auth", tags=["authentication"])
app.include_router(data_router, prefix="/data", tags=["data management"])

@app.get("/")
async def root():
    return {"message": "Welcome to Hyphae API"}

# app/auth/routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from app.models.user import User, UserInDB

router = APIRouter()

# This should be stored securely, e.g., as an environment variable
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str):
    # This is a mock function. In a real app, you'd query your database.
    if username == "testuser":
        return UserInDB(
            username=username,
            email="testuser@example.com",
            hashed_password=get_password_hash("testpassword")
        )

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# app/data_management/routes.py
from fastapi import APIRouter, Depends, HTTPException
from app.auth.routes import oauth2_scheme

router = APIRouter()

@router.get("/mycological-data")
async def get_mycological_data(token: str = Depends(oauth2_scheme)):
    # This is a placeholder. In a real app, you'd query your database or external services.
    return {"message": "Here's your mycological data"}

# app/models/user.py
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str

class UserInDB(User):
    hashed_password: str
