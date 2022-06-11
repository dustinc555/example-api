from time import gmtime
import inspect
import logging.config
import re
from logging import CRITICAL, ERROR, WARN, INFO, DEBUG

def getLogger(name=None):
    """
    Returns an appropriately configured logger instance

    If a name is not specified then the current module's name will be used.
    """
    if name is None:
        name = inspect.getmodule(inspect.stack(0)[1][0]).__name__
    return logging.getLogger(name)

def setLevel(level, logger=None):
    """Sets the logging level"""
    if logger == "root":
        logger = None

    if logger is None:
        CONFIG["root"]["level"] = level
        for logger in CONFIG["loggers"].values():
            logger["level"] = level
        install()
    elif isinstance(logger, str):
        if logger not in CONFIG["loggers"]:
            CONFIG["loggers"][logger] = CONFIG["loggers"][""].copy()
        CONFIG["loggers"][logger]["level"] = level
        install()
    elif hasattr(logger, 'setLevel'):
        logger.setLevel(level)
    else:
        getLogger(__name__).warn("Invalid logger specified '%s'", logger)

class _ReFilter(logging.Filter):
    def __init__(self, regexes=None):
        self.regexes = [re.compile(r) for r in (regexes or [])]

    def filter(self, record):
        if isinstance(record.msg, str):
            return not any(r.match(record.msg) for r in self.regexes)
        return True

CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "refilter": {
            "()": _ReFilter,
            "regexes": [r'poll .* (?:timeout|events)']
        }
    },
    "formatters": {
        "generic": {
            "format": "[%(asctime)s.%(msecs)03dZ][%(levelname)s][%(name)s.%(funcName)s():%(lineno)s] %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S"
        }
    },
    "handlers": {
        "stdout": {
            "level": "DEBUG",
            "formatter": "generic",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "filters": ["refilter"]
        }
    },
    "loggers": {
        "": {
            "handlers": ["stdout"],
            "level": "INFO"
        },
        "asyncio": {
            "handlers": ["stdout"],
            "level": "WARN"
        },
        "gunicorn.error": {
            "handlers": ["stdout"],
            "level": "INFO"
        }
    }
}

CONFIG["root"] = CONFIG["loggers"][""] # Legacy library compatibility

def install():
    """Installs the current configuration into the logging module"""
    logging.config.dictConfig(CONFIG)
    logging.Formatter.converter = gmtime

__all__ = ['getLogger', 'setLevel', 'install', 'CRITICAL', 'ERROR', 'WARN', 'INFO', 'DEBUG']
