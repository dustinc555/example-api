__version__ = '1.0.0'


from gunicorn import util
from gunicorn.app.base import BaseApplication

from example_api import logging

logger = logging.getLogger()


def start(config):
    logger.info('Initializing api')

    Server(config).run()


class Server(BaseApplication):
    def __init__(self, app_config):
        self.app_config = app_config or {}
        super().__init__()

    def load_config(self):
        # https://docs.gunicorn.org/en/stable/settings.html
        self.cfg.set('bind',
                     self.app_config.get('server.address', '0.0.0.0:9080'))
        self.cfg.set('workers', self.app_config.get('server.workers', 1))
        self.cfg.set('reload', self.app_config.get('server.reload', False))
        self.cfg.set('accesslog',
                     self.app_config.get('server.access_log_path'))
        self.cfg.set('keyfile', self.app_config.get('server.keyfile_path'))
        self.cfg.set('certfile', self.app_config.get('server.certfile_path'))
        self.cfg.set('worker_class', 'aiohttp.GunicornUVLoopWebWorker')
        self.cfg.set('logconfig_dict', logging.CONFIG)
        self.cfg.set('proc_name', 'example_api_server')

    def load(self):
        return util.import_app('example_api.server.app:get_app')