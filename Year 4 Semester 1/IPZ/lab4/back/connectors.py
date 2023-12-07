import mysql.connector
from pymongo import MongoClient

import config

def mysql_conn():
    return mysql.connector.connect(
        host = config.MYSQL_CREDENTIALS["host"],
        user = config.MYSQL_CREDENTIALS["user"],
        password = config.MYSQL_CREDENTIALS["password"]
    )

def mongo_conn():
    return MongoClient(config.MONGO_CREDENTIALS)