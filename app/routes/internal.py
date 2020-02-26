from aiohttp import web


async def healthcheck(request):
	return web.json_response({'status': 'Active!'})
