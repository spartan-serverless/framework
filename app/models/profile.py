from sqlalchemy import Column, Integer, String, Date, Text ,DateTime ,func

from .base import Base


class Profile(Base):

    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True)
    firstname = Column(String,nullable=False)
    lastname = Column(String,nullable=False)
    middlename = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    mobile = Column(String,nullable=False)
    gender = Column(Integer,nullable=False)
    birthdate = Column(Date,nullable=False)
    civil_status = Column(Integer,nullable=False)
    notification_type = Column(Integer,nullable=False)
    address = Column(Text,nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp())