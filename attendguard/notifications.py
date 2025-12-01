"""Notifications blueprint for AttendGuard demo.
"""
from types import SimpleNamespace
from flask import Blueprint, render_template
from datetime import datetime

notifications_bp = Blueprint("notifications", __name__, url_prefix="/notifications")


@notifications_bp.route("/", endpoint="preview")
def preview():
    notifications = [SimpleNamespace(title=f"Notice {i}", message="Short message preview.", timestamp=datetime.now().strftime("%Y-%m-%d %H:%M"), read=(i%2==0)) for i in range(1,6)]
    return render_template("notifications/preview.html", notifications=notifications)
