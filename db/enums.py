from enum import Enum


class CropTypeEnum(Enum):
    fruit = 0
    vegetable = 1
    flower = 2


class SeasonEnum(Enum):
    winter = 0
    spring = 1
    summer = 2
    autumn = 3


class AnimalHome(Enum):
    coop = 0
    barn = 1


class ProductSourceType(Enum):
    crop = 0
    animal = 1
