from loguru import logger
import sys


logger.add(sys.stderr,
           format="{time} {level} {message}",
           level="INFO"
           )

loger.add("logs\\logs.log",
          rotation="20 mb"
          )
