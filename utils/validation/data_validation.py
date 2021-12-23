from typing import final, Union


@final
class Validator:

    @staticmethod
    def is_valid_nickname(nickname: str) -> bool:
        # TODO: запрос в бд, есть ли уже человек с таким ником, если есть -> False, а иначе -> True
        return True

    @staticmethod
    def is_valid_age(age: Union[str, int]) -> bool:
        try:
            return 0 < int(age) < 100
        except ValueError:
            return False
