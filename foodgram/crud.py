from sqlalchemy import select
from sqlalchemy.orm import Session

from . import schemas, models


async def get_ingredients(db: Session):
    statement = select(models.Ingredient)
    result = await db.execute(statement)
    return result.scalars().all()


async def create_ingredient(db: Session, instance: schemas.IngredientBase):
    db_instance = models.Ingredient(**instance.dict())
    db.add(db_instance)
    await db.commit()
    await db.refresh(db_instance)
    return db_instance
