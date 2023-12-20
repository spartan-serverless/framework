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

##response_model=SingleProfileResponse

@route.put("/profiles", status_code=200, )
async def update_user(
    update_request: ProfileUpdateRequest, db: Session = Depends(get_session)
):
    profile_service.db = db
    updated_profile = profile_service.update(3, update_request)
    print(updated_profile)
    return {"data": updated_profile, "status_code": 200}

