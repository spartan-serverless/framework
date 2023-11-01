from app.services.user import UserService


def main(event, context):
    for item in event["Records"]:
        body = item["body"]
        user_service = UserService()
        user_service.save(body)

    return {"StatusCode": 200}
