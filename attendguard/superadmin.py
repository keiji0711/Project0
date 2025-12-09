"""Superadmin blueprint for AttendGuard demo.
"""
from types import SimpleNamespace
from flask import Blueprint, render_template

superadmin_bp = Blueprint("superadmin", __name__, url_prefix="/superadmin")


@superadmin_bp.route("/", endpoint="dashboard")
def dashboard():
    schools = [
        SimpleNamespace(name="Central High"),
        SimpleNamespace(name="Westside Academy"),
        SimpleNamespace(name="North Prep"),
    ]
    totals = dict(
        total_schools=len(schools),
        total_users=1243,
        active_subscriptions=3,
        active_schools=len(schools),
    )
    return render_template("superadmin/dashboard.html", schools=schools, **totals)


@superadmin_bp.route("/schools", endpoint="schools")
def schools():
    schools = [
        SimpleNamespace(name="Central High"),
        SimpleNamespace(name="Westside Academy"),
        SimpleNamespace(name="North Prep"),
    ]
    return render_template("superadmin/dashboard.html", schools=schools)


@superadmin_bp.route("/subscriptions", endpoint="subscriptions")
def subscriptions():
    # Mock subscriptions data
    subscriptions = [
        dict(school="Central High", plan="Pro", status="Active", seats=100, used_seats=84, renewal="2026-01-15", price_per_month=299.00),
        dict(school="Westside Academy", plan="Enterprise", status="Trialing", seats=500, used_seats=312, renewal="2026-02-01", price_per_month=1299.00),
        dict(school="North Prep", plan="Free", status="Active", seats=25, used_seats=21, renewal="—", price_per_month=0.00),
        dict(school="Lakeside College", plan="Pro", status="Paused", seats=150, used_seats=0, renewal="2026-03-10", price_per_month=399.00),
        dict(school="Eastview School", plan="Pro", status="Active", seats=80, used_seats=65, renewal="2026-01-28", price_per_month=249.00),
        dict(school="Riverbend Institute", plan="Enterprise", status="Canceled", seats=1000, used_seats=0, renewal="—", price_per_month=0.00),
    ]
    return render_template("superadmin/subscriptions.html", subscriptions=subscriptions)


@superadmin_bp.route("/users", endpoint="users")
def users():
    # Mock users data
    users = [
        dict(name="Alice Johnson", email="alice@attendguard.io", role="Super Admin", status="Active", school="—", joined="2025-04-02", initials="AJ"),
        dict(name="Brian Lee", email="brian@centralhigh.edu", role="School Admin", status="Active", school="Central High", joined="2025-06-11", initials="BL"),
        dict(name="Cynthia Ramos", email="cramos@westside.ac", role="School Admin", status="Invited", school="Westside Academy", joined="2025-09-21", initials="CR"),
        dict(name="Diego Santos", email="dsantos@northprep.edu", role="Instructor", status="Active", school="North Prep", joined="2025-03-14", initials="DS"),
        dict(name="Emily Wong", email="ewong@lakeside.edu", role="Instructor", status="Suspended", school="Lakeside College", joined="2025-01-08", initials="EW"),
        dict(name="Faisal Khan", email="faisal@eastview.edu", role="Instructor", status="Active", school="Eastview School", joined="2025-08-30", initials="FK"),
        dict(name="Grace Park", email="grace@riverbend.edu", role="School Admin", status="Active", school="Riverbend Institute", joined="2025-05-26", initials="GP"),
        dict(name="Henry Zhao", email="henry@westside.ac", role="Instructor", status="Invited", school="Westside Academy", joined="2025-10-03", initials="HZ"),
    ]
    return render_template("superadmin/users.html", users=users)


@superadmin_bp.route("/settings", endpoint="settings")
def settings():
    settings = dict(
        org_name="AttendGuard",
        timezone="Asia/Manila",
        locale="en-US",
        date_format="YYYY-MM-DD",
        primary_color="#2563EB",
        logo_url="",
        theme="system",
        require_2fa=True,
        password_policy="Strong",
        session_timeout=30,
        ip_allowlist="",
        email_notifications=True,
        weekly_summary=False,
        alert_severity="High Only",
        billing_email="billing@attendguard.io",
        invoice_frequency="Monthly",
        auto_renew=True,
        webhook_url="",
        api_key="sk_live_************************",
    )
    return render_template("superadmin/settings.html", settings=settings)
