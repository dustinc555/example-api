import anyconfig
from collections import UserDict
from pathlib import Path

from example_api import exceptions, logging

logger = logging.getLogger()

class Config(UserDict):
    """
    Configuration dict supporting loading from config files and setting values
    explicitly. All keys are in dot notation and any dicts get flattened to match.
    """
    def __init__(self, data=None):
        super().__init__(data)

    def __setitem__(self, key, value):
        if isinstance(value, dict):
            for k, v in value.items():
                self[key + '.' + k] = v
        else:
            super().__setitem__(key, value)

    def load(self, path):
        try:
            path = Path(path).absolute()
        except Exception:
            raise exceptions.ConfigError(
                str(path) + ' is not a valid config path')
        try:
            self.update(anyconfig.load(path))
            return self
        except Exception as e:
            raise exceptions.ConfigError('Failed to load config from ' +
                                         str(path) + ' - ' + str(e)) from e

    def asdict(self):
        return self.data
