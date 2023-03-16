from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db import models

engine = create_engine("sqlite:///test_db.sqlite", echo=True)
models.Base.metadata.create_all(engine)

def fill_database():
    with Session(engine) as session:
        parsnip_seeds = models.Seed(
            name = "parsnip",
            price = 20,
            season = "spring",
            time_to_grow = 4,
            multiharvest = False,
            crop = models.Crop(name="parsnip")
        )

        bean_starter = models.Seed(
            name = "bean starter",
            price = 60,
            season = "spring",
            time_to_grow = 10,
            multiharvest = True,
            crop = models.Crop(name="bean")
        )
        
        session.add_all([parsnip_seeds, bean_starter])
        session.commit()


from sqlalchemy import select

session = Session(engine)

stmt = select(models.Crop).where(models.Crop.name.in_(["bean", "sandy"]))

for user in session.scalars(stmt):
    print(user)