from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from app.schemas import SignupSchema, LoginSchema
from app.database import users_collection
from app.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup")
def signup(data: SignupSchema):
    # Check if user already exists
    if users_collection.find_one({"email": data.email}):
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user = {
        "full_name": data.full_name,
        "email": data.email,
        "password": hash_password(data.password),
        "role": "user",
        "is_active": True,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "last_login": None,
    }

    try:
        users_collection.insert_one(user)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    token = create_access_token({
        "sub": data.email,
        "role": "user"
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.post("/login")
def login(data: LoginSchema):
    user = users_collection.find_one({"email": data.email})

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not user.get("is_active", True):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )

    if not verify_password(data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Update last login time
    users_collection.update_one(
        {"_id": user["_id"]},
        {"$set": {"last_login": datetime.utcnow()}}
    )

    token = create_access_token({
        "sub": user["email"],
        "role": user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
