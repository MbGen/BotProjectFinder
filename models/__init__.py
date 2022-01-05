import sys
import os
sys.path.append(os.path.abspath(".."))
from models.user import User

User.create_table()
