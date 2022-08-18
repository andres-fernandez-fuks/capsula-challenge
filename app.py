import asyncio


async def main():
    application = tornado.web.Application([
        (r"account/balance", AccountHandler),
        (r"/transaction", TransactionHandler),
    ])
    application.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())