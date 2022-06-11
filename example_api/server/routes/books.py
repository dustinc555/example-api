from . import routes

from example_api import logging
from example_api.db.static.books import get_all_books
from ..responses import JsonResponse

import json

logger = logging.getLogger()

@routes.get('/books')
async def get_books(request):
    db_path = request.app['config'].get('db.path', '/code/database')
    return JsonResponse(get_all_books(db_path))

@routes.get('/books/available')
async def get_books(request):
    db_path = request.app['config'].get('db.path', '/code/database')
    all_books = [x for x in get_all_books(db_path) if x['isAvailable']]
    return JsonResponse(all_books)