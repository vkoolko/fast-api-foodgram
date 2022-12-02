from sqlalchemy import select
from sqlalchemy.orm import Session

from core.database import database

from . import schemas, models


async def get_ingredients():
    query = models.Ingredient.__table__.select()
    return await database.fetch_all(query)


async def create_ingredient(db: Session, instance: schemas.IngredientBase):
    query = models.Ingredient.__table__.insert().values(**instance.dict())
    id = await database.execute(query)
    query = models.Ingredient.__table__.select().filter(
        models.Ingredient.id == id
    )
    return dict(await database.fetch_one(query))
