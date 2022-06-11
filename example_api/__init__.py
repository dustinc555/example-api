from importlib_metadata import version
from pathlib import Path

project_root = Path(__file__).parent

__version__ = version(__package__)
