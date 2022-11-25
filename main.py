from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from foodgram import crud, models, schemas
from core.database import async_session, engine


app = FastAPI()


# Dependency
async def get_session():
    async with async_session() as session:
        yield session


@app.get("/ingredients", response_model=List[schemas.IngredientBase])
async def get_ingredients(db: Session = Depends(get_session)):
    return await crud.get_ingredients(db)


@app.post('/ingredients', response_model=schemas.IngredientCreate)
async def create_ingredient(
        item: schemas.IngredientBase,
        db: Session = Depends(get_session)
):
    ingredient = await crud.create_ingredient(db, item)
    return ingredient
