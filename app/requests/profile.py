from typing import Optional

from pydantic import BaseModel, validator


class ProfileCreateRequest(BaseModel):

    username: str
    email: EmailStr
    password: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()



class ProfileUpdateRequest(BaseModel):


    firstname: Optional[str]
    lastname: Optional[str]
    middlename: Optional[str]
    age: Optional[str]
    mobile: Optional[str]
    gender: Optional[str]
    birthdate: Optional[str]
    civil_status: Optional[str]
    notification_type: Optional[str]
    address: Optional[str]
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
