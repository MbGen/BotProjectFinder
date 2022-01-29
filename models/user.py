import sys
import os

sys.path.append(os.path.abspath(".."))

from peewee import *
from datetime import datetime
from utils.db_api import user_db


class User(Model):
    id = IntegerField(primary_key=True, null=False, index=True, unique=True)
    nickname = CharField(default=None, unique=True, null=True)
    age = IntegerField(default=None, null=True)
    theme = CharField(default=None, null=True)
    skills = CharField(default=None, null=True)
    about = CharField(default=None, null=True)
    is_creator = BooleanField(default=False, null=False)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = user_db
