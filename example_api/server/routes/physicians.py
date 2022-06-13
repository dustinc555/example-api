from . import routes

from example_api import logging
from ..responses import JsonResponse

import json

logger = logging.getLogger()

@routes.get('/physicians')
async def get_books(request):
    static_db = request.app['static_db']
    print(static_db.get_all_physicians())
    return JsonResponse(static_db.get_all_physicians())

@routes.get('/physicians/appointments/{id}')
async def get_books(request):
    physician_id = request.match_info['id']
    static_db = request.app['static_db']
    return JsonResponse(static_db.get_physician_appointments(physician_id))

