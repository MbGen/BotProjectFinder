from typing import final, Union
from models.user import User, DoesNotExist


@final
class Validator:

    @staticmethod
    def is_valid_nickname(nickname: str) -> bool:
        try:
            User.get(nickname=nickname)
            return False
        except DoesNotExist:
            return True

    @staticmethod
    def is_valid_age(age: Union[str, int]) -> bool:
        try:
            return 0 < int(age) < 100
        except ValueError:
            return False
