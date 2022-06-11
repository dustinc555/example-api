import importlib
import inspect
import pkgutil

from example_api import logging
logger = logging.getLogger()

def import_submodules(package=None, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if package is None:
        package = inspect.getmodule(inspect.stack(0)[1][0]).__name__

    if isinstance(package, str):
        package = importlib.import_module(package)

    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name

        logger.debug('Dynamically importing %s', full_name)
        try:
            results[full_name] = importlib.import_module(full_name)
        except ImportError as e:
            logger.info('Failed to import %s: "%s"', full_name, e)

        if recursive and is_pkg:
            results.update(import_submodules(full_name))

    return results
