"""Auth blueprint (visual-only) for AttendGuard demo.
"""
from flask import Blueprint, render_template, redirect, url_for

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


class DummyForm:
    def hidden_tag(self):
        return ""


@auth_bp.route("/login", methods=["GET"], endpoint="login")
def login():
    form = DummyForm()
    return render_template("login.html", form=form)


@auth_bp.route("/logout", endpoint="logout")
def logout():
    return redirect(url_for("landing"))


@auth_bp.route("/forgot", endpoint="forgot_password")
def forgot_password():
    return redirect(url_for("auth.login"))
