from aiohttp import web
from app.routes.internal import healthcheck
from app.routes.internal import getproducts

routes = [web.get('/health', healthcheck), web.get('products', getproducts)]
