from peewee import *
from model.BaseModel import BaseModel
from model.Order import Order
from model.Dish import Dish


class OrderDish(BaseModel):
    order = ForeignKeyField(Order)
    dish = ForeignKeyField(Dish)
    count = IntegerField()

    class Meta:
        table_name = 'order_dishes'
