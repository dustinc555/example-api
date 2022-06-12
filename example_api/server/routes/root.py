from aiohttp import web

from . import routes

from example_api import logging

logger = logging.getLogger()

@routes.get('/ping')
@routes.post('/ping')
async def ping(request):
    response = web.Response(text="pong")

    return response
