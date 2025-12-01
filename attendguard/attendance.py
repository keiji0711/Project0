"""Attendance blueprint for AttendGuard demo.
"""
from types import SimpleNamespace
from flask import Blueprint, render_template
from datetime import date

attendance_bp = Blueprint("attendance", __name__, url_prefix="/attendance")


@attendance_bp.route("/record", endpoint="record")
def record():
    students = [SimpleNamespace(name=f"Student {i}", student_id=f"S{1000+i}") for i in range(1, 13)]
    class_info = SimpleNamespace(subject="Mathematics", section="Section A", instructor="Alan Smith")
    # 'class' is a reserved word in Python; pass it via dict-unpack so the template still
    # receives a variable named 'class'.
    return render_template("attendance/record.html", students=students, **{"class": class_info}, date=date.today().isoformat())
