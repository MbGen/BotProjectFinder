from loguru import logger
import sys

logger.add(sys.stderr,
           format="{time} {level} {message}",
           level="INFO"
           )

logger.add("logs\\logs.log",
           rotation="20 mb",
           enqueue=True
           )
