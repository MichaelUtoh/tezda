import json

from core.login import login
from core.register import register
from core.verify import verify
from utils.response import build_response

register_path = "/register"
login_path = "/login"
verify_path = "/verify"


def lambda_handler(event, context):
    print(" Request Event : ", event)
    http_method = event["httpMethod"]
    resource = event["resource"]
    request_body = json.loads(event["body"])

    if http_method == "POST" and resource == register_path:
        response = register(request_body)
    elif http_method == "POST" and resource == login_path:
        response = login(request_body)
        print(response)
    elif http_method == "POST" and resource == verify_path:
        response = verify(request_body)
    else:
        response = build_response(404, "404 Not Found ")

    return response
