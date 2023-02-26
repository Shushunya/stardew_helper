class Meal:
    def __init__(self, name, ingredients, energy, health) -> None:
        self.name = name
        self.ingredients = ingredients
        self.energy = energy
        self.health = health

class Ingredient:
    def __init__(self, name, count=1) -> None:
        self.name = name
        self.count = count

acquired_meals = [
    Meal(name="Fried Egg", ingredients=[Ingredient("Egg")], energy=50, health=22),
    Meal(name="Omelet", ingredients=[Ingredient("Egg"), Ingredient("Milk")], energy=100, health=45)
]

seeds_available = []

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import database.models as models

engine = create_engine("sqlite:///test_db.sqlite", echo=True)
session = Session(engine)

stmt = select(models.Seed)
session.rollback()
for seed in session.scalars(stmt):
    seeds_available.append(seed)

print(seeds_available)

print("Acquired meals: ")
for i in range(len(acquired_meals)):
    print(i, acquired_meals[i].name)

