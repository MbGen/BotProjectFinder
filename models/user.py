from utils.db_api import db
from peewee import *
from datetime import datetime


class User(Model):
    id = IntegerField(primary_key=True, null=False, index=True, unique=True)
    nickname = CharField(default=None, unique=True, null=True)
    age = IntegerField(default=None, null=True)
    theme = CharField(default=None, null=True)
    skills = CharField(default=None, null=True)
    about = CharField(default=None, null=True)
    type_of_user = BooleanField(db_column="typeOfUser")

    is_searcher = type_of_user.flag(0)
    is_creator = type_of_user.flag(1)

    class Meta:
        database = db
