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

    
@route.get("/settings/profile")
async def get_profile(db: Session = Depends(get_session)):
    profile_service.db = db
    user_id = 1 
    response_data = profile_service.get_profile(user_id)
    return {"data": response_data, "status_code": 200}
    
@route.put("/settings/profile", status_code=200, )
async def update_user(
    update_request: ProfileUpdateRequest, db: Session = Depends(get_session)
):
    profile_service.db = db
    updated_profile = profile_service.update(1, update_request)
    return {"data": updated_profile, "status_code": 200}

