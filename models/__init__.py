import sys
import os

sys.path.append(os.path.abspath(".."))

from models.user import User
from models.project import Project

User.create_table()
Project.create_table()
