import bcrypt

from utils.database import get_user
from utils.response import build_response


def login(user):
    username = user["username"]
    password = user["password"]

    if not username or not password:
        return Exception({"message": "username and password are required"})

    db_user = get_user(username)
    if not db_user or not db_user.get("username"):
        return build_response(401, {"message": "username incorrect"})

    if not bcrypt.checkpw(
        password.encode("utf-8"), db_user["password"].encode("utf-8")
    ):
        return build_response(401, {"message": "Password is wrong"})

    return user
