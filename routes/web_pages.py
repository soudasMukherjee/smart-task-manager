from flask import Blueprint, render_template

web_bp = Blueprint("web", __name__)


@web_bp.get("/")
def login_page():
    return render_template("landing.html")


@web_bp.get("/register")
def register_page():
    return render_template("register.html")


@web_bp.get("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")


@web_bp.get("/my_tasks")
def my_tasks_page():
    return render_template("my_tasks.html")


@web_bp.get("/tasks")
def tasks_page():
    return render_template("my_tasks.html")

