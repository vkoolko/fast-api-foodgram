from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from foodgram import crud, models, schemas
from core.database import SessionLocal, engine


app = FastAPI()


# Dependency
async def get_db():
    async with SessionLocal() as session:
        yield session


@app.get("/ingredients", response_model=List[schemas.IngredientBase])
async def read_users(db: Session = Depends(get_db)):
    return await crud.get_ingredients(db)
