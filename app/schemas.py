from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class SignupSchema(BaseModel):
    full_name: str
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=72,
        description="Password must be between 8 and 72 characters"
    )

class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    userId: int
    full_name: str
    email: EmailStr
    role: str
    is_active: bool

    class Config:
        orm_mode = True



class UpdateProfileSchema(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None

class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str = Field(min_length=8,max_length=72)
