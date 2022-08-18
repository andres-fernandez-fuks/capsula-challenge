from tornado import web

class AccountHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world")