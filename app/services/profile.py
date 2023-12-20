from typing import List

from fastapi import HTTPException
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session

from app.models.profile import Profile
from app.requests.profile import ProfileCreateRequest, ProfileUpdateRequest
from app.responses.profile import ProfileCreateResponse, ProfileResponse, ProfileUpdateResponse

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

    def all(self, page: int, items_per_page: int) -> List[ProfileResponse]:
        """
        Retrieve all profiles with pagination.

        Args:
            page (int): The page number.
            items_per_page (int): The number of items per page.

        Returns:
            Tuple[List[ProfileResponse], int]: A tuple containing the list of profile responses and the total number of profiles.

        Raises:
            HTTPException: If there is an internal server error.
        """
        try:
            offset = (page - 1) * items_per_page
            logging.info(f"offset: {offset}")
            profiles = self.db.query(Profile).offset(offset).limit(items_per_page).all()
            responses = [
                ProfileResponse(**profile.__dict__) for profile in profiles
            ]

            return responses, self.total()
        except DatabaseError as e:
            raise HTTPException(status_code=500, detail="Internal server error")
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal server error")

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
        """
        Update a profile in the database.

        Args:
            id (int): The ID of the profile.
            profile (ProfileUpdateRequest): The profile update request object.

        Returns:
            ProfileUpdateResponse: The response data of the updated profile.
        """
        item = self.get_by_id(id)
        data = profile.dict(exclude_unset=True)
        if "password" in data:
            data["password"] = "hashed_" + data["password"]
        for key, value in data.items():
            setattr(item, key, value)
        self.db.commit()
        self.db.refresh(item)
        response_data = {
            "id": item.id,
            "username": item.username,
            "email": item.email,
        }
        return response_data

