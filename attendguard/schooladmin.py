"""School admin blueprint for AttendGuard demo.
"""
from flask import Blueprint, render_template

schooladmin_bp = Blueprint("schooladmin", __name__, url_prefix="/schooladmin")


@schooladmin_bp.route("/", endpoint="dashboard")
def dashboard():
    """Main dashboard with overview stats and quick actions"""
    stats = {
        'total_students': 342,
        'total_instructors': 28,
        'total_subjects': 12,
        'total_sections': 8,
        'classes_today': 24,
        'attendance_rate': 94.5
    }
    return render_template("schooladmin/dashboard.html", stats=stats)


@schooladmin_bp.route("/subjects", endpoint="subjects")
def subjects():
    """Manage subjects page"""
    # Placeholder data
    return render_template("schooladmin/subjects.html")


@schooladmin_bp.route("/students", endpoint="students")
def students():
    """Manage students page"""
    return render_template("schooladmin/students.html")


@schooladmin_bp.route("/students/<int:student_id>", endpoint="student_view")
def student_view(student_id: int):
    """Student profile view page (mock)."""
    return render_template("schooladmin/student_view.html", student_id=student_id, active_page="students")


@schooladmin_bp.route("/instructors", endpoint="instructors")
def instructors():
    """Manage instructors page"""
    return render_template("schooladmin/instructors.html")


@schooladmin_bp.route("/sections", endpoint="sections")
def sections():
    """Manage sections page"""
    return render_template("schooladmin/sections.html")


@schooladmin_bp.route("/schedules", endpoint="schedules")
def schedules():
    """View and manage schedules"""
    # Mock data: full lists of instructors and subjects (school-wide)
    instructors = [
        {"id": 1, "name": "Dr. Maria Johnson", "department": "Mathematics"},
        {"id": 2, "name": "Robert Chen", "department": "Physics"},
        {"id": 3, "name": "Sarah Anderson", "department": "Algebra"},
        {"id": 4, "name": "Prof. David Lee", "department": "Statistics"},
        {"id": 5, "name": "Dr. Grace Miller", "department": "Calculus"},
    ]
    subjects = [
        {"code": "MATH101", "name": "Fundamentals of Mathematics", "tag": "Core"},
        {"code": "ALG201", "name": "Intermediate Algebra", "tag": "Core"},
        {"code": "CALC301", "name": "Differential Calculus", "tag": "Advanced"},
        {"code": "STAT210", "name": "Introductory Statistics", "tag": "Core"},
        {"code": "PHYS110", "name": "General Physics I", "tag": "Lab"},
        {"code": "GEOM150", "name": "Euclidean Geometry", "tag": "Elective"},
    ]
    return render_template("schooladmin/schedules.html", instructors=instructors, subjects=subjects, active_page="schedules")
