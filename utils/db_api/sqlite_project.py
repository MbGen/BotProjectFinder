from peewee import *
from os.path import dirname as up


path_to_project_db = f"{up(up(up(__file__)))}\\data\\ProjectDB.db"

project_db = SqliteDatabase(path_to_project_db)
project_db.connect()
