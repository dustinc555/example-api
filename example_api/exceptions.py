class ConfigError(Exception):
    """An error encountered while loading configuration"""
    pass


class NotFoundError(Exception):
    """Generic db item not found error"""
    pass