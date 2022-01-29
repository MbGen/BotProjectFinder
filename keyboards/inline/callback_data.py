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
    CREATE_BOTS: Final[str] = "bots\_create"
    CREATE_WEB: Final[str] = "web\_create"


@final
class TypeOfUserCallback:
    SEARCHER: Final[str] = "искатель"
    CREATOR: Final[str] = "создатель"


@final
class MenuCallback:
    LIST_OF_PROJECTS: Final[str] = "lst\_of\_proj"
    MAIN_MENU: Final[str] = "main\_menu"
    PROFILE: Final[str] = "profile"


@final
class ProfileCallback:
    ABOUT_ME: Final[str] = "about\_me"
    CREATE_PROJ: Final[str] = "create\_proj"
    MY_PROJ_SEARCHER: Final[str] = "my\_proj\_searcher"
    MY_PROJ_CREATOR: Final[str] = "my\_proj\_creator"
