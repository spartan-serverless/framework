from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from config.app import get_settings
from routes import router

description = """
Artisan for cloud native app development. 🚀
"""

tags_metadata = [
    {
        "name": "Default",
        "description": "This endpoint allows performing operations related to users. It provides functionality to save and download users through a RESTful API.",
    }
]

settings = get_settings()
root_path = "/dev/"
if settings.APP_ENVIRONMENT == "local":
    root_path = "/"

app = FastAPI(
    title="Artisan",
    description=description,
    version="0.1.0",
    terms_of_service="N/A",
    contact={
        "name": "Sydel Palinlin",
        "url": "https://github.com/nerdmonkey",
        "email": "sydel.palinlin@gmail.com",
    },
    openapi_tags=tags_metadata,
    root_path=root_path,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

handle = Mangum(app)
