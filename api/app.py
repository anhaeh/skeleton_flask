# -*- coding: utf-8 -*-

import os
import sys
from flask import Flask
import urls

root_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, root_path)

app = Flask(__name__)

app.register_blueprint(urls.blueprint, url_prefix='/api')
