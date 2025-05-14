from fastapi import FastAPI
from app.routers.game_router import router as game_router

app = FastAPI(title="Souls API")
app.include_router(game_router)
