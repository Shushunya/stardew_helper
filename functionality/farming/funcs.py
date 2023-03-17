# connections = [
#     ('seeds', 'crops', 'crops_qualities', 'products'),
#     ('animals', 'animal_products', 'animal_products_qualities', 'products', 'meals')
# ]
#
from functionality.farming.item_classes import *
# from db.models import *
def get_all_items(item_type: str) -> list[str]:
    import db
    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import Session

    result = []

    engine = create_engine("postgresql+psycopg2://postgres:qwerty02@localhost:5432/stardew valley helper")
    db.Base.metadata.create_all(engine)

    match item_type:
        case 'seeds':
            with Session(engine) as session:
                seeds = session.execute(select(db.Seed)).first()
                # print(seeds.name)
                result = seeds
        case 'crops':
            with Session(engine) as session:
                crops = session.execute(select(db.Crop)).all()
                result = crops
        case 'animals':
            with Session(engine) as session:
                animals = session.execute(select(db.Animal)).all()
                result = animals

    return result


def pretty_output(data):
    print(data)
    #max len of a crop
    # crops_count = len(data)
    # print(crops_count)
    # count_string = "#".rjust(len(str(crops_count)))
    # print(count_string)
    # name_len = max([len(data[i][0].name) for i in range(crops_count)])
    # name_string = "name".center(name_len)
    # type_string = "type".center(len("vegetable"))
    # header_string = count_string+"|"+name_string+"|"+type_string+"|"
    # print(header_string)
    # print("-"*len(header_string))

    for i in range(len(data)):
    #     item_count = f"{i}".rjust(len(str(crops_count)))
    #     item_name = f"{data[i][0].name}".center(name_len)
    #     item_type = f"{data[i][0].type.name}".center(len("vegetable"))
    #     print(item_count+"|"+item_name+"|"+item_type+"|")
        print(data[i][0])


