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

profile_service = ProfileService(db=None)

route = APIRouter(
    prefix="/api", tags=["Profiles"], responses={404: {"description": "Not found"}}
)



@route.put("/profiles/1", status_code=200, response_model=SingleProfileResponse)
async def update_user(
    profile: ProfileUpdateRequest, db: Session = Depends(get_session)
):

        profile_service.db = db
        updated_profile = profile_service.update(1, profile)
        return {"data": updated_profile, "status_code": 200}

