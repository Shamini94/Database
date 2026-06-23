from flask import Flask
from routes.events_routes import events_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(events_bp)

    return app