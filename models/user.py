from utils.db_api import db
from peewee import *
from datetime import datetime


class User(Model):
    id = IntegerField(primary_key=True, null=False)
    nickname = CharField(default=None)
    age = IntegerField(default=None)
    theme = CharField(default=None)
    skills = CharField(default=None)
    about = CharField(default=None, null=True)
    type_of_user = BooleanField(db_column="typeOfUser")

    is_searcher = type_of_user.flag(0)
    is_creator = type_of_user.flag(1)

    class Meta:
        database = db
