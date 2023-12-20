from typing import Optional

from pydantic import BaseModel, validator
from datetime import datetime
from datetime import date

class ProfileUpdateRequest(BaseModel):

    email: Optional[str]
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
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
