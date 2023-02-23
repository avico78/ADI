from databases import Database
import asyncio

async def initalize_connection():
	database = Database('postgresql://username:password@host:5432/database')
	try:
		await database.connect()
		print('Connected to Database')
		await database.disconnect()
		print('Disconnecting from Database')
	except :
		print('Connection to Database Failed')

if __name__ == '__main__':
	asyncio.run(initalize_connection())
