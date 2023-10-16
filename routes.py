import json
import os
from typing import Union

from fastapi import APIRouter, Depends, HTTPException, Security, Header

from config.app import get_settings


settings = get_settings()


router = APIRouter(
    prefix="/api", tags=["Health Check"], responses={404: {"description": "Not found"}}
)


@router.get("/health-check")
async def health_check():
    return {"message": "OK"}