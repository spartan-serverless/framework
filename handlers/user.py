from app.services.user import UserService


def main(event, context):
    user_service = UserService()

    data = {
            "username": "giana",
            "email": "giana@artisan-sample.com",
            "password": "sample333",
        }

    user_service.save(data)

    return {"StatusCode": 200}
