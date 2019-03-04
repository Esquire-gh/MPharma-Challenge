import logging

logger = logging.Logger("util-logger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

sformat = "%(asctime)s - %(levelname)s - %(message)s"
formattter = logging.Formatter(sformat)
console_handler.setFormatter(formattter)