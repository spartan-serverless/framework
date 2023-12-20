from typing import List

from fastapi import HTTPException
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session
from datetime import datetime, date

from app.models.profile import Profile
from app.requests.profile import  ProfileUpdateRequest
from app.responses.profile import ProfileResponse, ProfileUpdateResponse

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

    def find(self, id: int) -> ProfileResponse:
        """
        Find a profile by their ID and return the profile response.

        Args:
            id (int): The ID of the profile.

        Returns:
            ProfileResponse: The profile response.

        Raises:
            HTTPException: If the profile is not found.
        """
        item = self.get_by_id(id)
        return ProfileResponse(**item.__dict__)

    def update(self, id: int, profile: ProfileUpdateRequest) -> ProfileUpdateResponse:
        try:
            item = self.get_by_id(id)
            data = profile.dict(exclude_unset=True)
            
            for key, value in data.items():
                setattr(item, key, value)
            
            self.db.commit()
            
            self.db.refresh(item)


            response_data = {
                "id": item.id,
                "lastname": item.lastname,
                "firstname": item.firstname,
                "middlename": item.middlename,
                "age": item.age,
                "mobile": item.mobile,
                "gender": item.gender,
                "birthdate": item.birthdate,
                "civil_status": item.civil_status,
                "notification_type": item.notification_type,
                "address": item.address,
                "created_at": item.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": item.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            }

            return response_data
        except DatabaseError as e:
            logging.error(f"Error occurred while updating category: {str(e)}")
            raise HTTPException(status_code=500, detail="Internal server error")

