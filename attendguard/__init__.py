"""AttendGuard package factory and blueprint registration.

This module provides create_app() which registers blueprints and injects
global template context for demo rendering (no DB, no auth).
"""
from datetime import date
import os
from flask import Flask, render_template


# Resolve templates directory relative to project root so the package can find
# the top-level `templates/` folder created earlier.
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")


class DummyUser:
    def __init__(self, name=None, authenticated=False):
        self.name = name or "Demo User"
        self.is_authenticated = authenticated


def create_app():
    app = Flask(__name__, template_folder=TEMPLATES_DIR)

    # Import and register blueprints
    from .auth import auth_bp
    from .superadmin import superadmin_bp
    from .schooladmin import schooladmin_bp
    from .instructor import instructor_bp
    from .attendance import attendance_bp
    from .notifications import notifications_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(superadmin_bp)
    app.register_blueprint(schooladmin_bp)
    app.register_blueprint(instructor_bp)
    app.register_blueprint(attendance_bp)
    app.register_blueprint(notifications_bp)

    @app.context_processor
    def inject_globals():
        return {
            "current_user": DummyUser(name="Alex Teacher", authenticated=True),
            "current_year": date.today().year,
            "current_date": date.today().isoformat(),
        }

    @app.route('/', endpoint='landing')
    def landing():
        stats = {"schools": 3, "students": 842, "classes_today": 24, "notifications": 5}
        return render_template('landing.html', stats=stats)

    return app
