import jwt
import os
from datetime import datetime, timedelta


def generate_token(user_info):
    if not user_info:
        return None

    expiration_time = datetime.utcnow() + timedelta(hours=1)
    token = jwt.encode(
        {"exp": expiration_time, **user_info},
        os.environ.get("JWT_SECRET"),
        algorithm="HS256",
    )
    return token


def verify_token(username, token):
    try:
        decoded_token = jwt.decode(
            token, os.environ.get("JWT_SECRET"), algorithms=["HS256"]
        )

        if decoded_token["username"] != username:
            return {"verified": False, "message": "Invalid user"}

        return {"verified": True, "message": "Verified"}

    except jwt.ExpiredSignatureError:
        return {"verified": False, "message": "Token has expired"}

    except jwt.InvalidTokenError:
        return {"verified": False, "message": "Invalid token"}
