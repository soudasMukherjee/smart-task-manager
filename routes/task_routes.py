from flask import Blueprint, request, jsonify, session
from database.db import db
from models.task import Task
from analytics.task_analytics import compute_analytics
from flask_socketio import SocketIO

# Import socketio from app factory pattern via current_app.extensions

def require_login():
    user_id = session.get("user_id")
    if not user_id:
        return None
    return user_id


def get_socketio():
    # Flask-SocketIO attaches itself into current_app.extensions['socketio']
    from flask import current_app

    return current_app.extensions.get("socketio")


task_bp = Blueprint("tasks", __name__, url_prefix="/api")

PRIORITIES = {"Low", "Medium", "High"}
STATUSES = {"Pending", "In Progress", "Done"}


def task_to_dict(t: Task):
    return {
        "id": t.id,
        "title": t.title,
        "description": t.description,
        "priority": t.priority,
        "status": t.status,
        "created_at": t.created_at.isoformat(),
    }


@task_bp.get("/tasks")
def get_tasks():
    user_id = require_login()
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    tasks = Task.query.filter_by(user_id=user_id).order_by(Task.created_at.desc()).all()
    return jsonify({"tasks": [task_to_dict(t) for t in tasks]}), 200


@task_bp.post("/tasks")
def add_task():
    user_id = require_login()
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    description = data.get("description") or ""
    priority = data.get("priority") or "Medium"
    status = data.get("status") or "Pending"

    if not title:
        return jsonify({"error": "title is required"}), 400
    if priority not in PRIORITIES:
        return jsonify({"error": "Invalid priority"}), 400
    if status not in STATUSES:
        return jsonify({"error": "Invalid status"}), 400

    t = Task(user_id=user_id, title=title, description=description, priority=priority, status=status)
    db.session.add(t)
    db.session.commit()

    # Emit websocket update
    socketio = get_socketio()
    if socketio:
        socketio.emit("task_added", {"task": task_to_dict(t)}, room=f"user_{user_id}")

    return jsonify({"message": "Task added", "task": task_to_dict(t)}), 201


@task_bp.put("/tasks/<int:task_id>")
def update_task(task_id: int):
    user_id = require_login()
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    t = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not t:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json(silent=True) or {}

    if "title" in data:
        title = (data.get("title") or "").strip()
        if not title:
            return jsonify({"error": "title cannot be empty"}), 400
        t.title = title

    if "description" in data:
        t.description = data.get("description") or ""

    if "priority" in data:
        priority = data.get("priority")
        if priority not in PRIORITIES:
            return jsonify({"error": "Invalid priority"}), 400
        t.priority = priority

    if "status" in data:
        status = data.get("status")
        if status not in STATUSES:
            return jsonify({"error": "Invalid status"}), 400
        t.status = status

    db.session.commit()

    socketio = get_socketio()
    if socketio:
        socketio.emit("task_updated", {"task": task_to_dict(t)}, room=f"user_{user_id}")

    return jsonify({"message": "Task updated", "task": task_to_dict(t)}), 200


@task_bp.delete("/tasks/<int:task_id>")
def delete_task(task_id: int):

    user_id = require_login()
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    t = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not t:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(t)
    db.session.commit()

    socketio = get_socketio()
    if socketio:
        socketio.emit("task_deleted", {"task_id": task_id}, room=f"user_{user_id}")

    return jsonify({"message": "Task deleted"}), 200


@task_bp.get("/analytics")
def analytics():
    user_id = require_login()
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    tasks = Task.query.filter_by(user_id=user_id).all()
    data = compute_analytics(tasks)
    return jsonify(data), 200

