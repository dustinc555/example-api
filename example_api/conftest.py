import pytest
from example_api.config import Config
from example_api.server.app import get_app as _get_app

import os
import base64
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import threading

@pytest.fixture(autouse=True)
def setup_system_files():
    pass

@pytest.fixture(scope="session", autouse=True)
def set_envvars():
    os.environ['EXAMPLE_API_CONFIG'] = os.path.abspath('sample-config.toml')


@pytest.fixture(scope="session", autouse=True)
def app_config():
    config = Config({})
    config.load('sample-config.toml')
    return config


@pytest.fixture(scope="function", autouse=True)
def get_app(app_config, aiohttp_client, event_loop):
    async def _setup():
        app = await _get_app()

        app['config'] = app_config
        client = await aiohttp_client(app)

        return client

    return _setup