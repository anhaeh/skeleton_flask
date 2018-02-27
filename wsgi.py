# -*- coding: utf-8 -*-

from app.app import app
from config.settings import *


class WsgiApplication(object):

    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.debug = DEBUG

    def start(self):
        app.run(host=self.host, port=self.port, debug=self.debug)


if __name__ == '__main__':
    wsgi_application = WsgiApplication()
    wsgi_application.start()
