from peewee import *
from os.path import dirname as up


path_to_user_db = f"{up(up(up(__file__)))}\\data\\botBD.db"

user_db = SqliteDatabase(path_to_user_db)
user_db.connect()
