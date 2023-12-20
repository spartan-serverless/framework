from faker import Faker
import random
from app.models.profile import Profile
from config.database import get_session
from datetime import datetime, timedelta


def run():
    db = get_session()
    fake = Faker()

    current_time = datetime.now()
    two_months_ago = current_time - timedelta(days=60)
    one_week_ago = current_time - timedelta(days=7)

    for user_id in range(1, 60):
        profile = {
            "user_id": user_id,
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "age": fake.random_int(min=18, max=99),
            "gender": random.choice([1, 2]),
            "civil_status": random.choice([1, 2, 3, 4]),
            "birthdate": fake.date_of_birth(),
            "mobile": fake.phone_number(),
            "address": fake.address(),
            "created_at": fake.date_time_between(start_date=two_months_ago, end_date=one_week_ago),
            "updated_at": fake.date_time_between(start_date=one_week_ago, end_date=current_time),
        }

        profile = Profile(**profile)
        db.add(profile)
        db.commit()
        db.refresh(profile)
