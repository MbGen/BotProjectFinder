from utils.db_api import db
from peewee import *
from datetime import datetime
from enum import Enum


class TypeOfUser(Enum):
    searcher = 1
    creator = 2


class User(Model):
    id = IntegerField(primary_key=True)
    nickname = CharField()
    age = IntegerField()
    theme = CharField()
    skills = CharField()
    about = CharField()
    type_of_user: TypeOfUser = BitField(db_column="typeOfUser")

    class Meta:
        database = db
