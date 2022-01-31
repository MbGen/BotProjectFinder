from enum import Enum
from typing import Final, final


__all__ = [
    "AuthorizationCallback",
    "ThemeAuthCallback",
    "ThemeCreateCallback",
    "TypeOfUserCallback",
    "MenuCallback",
    "ProfileCallback"
]


@final
class AuthorizationCallback:
    AUTHORIZATION: Final[str] = "authorization"


@final
class ThemeAuthCallback:
    AUTH_BOTS: Final[str] = "боты"
    AUTH_WEB: Final[str] = "веб"


@final
class ThemeCreateCallback:
    CREATE_BOTS: Final[str] = "бот проект"
    CREATE_WEB: Final[str] = "веб проект"


@final
class TypeOfUserCallback:
    SEARCHER: Final[str] = "искатель"
    CREATOR: Final[str] = "создатель"


@final
class MenuCallback:
    LIST_OF_PROJECTS: Final[str] = "lst_of_proj"
    MAIN_MENU: Final[str] = "main_menu"
    PROFILE: Final[str] = "profile"


@final
class ProfileCallback:
    ABOUT_ME: Final[str] = "about_me"
    CREATE_PROJ: Final[str] = "create_proj"
    MY_PROJ_SEARCHER: Final[str] = "my_proj_searcher"
    MY_PROJ_CREATOR: Final[str] = "my_proj_creator"
