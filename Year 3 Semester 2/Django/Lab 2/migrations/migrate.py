from peewee import MySQLDatabase

from model.Dish import Dish
from model.DishIngredient import DishIngredient
from model.Ingredient import Ingredient
from model.Order import Order
from model.OrderDish import OrderDish

database = MySQLDatabase(database='django_lab2', user='root', password='', host='localhost')

database.drop_tables([
    Ingredient, Dish, DishIngredient, Order, OrderDish
])
database.create_tables([
    DishIngredient, OrderDish, Ingredient, Dish, Order
])

# Додавання в базу інгредієнтів
with database.atomic():
    spagetti = Ingredient.create(name="Спагетті", price=40, count=11550).id
    tomato = Ingredient.create(name="Помідор", price=96, count=2200).id
    chicken = Ingredient.create(name="Куряче філе", price=140, count=4600).id
    mushrooms = Ingredient.create(name="Гриби печериці", price=109, count=1900).id
    cheese = Ingredient.create(name="Сир твердий", price=300, count=900).id
    rice = Ingredient.create(name="Рис", price=60, count=3850).id
    potato = Ingredient.create(name="Картопля", price=20, count=29750).id
    carrot = Ingredient.create(name="Морква", price=20, count=9900)
    beef = Ingredient.create(name="М'ясо свинини", price=210, count=2400).id
    egg = Ingredient.create(name="Куряче яйце", price=100, count=6000).id
    raisins = Ingredient.create(name="Ізюм", price=150, count=1250).id

# Додавання в базу страв
pasta = Dish.create(name="Паста з куркою та грибами", price=40, count=11550)
DishIngredient.bulk_create([
    DishIngredient(dish=pasta, ingredient=spagetti, count=200),
    DishIngredient(dish=pasta, ingredient=tomato, count=200),
    DishIngredient(dish=pasta, ingredient=chicken, count=200),
    DishIngredient(dish=pasta, ingredient=mushrooms, count=200),
])
meat_potato = Dish.create(name="Картопля з м'ясом", price=96, count=2200).id
DishIngredient.bulk_create([
    DishIngredient(dish=meat_potato, ingredient=potato, count=200),
    DishIngredient(dish=meat_potato, ingredient=beef, count=200),
    DishIngredient(dish=meat_potato, ingredient=cheese, count=200),
    DishIngredient(dish=meat_potato, ingredient=tomato, count=200),
])
pilaf = Dish.create(name="Плов з овочами", price=140, count=4600).id
DishIngredient.bulk_create([
    DishIngredient(dish=pilaf, ingredient=raisins, count=200),
    DishIngredient(dish=pilaf, ingredient=beef, count=200),
    DishIngredient(dish=pilaf, ingredient=carrot, count=200),
    DishIngredient(dish=pilaf, ingredient=rice, count=200),
    DishIngredient(dish=pilaf, ingredient=tomato, count=200),
])
chicken_rice = Dish.create(name="Рис з куркою", price=109, count=1900).id
DishIngredient.bulk_create([
    DishIngredient(dish=chicken_rice, ingredient=chicken, count=200),
    DishIngredient(dish=chicken_rice, ingredient=rice, count=200),
])
