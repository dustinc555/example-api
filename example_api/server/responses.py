import aiohttp

from example_api.util import to_json

# aiohttp.web.json_response exists, but doesn't easily allow global behavior
# customization for things like datetime serialization. Thus why this exists
class JsonResponse(aiohttp.web.Response):
    def __init__(self, data, *args, **kwargs):
        kwargs['body'] = to_json(data, pretty_print=True)
        kwargs['charset'] = 'utf-8'
        kwargs['content_type'] = 'application/json'
        super().__init__(*args, **kwargs)

class TextResponse(aiohttp.web.Response):
    def __init__(self, data, *args, **kwargs):
        kwargs['body'] = data
        kwargs['charset'] = 'utf-8'
        kwargs['content_type'] = 'text/plain'
        super().__init__(*args, **kwargs)