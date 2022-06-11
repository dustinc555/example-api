from . import routes

from example_api import logging
from example_api.db.static.physicians import get_all_physicians, get_physician_appointments
from ..responses import JsonResponse

import json

logger = logging.getLogger()

@routes.get('/physicians')
async def get_books(request):
    db_path = request.app['config'].get('db.path', '/code/database')
    return JsonResponse(get_all_physicians(db_path))

@routes.get('/physicians/appointments/{id}')
async def get_books(request):
    physician_id = request.match_info['id']
    db_path = request.app['config'].get('db.path', '/code/database')
    return JsonResponse(get_physician_appointments(db_path, physician_id))

