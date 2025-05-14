from fastapi import FastAPI
from app.routers import game_router  # e outros routers

app = FastAPI(title="Souls API")
app.include_router(game_router.router)