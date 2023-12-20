import logging
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.models.profile import Profile
from app.requests.profile import ProfileUpdateRequest
from app.responses.profile import (
    SingleProfileResponse
)
from app.services.profile import ProfileService
from config.database import get_session
from datetime import date

from app.models.user import User 
from sqlalchemy.orm import Session

profile_service = ProfileService(db=None)

route = APIRouter(
    prefix="/api", tags=["Profiles"], responses={404: {"description": "Not found"}}
)

##response_model=SingleProfileResponse

def __init__(self, db: Session):
    """
    Initialize the UserService class.

    Args:
        db (Session): The database session.
    """
    self.db = db
    
@route.get("/settings/profile")
async def get_profile (db: Session = Depends(get_session)):

    user = db.query(User).get(1)
    profile = db.query(Profile).filter(Profile.user_id == user.id).first()

    if user and profile:
        response_data = {
            "id": profile.id,
            "firstname": profile.firstname,
            "lastname": profile.lastname,
            "middlename": profile.middlename,
            "birthdate": profile.birthdate.strftime("%Y-%m-%d") if profile.birthdate else None,
            "civil_status": profile.civil_status,
            "mobile": profile.mobile,
            "address": profile.address,
            "gender": profile.gender,
            "notification_type": profile.notification_type,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
        }

        return {"data": response_data, "status_code": 200}
    
@route.put("/settings/profile", status_code=200, )
async def update_user(
    update_request: ProfileUpdateRequest, db: Session = Depends(get_session)
):
    profile_service.db = db
    updated_profile = profile_service.update(1, update_request)
    print(updated_profile)
    return {"data": updated_profile, "status_code": 200}

