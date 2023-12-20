from pydantic import BaseModel
from typing import Optional
from datetime import date


class ProfileResponse(BaseModel):

    id: int
    firstname: Optional[str]
    lastname: Optional[str]
    middlename: Optional[str]
    age: Optional[int]
    mobile: Optional[str]
    gender: Optional[int]
    birthdate: Optional[date]
    civil_status: Optional[int]
    notification_type: Optional[int]
    address: Optional[str]
    created_at:  Optional[str]
    updated_at:  Optional[str]

class SingleProfileResponse(BaseModel):

    data: ProfileResponse
    status_code: int

class ProfileUpdateResponse(BaseModel):

    id: int
    firstname: Optional[str]
    lastname: Optional[str]
    middlename: Optional[str]
    age: Optional[int]
    mobile: Optional[str]
    gender: Optional[int]
    birthdate: Optional[date]
    civil_status: Optional[int]
    notification_type: Optional[int]
    address: Optional[str]
    created_at:  Optional[str]
    updated_at:  Optional[str]
