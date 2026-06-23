from flask import Flask
from flask_socketio import SocketIO
from dotenv import load_dotenv

load_dotenv()

from config import Config

from database.db import db
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp
from routes.web_pages import web_bp
from websocket.socket_events import register_socketio_handlers


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/static")
    app.config.from_object(Config)

    db.init_app(app)

    socketio = SocketIO(
        app,
        cors_allowed_origins=app.config.get("SOCKETIO_CORS_ALLOWED_ORIGINS", "*"),
        async_mode="threading",
    )

    # Make socketio available to routes for emitting
    app.extensions["socketio"] = socketio

    register_socketio_handlers(socketio)

    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(web_bp)

    return app, socketio


app, socketio = create_app()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    socketio.run(app, host="0.0.0.0", port=5000, debug=True)


