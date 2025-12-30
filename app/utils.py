def serialize_user(user):
    if not user:
        return None

    return {
        "userId": str(user["_id"]),
        "full_name": user.get("full_name"),
        "email": user.get("email"),
        "role": user.get("role"),
        "is_active": user.get("is_active")
    }
