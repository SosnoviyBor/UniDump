from peewee import *
from model.BaseModel import BaseModel
from model.Ingredient import Ingredient


class Dish(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    ingredients = ManyToManyField(Ingredient, backref='dishes')

    class Meta:
        table_name = 'dishes'
