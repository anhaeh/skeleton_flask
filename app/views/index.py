# -*- coding: utf-8 -*-
from flask.views import MethodView


class IndexView(MethodView):

    def get(self):
        return "Hello Happy World!"

    def post(self):
        pass
