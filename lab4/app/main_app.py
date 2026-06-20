# Imported symbols here please!
from flask import Flask, request, render_template, redirect, session
from .pages.index import index_pages
from .pages.auth import auth_pages
from .pages.iot_api import iot_api


# Initialize the Flask application
# Note: static folder means all files in there will be automatically offered over HTTP
app = Flask(__name__, static_folder="../public",
            template_folder="../templates")
app.secret_key = "gxnMaYjinQ27DeBwgKsDyuDQO"
app.register_blueprint(index_pages)
app.register_blueprint(auth_pages)
app.register_blueprint(iot_api)