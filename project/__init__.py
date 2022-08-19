import asyncio
from tornado import web
from project.request_handlers.account_handler import AccountHandler
from project.request_handlers.transaction_handler import TransactionHandler

PORT = 8080

async def app():
    application = web.Application([
        (r"/account/balance", AccountHandler),
        (r"/transaction", TransactionHandler),
    ])
    application.listen(PORT)
    await asyncio.Event().wait()