from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Crop, Seed, Base, Animal

engine = create_engine("postgresql+psycopg2://postgres:qwerty02@localhost:5432/stardew valley helper")
Base.metadata.create_all(engine)


def load_csv_to_db(file_name, table):
    import pandas as pd

    data = pd.read_csv(file_name)
    # print(data.dtypes)

    data.to_sql(con=engine, name=table.__tablename__, if_exists="append", index=False)
#
#
# load_csv_to_db(r'../csv files/seeds.csv', Seed)
# load_csv_to_db(r'../csv files/crops.csv', Crop)
# load_csv_to_db(r'../csv files/animals.csv', Animal)

def check():
    with Session(engine) as session:
        stmt = select(Crop.name).join(Seed).where((Seed.throws_seeds == True))
        seeds = session.execute(select(Seed.id, Seed.name).order_by(Seed.id)).all()
        crops = session.execute(select(Crop)).all()
        result = session.execute(stmt).all()
        animals = session.execute(select(Animal.name)).all()

        print(result)
        print(animals, seeds)

        # session.add_all([parsnip, jazz, cauliflower, garlic, green_bean, kale, potato, strawberry, tulip,
        # rice]) session.add_all([blueberry, corn, hops, pepper, melon, poppy, radish, cabbage, spangle, sunflower,
        # tomato, wheat])
        session.commit()


check()