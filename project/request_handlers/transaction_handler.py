from tornado import web

class TransactionHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world")