from pydantic import BaseModel


class IngredientBase(BaseModel):
    name: str
    measure_unit: str

    class Config:
        orm_mode = True
        