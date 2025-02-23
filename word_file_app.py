# /word_merge_app.py

# system library -------------------------------------------------------------
import os

# packages -------------------------------------------------------------------
from flask          import Flask, send_from_directory, render_template, request
from flask          import send_file, redirect, url_for, Blueprint
from flask          import session
from werkzeug.utils import secure_filename

# local library --------------------------------------------------------------
import config.app_config        as app_config

# routes ---------------------------------------------------------------------
from routes.main_app            import base_blueprint
from routes.merge_file          import merge_blueprint
# from routes.processing          import processing_blueprint


def create_application(app_name):
    app = Flask(app_name)
    app.config.from_object(app_config)
    app.secret_key ='RandomSecretKey'

    # register blueprints
    app.register_blueprint(base_blueprint)
    app.register_blueprint(merge_blueprint)
    # app.register_blueprint(processing_blueprint)

    # ------------------------------------------------------------------------
    # return the app
    # ------------------------------------------------------------------------
    return app
