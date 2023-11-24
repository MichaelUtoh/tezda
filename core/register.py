from utils.response import build_response
from utils.database import get_user, save_user
import bcrypt


def register(user_info):
    username = user_info["username"]
    name = user_info["name"]
    password = user_info["password"]

    if not username or not password or not name:
        return build_response(401, {"message": "All fields are required"})

    db_user = get_user(username)
    if db_user and db_user.get("username"):
        return build_response(401, {"message": "User already exists"})

    encrypted_password = bcrypt.hashpw(
        password.strip().encode("utf-8"), bcrypt.gensalt(10)
    )
    user = {
        "name": name,
        "username": username.lower(),
        "password": encrypted_password.decode("utf-8"),
    }

    saved_user_response = save_user(user)
    if not saved_user_response:
        return build_response(503, {"message": "Server error"})

    return build_response(200, {"username": username})
