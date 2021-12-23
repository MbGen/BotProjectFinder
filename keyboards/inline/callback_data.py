from enum import Enum
from typing import Final, final


@final
class CallbackData:
    AUTHORIZATION: Final[str] = "auth"
    BOTS: Final[str] = "bots"
    WEB: Final[str] = "web"
    SEARCHER: Final[str] = "searcher"
    CREATOR: Final[str] = "creator"
