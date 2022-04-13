from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

import settings
from api import app


async def connect_database():
    register_tortoise(
        app=app,
        config=settings.DATABASE_CONFIG,
    )
