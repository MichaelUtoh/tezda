import boto3
from decouple import config

# Set the region
region = "us-east-1"

# Create DynamoDB client
dynamodb = boto3.resource(
    "dynamodb",
    region_name=region,
    aws_access_key_id=config("AWS_ACCESS_KEY"),
    aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"),
)
user_table = dynamodb.Table("accounts")


def get_user(username):
    response = user_table.get_item(Key={"username": username})
    return response.get("Item")


def save_user(user):
    try:
        user_table.put_item(
            Item={
                "username": user["username"],
                "name": user["name"],
                "password": user["password"],
            }
        )
        return True
    except Exception as e:
        print(f"Error saving user: {e}")
        return False
