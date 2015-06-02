#!usr/local/bin/python3


@asyncio.coroutine
def create_pool(loop, **kw):
	logging.info('create database connectioin pool...')
	global __pool
	__pool = yield from aiomysql.create_pool(
		host = kw.get('host', 'localhost'),
		port = kw.get('port', 3306),
		user = kw['user'],
		password = kw['password'],
		db = kw['db'],
		charset 

	)