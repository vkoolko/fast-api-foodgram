from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from core.database import Base


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    measure_unit = Column(String(25))
