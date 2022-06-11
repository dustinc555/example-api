from aiohttp import web

import os

from .routes import routes
from example_api import logging, project_root
from example_api.config import Config

from example_api.util import from_json

from example_api.exceptions import ConfigError


logger = logging.getLogger()


async def get_app():
    app = web.Application()

    try:
        config = Config().load(os.environ.get('EXAMPLE_API_CONFIG'))

    except ConfigError:
        config = from_json('{}')

    finally:
        app['config'] = config

    logger.debug('config logging line')

    # Loading route(s)
    app.add_routes(routes)


    return app
