# -*- coding: utf-8 -*-
from flask import Blueprint
from views.users import Users

blueprint = Blueprint('api', __name__)

blueprint.add_url_rule('/users', view_func=Users.as_view('users'), methods=['GET', 'POST', 'PUT', 'DELETE'])

