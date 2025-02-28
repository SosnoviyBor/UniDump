from peewee import MySQLDatabase, Model


class BaseModel(Model):
    class Meta:
        database = MySQLDatabase('django_lab2', user='root', password='', host='localhost')