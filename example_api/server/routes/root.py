from aiohttp import web

from . import routes

from example_api import logging

logger = logging.getLogger()

@routes.get('/ping')
@routes.post('/ping')
async def ping(request):
    response = web.Response(text="pong")

    return response

@routes.get('/')
@routes.post('/')
async def root(request):
    
    response = web.Response(text=open('/code/public/index.html').read(), content_type='text/html')

    return response
