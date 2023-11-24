from utils.response import build_response
from utils.auth import verify_token


def verify(request_body):
    username = request_body["username"]
    token = request_body["token"]

    if not username or not token:
        return build_response(
            401, {"verified": False, "message": "Incorrect request body"}
        )

    verification = verify_token(username, token)

    if not verification["verified"]:
        return build_response(401, verification)

    return build_response(
        200,
        {"verified": True, "message": "success", "username": username, "token": token},
    )
