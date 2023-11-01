from app.services.user import UserService


def run():
    user_service = UserService()

    users = [
        {
            "username": "andeng",
            "email": "andeng@artisan-sample.com",
            "password": "sample111",
        },
        {
            "username": "loki",
            "email": "loki@artisan-sample.com",
            "password": "sample222",
        },
    ]

    for user in users:
        user_service.save(user)
