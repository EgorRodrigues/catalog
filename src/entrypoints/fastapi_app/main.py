from fastapi import FastAPI

from src.config import database

from .routers import feedstock, services, units


def create_app():
    app = FastAPI()

    app.include_router(units.router)
    app.include_router(feedstock.router)
    app.include_router(services.router)

    @app.on_event("startup")
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

    return app
