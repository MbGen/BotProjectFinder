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
class MenuCallbacks:
    LIST_OF_PROJECTS: Final[str] = "lst_of_proj"
