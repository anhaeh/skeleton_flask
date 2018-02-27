# -*- coding: utf-8 -*-
from flask import Blueprint
from views.index import IndexView

blueprint = Blueprint('urls_app', __name__)

blueprint.add_url_rule('/', view_func=IndexView.as_view('index_view'), methods=['GET', 'POST'])
