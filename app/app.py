# -*- coding: utf-8 -*-

import os
import sys
from flask import Flask
import urls


root_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, root_path)

templates_dir = os.path.join(root_path, "templates")
static_dir = os.path.join(root_path, "static")

app = Flask(__name__, template_folder=templates_dir, static_url_path=static_dir)

app.register_blueprint(urls.blueprint)
