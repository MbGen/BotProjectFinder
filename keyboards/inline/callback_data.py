from enum import Enum
from typing import Final, final


@final
class AuthorizationCallback:
    AUTHORIZATION: Final[str] = "auth"


@final
class ThemeCallback:
    BOTS: Final[str] = "bots"
    WEB: Final[str] = "web"


@final
class TypeOfUserCallback:
    SEARCHER: Final[str] = "searcher"
    CREATOR: Final[str] = "creator"


@final
class MenuCallback:
    LIST_OF_PROJECTS: Final[str] = "lst_of_proj"
    MAIN_MENU: Final[str] = "main_menu"
    PROFILE: Final[str] = "profile"


@final
class ProfileCallback:
    ABOUT_ME: Final[str] = "about_me"
    CREATE_PROJ: Final[str] = "create_proj"
