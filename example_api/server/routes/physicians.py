from . import routes

from example_api import logging
from example_api.exceptions import NotFoundError
from ..responses import JsonResponse

import json

from aiohttp import web

logger = logging.getLogger()

@routes.get('/physicians')
async def get_physicians(request):
    static_db = request.app['static_db']
    return JsonResponse(static_db.get_all_physicians())

@routes.get('/physicians/{id}/appointments')
async def get_physician_appointments(request):
    physician_id = request.match_info['id']
    static_db = request.app['static_db']
    return JsonResponse(static_db.get_physician_appointments(physician_id))

@routes.post('/physicians/{id}/appointments/add')
async def add_new_appointment(request):
    physician_id = request.match_info['id']
    static_db = request.app['static_db']

    new_appointments = await request.json()

    try:
        static_db.add_physician_appointments(physician_id, new_appointments)
    except NotFoundError as exc:
        return Web.NotFoundError()
    except Exception as exc:
        logger.error(exc)
        return web.HTTPInternalServerError()

    return web.Response()
