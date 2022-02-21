from typing import Final, Union, Iterable, final
from models.project import Project
from models.user import User


class ProjectObj:
    def __init__(self, creator, theme, description, current_partners, required_partners):
        self.creator = creator
        self.theme = theme
        self.description = description
        self.current_partners = current_partners
        self.required_partners = required_partners

    def __repr__(self) -> str:
        pattern = "<strong>Создатель - @{0}</strong>\n" \
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


@final
class ProjectCreator(ProjectObj):
    def __init__(self, user_id: str) -> None:
        try:
            project_cursor = Project.get(Project.id == user_id)

            super().__init__(project_cursor.creator,
                             project_cursor.theme,
                             project_cursor.description,
                             project_cursor.current_partners,
                             project_cursor.required_partners)
        except Exception as e:
            raise e


@final
class ProjectSearcher:
    def __init__(self, theme: str):
        self.theme = theme
        self.id_of_projects = None
        self.__get_id_of_projects()

    def __get_id_of_projects(self) -> None:
        self.id_of_projects = iter(list(map(lambda obj: obj.id, Project.select().where(Project.theme == self.theme))))

    def get_next_project(self) -> str:
        """:returns id of next project in list"""
        project_cursor = Project.get(Project.id == next(self.id_of_projects))
        project = ProjectObj(project_cursor.creator,
                             project_cursor.theme,
                             project_cursor.description,
                             project_cursor.current_partners,
                             project_cursor.required_partners)
        return str(project)

# TODO В хендлэре вместе с проектом для искателя кнопки (далее | подать заявку | предыдущий)
