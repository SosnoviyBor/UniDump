from peewee import MySQLDatabase

from model.Dish import Dish
from model.Ingredient import Ingredient
from model.DishIngredient import DishIngredient

database = MySQLDatabase(database='django_lab2', user='root', password='', host='localhost')

class DishRepository:

    def get_dishes(self) -> list[Dish]:
        dishes = []
        query = Dish.select(Dish, Ingredient).join(DishIngredient).join(Ingredient)
        count = 0
        names = []
        for dish in query:
            if dish.name in names:
                continue
            names.append(dish.name)
            count += 1
            ingredients = []
            for di in dish.ingredients:
                ingredients.append(di.ingredient)
            dishes.append(Dish(id=dish.id, name=dish.name, ingredients=ingredients, ))

        return dishes

    def create(self, name: str, ingredients: list):
        with database.atomic():
            dish = Dish.create(name=name)
            for ingredient in ingredients:
                DishIngredient.create(dish=dish.id, ingredient=ingredient.id, count=200)
        return dish.id

    def update(self, dish: Dish, ingredients: list):
        with database.atomic():
            existing_dish = Dish.get_by_id(dish.id)
            existing_dish.name = dish.name
            existing_dish.save()

            DishIngredient.delete().where(DishIngredient.dish == existing_dish).execute()

            for ingredient in ingredients:
                DishIngredient.create(dish=existing_dish, ingredient=ingredient, count=200)

    def delete(self, dish: Dish):
        with database.atomic():
            DishIngredient.delete().where(DishIngredient.dish == dish).execute()
            Dish.delete_by_id(dish.id)
