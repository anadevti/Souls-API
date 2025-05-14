from sqlalchemy.ext.asyncio import AsyncSession

from app.models.game import Game
from app.repositories.game_repo import GameRepository

class GameService:
    @staticmethod
    async def list_all_games(db: AsyncSession):
        repo = GameRepository(db)
        return await repo.list_all()

    @staticmethod
    async def get_game(db: AsyncSession, game_id: int):
        repo = GameRepository(db)
        return await repo.get_by_id(game_id)

    @staticmethod
    async def search_game(db: AsyncSession, game_name: str):
        repo = GameRepository(db)
        return await repo.search_by_name(game_name)

    @staticmethod
    async def create_game(db: AsyncSession, game: Game):
        repo = GameRepository(db)
        db.add(game)
        await db.commit()
        await db.refresh(game)
        return game
