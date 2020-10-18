import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


async def handle(request):
  name = request.match_info.get('name', "awesome")
  text = "hello," + name
  return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
  web.run_app(app)
# def index(request):
#   return web.Response(body=b'<h1>hello world</h1>')


# @asyncio.coroutine
# def init(loop):
#   app = web.Application(loop=loop)
#   app.router.add_route('GET', '/index', index)
#   srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
#   logging.info('start')
#   return srv

# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()