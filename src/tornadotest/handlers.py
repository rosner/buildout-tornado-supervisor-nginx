from tornado.web import RequestHandler

import json

class MainHandler(RequestHandler):

    def get(self):
        self.write('Hello World')
