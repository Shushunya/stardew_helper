from dataclasses import dataclass


@dataclass()
class Seed:
    name: str
    price: int
    season: str
    time_to_grow: int
    multiharvest: bool = False
    regrowth_time: int = 0
    multicrop: bool = False
    throws_seeds: bool = False


@dataclass()
class Crop:
    name: str
    type: str


@dataclass()
class Animal:
    name: str
    lives_in: str
    production_time: int
    price_to_buy: int
