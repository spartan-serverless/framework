from typing import List

from fastapi import HTTPException
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session
from datetime import datetime, date

from app.models.profile import Profile
from app.models.user import User 
from app.requests.profile import  ProfileUpdateRequest
from app.responses.profile import ProfileResponse, ProfileUpdateResponse
from app.requests.user import UserCreateRequest, UserUpdateRequest
from app.responses.user import UserCreateResponse, UserResponse, UserUpdateResponse

import logging

class ProfileService:
    """
    Service class for managing profile-related operations.
    """

    def __init__(self, db: Session):
        """
        Initialize the ProfileService class.

        Args:
            db (Session): The database session.
        """
        self.db = db

    def get_by_id(self, id: int) -> Profile:
        """
        Retrieve a profile by their ID.

        Args:
            id (int): The ID of the profile.

        Returns:
            Profile: The profile object.

        Raises:
            HTTPException: If the profile is not found.
        """
        profile = self.db.query(Profile).filter(Profile.id == id).first()
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")
        return profile


    def update(self, id: int, update_request: ProfileUpdateRequest) -> dict:
        try:
            user = self.db.query(User).filter(User.id == id).first()

            if update_request.email:
                user.email = update_request.email
                self.db.commit()
                self.db.refresh(user)

            profile = self.db.query(Profile).filter(Profile.user_id == id).first()
            profile_data = update_request.dict(exclude_unset=True)

            for key, value in profile_data.items():
                setattr(profile, key, value)

            self.db.commit()
            self.db.refresh(profile)

            response_data = {
                'user_id': user.id,
                'email': user.email,
                "firstname": profile.firstname,
                "lastname": profile.lastname,
                "middlename": profile.middlename,
                "age": profile.age,
                "mobile": profile.mobile,
                "gender": profile.gender,
                "birthdate": profile.birthdate,
                "civil_status": profile.civil_status,
                "notification_type": profile.notification_type,
                "address": profile.address,
                "created_at": profile.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": profile.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            }
            return response_data
        
        except DatabaseError as e:
            logging.error(f"Error occurred while updating category: {str(e)}")
            raise HTTPException(status_code=500, detail="Internal server error")
    
