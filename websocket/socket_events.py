from flask import session
from flask_socketio import join_room, leave_room


def register_socketio_handlers(socketio):
    @socketio.on("connect")
    def on_connect():
        user_id = session.get("user_id")
        if user_id:
            join_room(f"user_{user_id}")

    @socketio.on("disconnect")
    def on_disconnect():
        user_id = session.get("user_id")
        if user_id:
            leave_room(f"user_{user_id}")

