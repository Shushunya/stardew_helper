from typing import List, Optional
from sqlalchemy import ForeignKey, String, Enum
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from enums import SeasonEnum, CropTypeEnum


class Base(DeclarativeBase):
    pass

class Seed(Base):
    __tablename__ = "seeds"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[int]
    season: Mapped[Enum] = mapped_column(Enum(SeasonEnum))
    time_to_grow: Mapped[int]
    multiharvest: Mapped[bool] = mapped_column(nullable=True)
    regrowth_time: Mapped[int] = mapped_column(nullable=True)
    multicrop: Mapped[bool] = mapped_column(nullable=True)
    throws_seeds: Mapped[bool] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return f"Seed(id={self.id!r}, name={self.name!r})"


class Crop(Base):
    __tablename__ = "crops"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    type: Mapped[str] = mapped_column(Enum(CropTypeEnum))
    seed_id: Mapped[int] = mapped_column(ForeignKey("seeds.id"))
    # seeds: Mapped["Seed"] = relationship(back_populates="crop")
    
    def __repr__(self) -> str:
        return f"Crop(id={self.id!r}, name={self.name!r})"

class CropQuality(Base):
    __tablename__ = "crop_qualities"
    crop_id: Mapped[int] = mapped_column(ForeignKey("crops.id"), primary_key=True)
    quality: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[int]
    energy: Mapped[int]
    health: Mapped[int]


# class Product(Base):
#     __tablename__ = "products"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str]
#     price: Mapped[int]
#     energy: Mapped[int]
#     health: Mapped[int]
#     can_be_cooked: Mapped[bool]
    
#     # produced_in: Mapped[Optional[str]]
#     def __repr__(self) -> str:
#         return f"Product(id={self.id!r}, name={self.name!r})"

# class Fish(Base):
#     __tablename__ = "fish"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str]
#     price: Mapped[int]
#     start_time: Mapped[int] = mapped_column(default=6)
#     end_time: Mapped[int] = mapped_column(default=24)
#     weather: Mapped[str] = mapped_column(default="any")
#     def __repr__(self) -> str:
#         return f"Fish(id={self.id!r}, name={self.name!r})"

# class Recipe(Base):
#     __tablename__ = "recipes"
#     crop: Mapped[int] = relationship(back_populates="recipes")
#     product: Mapped[int] = relationship(back_populates="recipes")
#     fish: Mapped[int] = relationship(back_populates="recipes")
#     meal: Mapped[int] = relationship(back_populates="recipes")
#     count: Mapped[int] = mapped_column(default=1)

# class Meal(Base):
#     __tablename__ = "meals"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str]
#     energy: Mapped[int]
#     health: Mapped[int]
#     price: Mapped[int]
