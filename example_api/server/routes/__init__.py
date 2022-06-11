from aiohttp import web
from example_api.util import import_submodules


routes = web.RouteTableDef()

# the intent here is to build wide for scalability
import_submodules()
__all__ = ["routes", "template", "render_template"]
