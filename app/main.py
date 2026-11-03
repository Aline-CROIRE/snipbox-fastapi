from fastapi import FastAPI

from app.router import api_router
from app.core.config import get_settings
from app.api.routes import health

def create_app(settings: Settings | None=None) -> FastAPI:
    settings=settings or get_settings()
    app=FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="Share text snippets with ease.",
        debug=settings.debug
    )
    app.state.settings=settings
    app.include_router(api_router)
    app.include_router(health.router)

    return app

app=create_app()
