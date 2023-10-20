import sys

sys.path.append(".")

from app.models.user import User


def run():
    user_model = User()

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
        user_model.create(**user)
