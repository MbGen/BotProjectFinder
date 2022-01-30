from typing import Final


class ProjectObj:
    def __init__(self,
                 creator: str,
                 theme: str,
                 description: str,
                 current_partners: int,
                 required_partners) -> None:
        self.creator = creator
        self.theme = theme
        self.description = description
        self.current_partners = current_partners
        self.required_partners = required_partners

    def __repr__(self) -> str:
        pattern = """
        <strong> Создатель - {0}</strong>
        """.format(self.creator)

        return repr(pattern)

    def normalize_descripion(self) -> str:
        splitted_text = self.description.split()
        words_to_newline: Final[int] = 5
        for index, word in enumerate(splitted_text):
            if index % words_to_newline == 0:
                splitted_text.insert(index, "\n")

        return " ".join(splitted_text)


class ProjectCreator(ProjectObj):
    def __init__(self,
                 creator,
                 theme,
                 description,
                 current_partners,
                 required_partners) -> None:
        super().__init__(creator,
                         theme,
                         description,
                         current_partners,
                         required_partners)


class ProjectSearcher(ProjectObj):
    pass


# TODO
# 1. Объект проекта как базовый класс
# 2. Класс проект для создателя с некоторыми кнопками
# 3. Класс проект для искателя с некоторыми кнопками
# 4. Класс поиск проекта
