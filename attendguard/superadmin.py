"""Superadmin blueprint for AttendGuard demo.
"""
from types import SimpleNamespace
from flask import Blueprint, render_template

superadmin_bp = Blueprint("superadmin", __name__, url_prefix="/superadmin")


@superadmin_bp.route("/", endpoint="dashboard")
def dashboard():
    schools = [SimpleNamespace(name="Central High"), SimpleNamespace(name="Westside Academy"), SimpleNamespace(name="North Prep")]
    return render_template("superadmin/dashboard.html", schools=schools)
