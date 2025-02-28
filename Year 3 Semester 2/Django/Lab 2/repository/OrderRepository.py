from datetime import datetime
from peewee import *
from model.Order import Order
from model.OrderDish import OrderDish
from model.Ingredient import Ingredient

database = MySQLDatabase(database='django_lab2', user='root', password='', host='localhost')


class OrderRepository:

    def create(self, order: Order):
        with database.atomic():
            order_db = Order.create(name=order.name, sum=order.sum, created=datetime.now())
            for dish in order.dishes:
                OrderDish.create(order=order_db, dish=dish.id, count=dish.count)

        return order_db.id
