import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

host = os.environ.get("DB_HOST")
port = os.environ.get("DB_PORT")
database = os.environ.get("DB_NAME")
username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")

database_url = f"postgresql+pg8000://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(database_url)

Session = sessionmaker(bind=engine)


def get_session() -> Session:
    return Session()
