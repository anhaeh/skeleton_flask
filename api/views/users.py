# -*- coding: utf-8 -*-
from flask import jsonify
from flask.views import MethodView


class Users(MethodView):

    def get(self):
        return jsonify(
            {
                'status': 'OK',
                'users': [
                    {'name': 'Pepe', 'age': 35, 'ocupation': "Engineer"},
                    {'name': 'Bob', 'age': 20, 'ocupation': "Student"}
                ]
            }
        )

    def post(self):
        # create user
        pass

    def put(self):
        # update user
        pass

    def delete(self):
        # delete user
        pass
