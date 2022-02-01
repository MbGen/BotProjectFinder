from typing import Final, Union
from models.project import Project


class ProjectObj:
    def __init__(self, user_id: str) -> None:
        try:
            project_cursor = Project.get(Project.id == user_id)
        except Exception as e:
            raise e

        self.creator = project_cursor.creator
        self.theme = project_cursor.theme
        self.description = project_cursor.description
        self.current_partners = project_cursor.current_partners
        self.required_partners = project_cursor.required_partners

    def __repr__(self) -> str:
        pattern = "<strong>Создатель - {0}</strong>\n" \
                  "\n" \
                  "<strong>Тема проекта - {1}</strong>\n" \
                  "\n" \
                  "<strong>Количество участников - {2}/{3}</strong>\n" \
                  "\n" \
                  "<strong>Описание:</strong>" \
                  "{4}".format(self.creator,
                               self.theme,
                               self.current_partners,
                               self.required_partners,
                               self.normalize_descripion())

        return pattern

    def normalize_descripion(self) -> str:
        splitted_text = self.description.split()
        words_to_newline: Final[int] = 5
        for index, word in enumerate(splitted_text):
            if index % words_to_newline == 0:
                splitted_text.insert(index, "\n")

        return " ".join(splitted_text) + "."


class ProjectCreator(ProjectObj):
    def __init__(self, user_id: str) -> None:
        super().__init__(user_id=user_id)


class ProjectSearcher(ProjectObj):
    pass


# TODO
# 1. Объект проекта как базовый класс
# 2. Класс проект для создателя с некоторыми кнопками
# 3. Класс проект для искателя с некоторыми кнопками
# 4. Класс поиск проекта
