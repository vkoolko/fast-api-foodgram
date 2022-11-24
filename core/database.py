from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:masterkey@localhost/fastapi_foodgram"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()
