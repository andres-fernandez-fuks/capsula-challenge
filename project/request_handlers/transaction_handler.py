from tornado import web

class TransactionHandler(web.RequestHandler):
    def post(self):
        self.write("Hello, world")