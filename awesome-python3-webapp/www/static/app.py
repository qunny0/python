#!/usr/local/bin/python3
# _*_ coding:utf-8 -*-

__author__ = 'qunny'

...
async web application
...

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time

from datetime import datetime
from aiohttp import web

import orm

# def index(request):
# 	return web.Response(body=b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
	yield from orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='www', password='www', db='awesome')
	app = web.Application(loop=loop)
	# app.router.add_route('GET', '/', index)
	src = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return src

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

