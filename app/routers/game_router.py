from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.game_schema import GameOut
from app.services.game_service import GameService
from app.db.session import get_db
from app.models.game import Game

router = APIRouter(prefix="/games", tags=["Games"])

@router.get("/", response_model=List[GameOut])
async def list_games(db: AsyncSession = Depends(get_db)):
    return await GameService.list_all_games(db)

@router.get("/{game_id}", response_model=GameOut)
async def get_game(game_id: int, db: AsyncSession = Depends(get_db)):
    game = await GameService.get_game(db, game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game não encontrado")
    return game

@router.get("/search/{game_name}", response_model=List[GameOut])
async def search_game(game_name: str, db: AsyncSession = Depends(get_db)):
    games = await GameService.search_game(db, game_name)
    if not games:
        raise HTTPException(status_code=404, detail="Nenhum jogo encontrado")
    return games

@router.post("/insert-game", response_model=GameOut)
async def insert_game(game: GameOut, db: AsyncSession = Depends(get_db)):
    new_game = Game(**game.dict())
    db.add(new_game)
    await db.commit()
    await db.refresh(new_game)
    return new_game