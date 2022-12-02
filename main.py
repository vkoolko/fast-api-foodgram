from typing import List

from databases import Database
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from foodgram import crud, models, schemas
from core.database import async_session, engine

from core.database import database


app = FastAPI()


# Dependency
async def get_session():
    async with async_session() as session:
        yield session


@app.on_event('startup')
async def startup_event():
    await database.connect()


@app.on_event('shutdown')
async def shutdown_event():
    await database.disconnect()


@app.get("/ingredients", response_model=List[schemas.IngredientBase])
async def get_ingredients():
    return await crud.get_ingredients()


@app.post('/ingredients', response_model=schemas.IngredientCreate)
async def create_ingredient(
        item: schemas.IngredientBase,
        db: Session = Depends(get_session)
):
    ingredient = await crud.create_ingredient(db, item)
    return ingredient
