from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class SignupRequest(BaseModel):
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: str = Field(..., alias="_id")
    email: EmailStr
    role: Optional[str] = "patient"
    created_at: Optional[datetime]

    class config:
        allow_population_by_field_name = True
        orm_mode = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"