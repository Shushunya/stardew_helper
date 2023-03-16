from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import models as m

engine = create_engine("sqlite:///csv_db.sqlite3")
m.Base.metadata.create_all(engine)


import pandas as pd

data = pd.read_csv("seeds.csv")
# print(data.dtypes)

data.to_sql(con=engine, name=m.Seed.__tablename__, if_exists="append", index=False)

session = sessionmaker(bind=engine)
s = session()

results = s.query(m.Seed).where(m.Seed.multiharvest==True)

for r in results:
    print(r)