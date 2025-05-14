from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# cria o engine
engine = create_async_engine(
    str(settings.DATABASE_URL),
    echo=True,
)

# factory de sessões async
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,  # evita expirar objetos após commit
)

# dependência do FastAPI para injetar sessão
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
