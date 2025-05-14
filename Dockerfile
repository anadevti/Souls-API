# Dockerfile
FROM python:3.11-slim as base

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia arquivos de dependências e instala
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install fastapi uvicorn sqlalchemy[asyncio] asyncpg alembic pydantic-settings

# Copia o restante do código
COPY . /app

# Expõe a porta
EXPOSE 8000

# Comando padrão
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
