from app.services.user import UserService


def run():
    user_service = UserService()

    users = [
        {
            "username": "andeng",
            "email": "andeng@python-artisan.com",
            "password": "andeng",
        },
        {
            "username": "iviang",
            "email": "iviang@python-artisan.com",
            "password": "iviang",
        },
        {
            "username": "loki",
            "email": "loki@python-artisan.com",
            "password": "loki",
        },
        {
            "username": "lara",
            "email": "lara@python-artisan.com",
            "password": "lara",
        },
    ]

    for user in users:
        user_service.save(user)
