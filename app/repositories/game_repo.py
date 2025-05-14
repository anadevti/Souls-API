from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.game import Game

class GameRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_all(self) -> list[Game]:
        result = await self.db.execute(select(Game))
        return result.scalars().all()

    async def get_by_id(self, game_id: int) -> Game | None:
        result = await self.db.execute(
            select(Game).where(Game.id == game_id)
        )
        return result.scalar_one_or_none()

    async def search_by_name(self, game_name: str) -> list[Game]:
        result = await self.db.execute(
            select(Game).where(Game.name.ilike(f"%{game_name}%"))
        )
        return result.scalars().all()

    async def create(self, game: Game) -> Game:
        self.db.add(game)
        await self.db.commit()
        await self.db.refresh(game)
        return game