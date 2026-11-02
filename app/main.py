from fastapi import FastAPI
from app.router import api_router
from app.api.routes import health

def create_app()-> FastAPI:
    app=FastAPI(
        title="SnipBox",
        version="0.1.0",
        description="Share text Snippets"
    )
    app.include_router(health.router)
    app.include_router(api_router)

    return app
app=create_app()
