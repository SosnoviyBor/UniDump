from peewee import *

from model.BaseModel import BaseModel


class Ingredient(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    price = FloatField()
    count = IntegerField()

    class Meta:
        table_name = 'ingredients'
