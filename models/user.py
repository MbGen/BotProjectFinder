from utils.db_api import db
from peewee import *
from datetime import datetime


class TypeOfUser(Enum):
    searcher = 1
    creator = 2


class Authorization(Model):
    id = IntegerField(primary_key=True)
    nickname = CharField()
    age = IntegerField()
    theme = CharField()
    skills = CharField()
    about = CharField()
    type_of_user: TypeOfUser = SmallIntegerField(db_column="typeOfUser")

    class Meta:
        database = db
