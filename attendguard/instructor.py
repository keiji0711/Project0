"""Instructor blueprint for AttendGuard demo.
"""
from types import SimpleNamespace
from flask import Blueprint, render_template

instructor_bp = Blueprint("instructor", __name__, url_prefix="/instructor")


@instructor_bp.route("/", endpoint="dashboard")
def dashboard():
    todays_classes = [SimpleNamespace(name="Mathematics", time="08:00 — 09:00", section="Section A"),
                      SimpleNamespace(name="History", time="09:15 — 10:15", section="Section B")]
    return render_template("instructor/dashboard.html", todays_classes=todays_classes)
