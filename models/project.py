import sys
import os

sys.path.append(os.path.abspath(".."))

from peewee import *
from datetime import datetime
from utils.db_api import project_db


class Project(Model):
    id = IntegerField(primary_key=True, null=False, index=True, unique=True)
    creator = CharField(default=None, unique=True, null=True)
    theme = CharField(default=None, null=True)
    description = CharField(default=None, unique=False, null=True, max_length=250)
    current_partners = SmallIntegerField(default=1, unique=False, null=False)
    required_partners = SmallIntegerField(default=2, unique=False, null=False)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = project_db
