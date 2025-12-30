from fastapi import APIRouter, Depends, Query, HTTPException, status
from bson import ObjectId
from bson.errors import InvalidId

from app.deps import get_current_user, admin_only
from app.database import users_collection
from app.utils import serialize_user
from app.schemas import UpdateProfileSchema, ChangePasswordSchema
from app.security import verify_password, hash_password

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
def get_my_profile(current_user=Depends(get_current_user)):
    user = users_collection.find_one(
        {"email": current_user["email"]}
    )

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return serialize_user(user)


@router.get("/")
def get_all_users(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=50),
    current_user=Depends(admin_only)
):
    
    skip = (page - 1) * limit
    users = users_collection.find().skip(skip).limit(limit)

    return {
        "page": page,
        "users": [serialize_user(user) for user in users]
    }


@router.put("/{user_id}/activate")
def activate_user(user_id: str, current_user=Depends(admin_only)):
    try:
        obj_id = ObjectId(user_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid user ID")

    result = users_collection.update_one(
        {"_id": obj_id},
        {"$set": {"is_active": True}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User account activated"}


@router.put("/{user_id}/deactivate")
def deactivate_user(user_id: str, current_user=Depends(admin_only)):
    try:
        obj_id = ObjectId(user_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid user ID")

    result = users_collection.update_one(
        {"_id": obj_id},
        {"$set": {"is_active": False}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User account deactivated"}


@router.put("/me/profile")
def update_my_profile(
    data: UpdateProfileSchema,
    current_user=Depends(get_current_user)
):
    update_fields = {}

    # Update full name if provided
    if data.full_name:
        update_fields["full_name"] = data.full_name

    # Update email if provided
    if data.email:
        existing_user = users_collection.find_one({"email": data.email})
        if existing_user and existing_user["email"] != current_user["email"]:
            raise HTTPException(
                status_code=400,
                detail="Email already in use"
            )
        update_fields["email"] = data.email

    if not update_fields:
        raise HTTPException(
            status_code=400,
            detail="No fields provided for update"
        )

    users_collection.update_one(
        {"email": current_user["email"]},
        {"$set": update_fields}
    )

    user = users_collection.find_one(
        {"email": update_fields.get("email", current_user["email"])}
    )

    return serialize_user(user)



@router.put("/me/change-password")
def change_password(
    data: ChangePasswordSchema,
    current_user=Depends(get_current_user)
):
    user = users_collection.find_one(
        {"email": current_user["email"]}
    )

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(data.old_password, user["password"]):
        raise HTTPException(status_code=400, detail="Old password is incorrect")

    users_collection.update_one(
        {"email": current_user["email"]},
        {"$set": {"password": hash_password(data.new_password)}}
    )

    return {"message": "Password updated successfully"}
