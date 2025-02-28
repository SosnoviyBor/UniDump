from model.BaseModel import BaseModel
from model.Dish import Dish
from model.Ingredient import Ingredient
from peewee import *


class DishIngredient(BaseModel):
    dish = ForeignKeyField(Dish, backref='ingredients', null=True)
    ingredient = ForeignKeyField(Ingredient, backref='dishes', null=True)
    count = IntegerField()

    class Meta:
        table_name = 'dish_ingredients'
