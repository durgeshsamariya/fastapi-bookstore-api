from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models import User
from typing import Annotated

from pydantic import BaseModel

class TokenData(BaseModel):
    username: str | None = None


# Secret key for JWT encoding and decoding (replace with your own secret)
SECRET_KEY = "f408b6e19c8719c4a8dabfbc95e2f56d6e36945b562d15c8d7f3ce9bbed3d805"

# Algorithm to encode and decode JWT
ALGORITHM = "HS256"

# Token expiration time in minutes
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Create an instance of OAuth2PasswordBearer for token management
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password hashing
password_hashing = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Mock user database (replace with your database connection)
fake_users_db = {
    "user1": {
        "username": "user1",
        "full_name": "User One",
        "email": "user1@example.com",
        "hashed_password": "$2b$12$Gtz0WFQ9It5qb1RoCOy9pu7o.LfuKtoUobfzZveZSrZrCkSInLSNu",  # Password: secret1
        "disabled": False,
        "role": "user",
    },
    "admin": {
        "username": "admin",
        "full_name": "Admin User",
        "email": "admin@example.com",
        "hashed_password": "$2b$12$2WpdxR5w1lgU.P7oEZhBbuIWVLzCSRq0gcgwvdHTHBMfXvEWK5xXG",  # Password: admin_secret
        "disabled": False,
        "role": "admin",
    },
}

# Create access token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire, "sub": data["username"]})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Verify user credentials
def verify_user(db_user: User, password: str):
    if not db_user or not password_hashing.verify(password, db_user.hashed_password):
        return None
    return db_user

# Get current user
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    return token_data

# Get user by username
def get_user(username: str):
    if username in fake_users_db:
        user_dict = fake_users_db[username]
        return User(**user_dict)

# Create access token for login
def create_access_token_for_user(user: User, expires_delta: timedelta = None):
    data = {"sub": user.username}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)