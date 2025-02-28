from peewee import *

from model.BaseModel import BaseModel
from model.Dish import Dish


class Order(BaseModel):
    name = CharField()
    sum = FloatField()

    class Meta:
        table_name = 'orders'
