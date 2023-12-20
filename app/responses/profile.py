from typing import List
from pydantic import BaseModel


class ProfileResponse(BaseModel):

    id: int
    firstname: str
    lastname: str
    middlename: str
    age: str
    mobile: str
    gender: str
    birthdate: str
    civil_status: str
    notification_type: str
    address: str
    created_at: str
    updated_at: str

class ProfileUpdateResponse(BaseModel):

    id: int
    firstname: str
    lastname: str
    middlename: str
    age: str
    mobile: str
    gender: str
    birthdate: str
    civil_status: str
    notification_type: str
    address: str
    created_at: str
    updated_at: str
