"""Instructor blueprint for AttendGuard demo.
"""
from types import SimpleNamespace
from flask import Blueprint, render_template

instructor_bp = Blueprint("instructor", __name__, url_prefix="/instructor")


@instructor_bp.route("/", endpoint="dashboard")
def dashboard():
    """Instructor dashboard with stats and today's schedule"""
    stats = {
        'todays_classes': 5,
        'total_students': 128,
        'attendance_rate': '92',
        'weekly_classes': 18
    }
    
    todays_classes = [
        dict(subject="Mathematics", section="Grade 10-A", time="08:00 - 09:00", students=32, room="201", status="completed"),
        dict(subject="Mathematics", section="Grade 10-B", time="09:15 - 10:15", students=28, room="201", status="ongoing"),
        dict(subject="Science", section="Grade 11-A", time="11:00 - 12:00", students=30, room="305", status="upcoming"),
        dict(subject="Mathematics", section="Grade 11-B", time="13:00 - 14:00", students=26, room="201", status="upcoming"),
        dict(subject="English", section="Grade 10-C", time="14:30 - 15:30", students=31, room="108", status="upcoming"),
    ]
    
    return render_template("instructor/dashboard.html", stats=stats, todays_classes=todays_classes, active_page='dashboard')


@instructor_bp.route("/classes", endpoint="classes")
def classes():
    """View all assigned classes"""
    classes_list = [
        dict(subject="Mathematics", section="Grade 10-A", grade="Grade 10", students=32, schedule="MWF 08:00-09:00", room="201", attendance_rate=94),
        dict(subject="Mathematics", section="Grade 10-B", grade="Grade 10", students=28, schedule="MWF 09:15-10:15", room="201", attendance_rate=91),
        dict(subject="Science", section="Grade 11-A", grade="Grade 11", students=30, schedule="TTh 11:00-12:00", room="305", attendance_rate=89),
        dict(subject="Mathematics", section="Grade 11-B", grade="Grade 11", students=26, schedule="MWF 13:00-14:00", room="201", attendance_rate=95),
        dict(subject="English", section="Grade 10-C", grade="Grade 10", students=31, schedule="TTh 14:30-15:30", room="108", attendance_rate=92),
        dict(subject="English", section="Grade 11-C", grade="Grade 11", students=29, schedule="MWF 15:45-16:45", room="108", attendance_rate=88),
    ]
    
    total_students = sum(c['students'] for c in classes_list)
    subjects_count = len(set(c['subject'] for c in classes_list))
    sections_count = len(classes_list)
    
    return render_template("instructor/classes.html", 
                         classes=classes_list, 
                         total_students=total_students,
                         subjects_count=subjects_count,
                         sections_count=sections_count,
                         active_page='classes')


@instructor_bp.route("/schedule", endpoint="schedule")
def schedule():
    """Weekly schedule view"""
    # Mock schedule data
    schedule_data = {
        'monday': {
            '08:00 - 09:00': dict(subject="Mathematics", section="Grade 10-A", room="201"),
            '09:00 - 10:00': dict(subject="Mathematics", section="Grade 10-B", room="201"),
            '13:00 - 14:00': dict(subject="Mathematics", section="Grade 11-B", room="201"),
            '15:00 - 16:00': dict(subject="English", section="Grade 11-C", room="108"),
        },
        'tuesday': {
            '11:00 - 12:00': dict(subject="Science", section="Grade 11-A", room="305"),
            '14:00 - 15:00': dict(subject="English", section="Grade 10-C", room="108"),
        },
        'wednesday': {
            '08:00 - 09:00': dict(subject="Mathematics", section="Grade 10-A", room="201"),
            '09:00 - 10:00': dict(subject="Mathematics", section="Grade 10-B", room="201"),
            '13:00 - 14:00': dict(subject="Mathematics", section="Grade 11-B", room="201"),
            '15:00 - 16:00': dict(subject="English", section="Grade 11-C", room="108"),
        },
        'thursday': {
            '11:00 - 12:00': dict(subject="Science", section="Grade 11-A", room="305"),
            '14:00 - 15:00': dict(subject="English", section="Grade 10-C", room="108"),
        },
        'friday': {
            '08:00 - 09:00': dict(subject="Mathematics", section="Grade 10-A", room="201"),
            '09:00 - 10:00': dict(subject="Mathematics", section="Grade 10-B", room="201"),
            '13:00 - 14:00': dict(subject="Mathematics", section="Grade 11-B", room="201"),
            '15:00 - 16:00': dict(subject="English", section="Grade 11-C", room="108"),
        },
    }
    
    return render_template("instructor/schedule.html", 
                         schedule=schedule_data,
                         weekly_total=18,
                         teaching_hours=24,
                         sections=8,
                         next_class="Tomorrow 8:00 AM",
                         active_page='schedule')


@instructor_bp.route("/attendance", endpoint="attendance")
def attendance():
    """Attendance records view"""
    records = [
        dict(date="Dec 9, 2025", subject="Mathematics", section="Grade 10-A", total=32, present=30, absent=2, rate=94),
        dict(date="Dec 9, 2025", subject="Mathematics", section="Grade 10-B", total=28, present=26, absent=2, rate=93),
        dict(date="Dec 8, 2025", subject="Science", section="Grade 11-A", total=30, present=27, absent=3, rate=90),
        dict(date="Dec 8, 2025", subject="English", section="Grade 10-C", total=31, present=29, absent=2, rate=94),
        dict(date="Dec 6, 2025", subject="Mathematics", section="Grade 10-A", total=32, present=31, absent=1, rate=97),
        dict(date="Dec 6, 2025", subject="Mathematics", section="Grade 11-B", total=26, present=24, absent=2, rate=92),
    ]
    
    return render_template("instructor/attendance.html", records=records, active_page='attendance')


@instructor_bp.route("/reports", endpoint="reports")
def reports():
    """Comprehensive reports and analytics"""
    # Overall Statistics
    overall_stats = {
        'total_classes': 6,
        'total_students': 176,
        'avg_attendance_rate': 92.3,
        'total_sessions': 48,
        'present_total': 4156,
        'absent_total': 312,
        'late_total': 89
    }
    
    # Class Performance Data
    class_performance = [
        dict(subject="Mathematics", section="Grade 10-A", students=32, sessions=16, attendance_rate=94.5, 
             present=483, absent=29, late=12, trend="up"),
        dict(subject="Mathematics", section="Grade 10-B", students=28, sessions=16, attendance_rate=91.2, 
             present=408, absent=40, late=8, trend="stable"),
        dict(subject="Science", section="Grade 11-A", students=30, sessions=8, attendance_rate=89.7, 
             present=215, absent=25, late=10, trend="down"),
        dict(subject="Mathematics", section="Grade 11-B", students=26, sessions=16, attendance_rate=95.1, 
             present=395, absent=21, late=6, trend="up"),
        dict(subject="English", section="Grade 10-C", students=31, sections=8, attendance_rate=92.6, 
             present=230, absent=18, late=4, trend="up"),
        dict(subject="English", section="Grade 11-C", students=29, sessions=8, attendance_rate=88.3, 
             present=205, absent=27, late=9, trend="stable"),
    ]
    
    # Monthly Attendance Trend
    monthly_trend = [
        dict(month="August", rate=91.2, present=1820, absent=165, late=28),
        dict(month="September", rate=92.8, present=1892, absent=142, late=24),
        dict(month="October", rate=93.5, present=1945, absent=128, late=18),
        dict(month="November", rate=92.1, present=1876, absent=158, late=35),
        dict(month="December", rate=94.2, present=756, absent=42, late=12),
    ]
    
    # Student Attendance Patterns
    top_performers = [
        dict(name="Alice Johnson", student_id="2025001", class_section="Grade 10-A", rate=100, present=48, absent=0),
        dict(name="Bob Smith", student_id="2025012", class_section="Grade 11-B", rate=100, present=48, absent=0),
        dict(name="Carol White", student_id="2025023", class_section="Grade 10-C", rate=98.5, present=47, absent=1),
        dict(name="David Brown", student_id="2025034", class_section="Grade 11-A", rate=97.9, present=47, absent=1),
        dict(name="Eva Green", student_id="2025045", class_section="Grade 10-B", rate=97.9, present=47, absent=1),
    ]
    
    at_risk_students = [
        dict(name="Frank Miller", student_id="2025078", class_section="Grade 11-A", rate=75.0, present=36, absent=12, consecutive_absent=3),
        dict(name="Grace Lee", student_id="2025089", class_section="Grade 10-B", rate=77.1, present=37, absent=11, consecutive_absent=2),
        dict(name="Henry Wilson", student_id="2025091", class_section="Grade 11-C", rate=79.2, present=38, absent=10, consecutive_absent=2),
        dict(name="Iris Taylor", student_id="2025102", class_section="Grade 10-A", rate=81.3, present=39, absent=9, consecutive_absent=1),
    ]
    
    # Day of Week Analysis
    day_analysis = [
        dict(day="Monday", avg_rate=93.5, classes=4, avg_present=118, avg_absent=8),
        dict(day="Tuesday", avg_rate=91.2, classes=2, avg_present=55, avg_absent=5),
        dict(day="Wednesday", avg_rate=94.1, classes=4, avg_present=119, avg_absent=7),
        dict(day="Thursday", avg_rate=90.8, classes=2, avg_present=54, avg_absent=6),
        dict(day="Friday", avg_rate=89.5, classes=4, avg_present=115, avg_absent=11),
    ]
    
    return render_template("instructor/reports.html",
                         overall_stats=overall_stats,
                         class_performance=class_performance,
                         monthly_trend=monthly_trend,
                         top_performers=top_performers,
                         at_risk_students=at_risk_students,
                         day_analysis=day_analysis,
                         active_page='reports')
