from peewee import *
import os

path_to_db = f"{os.path.abspath('.')}\\data\\botBD.db"

db = SqliteDatabase(path_to_db)
db.connect()
