# AttendGuard

**Modern school attendance monitoring system** built with Flask and Tailwind CSS.

## 🚀 Quick Start

### Install Dependencies

```bash
# Create and activate virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### Run the Application

```bash
python3 app.py
```

The app will be available at: **http://127.0.0.1:5000**

## 📋 Features

✅ **Automated Attendance** - Quick attendance recording with instructor portals  
✅ **Parent Notifications** - Instant alerts for absences and tardiness  
✅ **Instructor Portal** - Manage rosters, attendance, and schedules  
✅ **Admin Control Panel** - Complete school management system  
✅ **Responsive Design** - Mobile-friendly interface with Tailwind CSS  
✅ **Role-Based Dashboards** - Separate interfaces for superadmin, school admin, and instructors

## 🎨 Design System

### Color Palette
- **Primary**: `#2563EB` (blue-600)
- **Secondary**: `#1E40AF` (blue-800)
- **Accent**: `#FACC15` (yellow-400)
- **Background**: `#F8FAFC` (slate-50)
- **Text**: `#1E293B` (slate-800)

### UI Components
- Modern gradient buttons with hover effects
- Card-based layouts with shadow elevations
- Responsive tables with hover states
- Professional sidebar navigation
- Avatar badges and status indicators

## 🗂️ Project Structure

```
AttendGuard/
├── attendguard/               # Main application package
│   ├── __init__.py           # App factory and blueprint registration
│   ├── auth.py               # Authentication routes
│   ├── superadmin.py         # Superadmin dashboard
│   ├── schooladmin.py        # School admin management
│   ├── instructor.py         # Instructor portal
│   ├── attendance.py         # Attendance recording
│   └── notifications.py      # Notifications system
├── templates/                 # Jinja2 templates
│   ├── base.html             # Base layout with navbar
│   ├── landing.html          # Home/landing page
│   ├── login.html            # Login form
│   ├── superadmin/
│   │   └── dashboard.html    # Superadmin schools management
│   ├── schooladmin/
│   │   └── dashboard.html    # School admin portal
│   ├── instructor/
│   │   └── dashboard.html    # Instructor classes view
│   ├── attendance/
│   │   └── record.html       # Attendance recording interface
│   └── notifications/
│       └── dashboard.html    # Notifications preview
├── app.py                     # Application entry point
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🌐 Routes & Pages

### Public Routes
| Route | Description |
|-------|-------------|
| `/` | Landing page with features and stats |
| `/auth/login` | Login page (visual only in demo) |

### Dashboard Routes
| Route | Role | Description |
|-------|------|-------------|
| `/superadmin/` | Super Admin | Schools management table |
| `/schooladmin/` | School Admin | Manage subjects, students, instructors, sections, schedules |
| `/instructor/` | Instructor | Today's classes with attendance buttons |
| `/attendance/record` | Instructor | Record attendance for a class |
| `/notifications/` | All | View notifications |

## 👤 Accessing Dashboards

**Current Setup**: No authentication is required (demo mode). You can access any dashboard directly:

- **Superadmin**: http://127.0.0.1:5000/superadmin/
- **School Admin**: http://127.0.0.1:5000/schooladmin/
- **Instructor**: http://127.0.0.1:5000/instructor/
- **Attendance**: http://127.0.0.1:5000/attendance/record
- **Notifications**: http://127.0.0.1:5000/notifications/

### Adding Authentication (Optional)

To add development login:
1. Uncomment the `dev_auth.py` blueprint (if present)
2. Visit `/dev/login?role=schooladmin` to set your role
3. Protected routes will check `session['role']`

## 🎯 Template Context Variables

Each template expects the following placeholder data:

### Landing Page (`landing.html`)
```python
stats = {
    'schools': 3,
    'students': 842,
    'classes_today': 24,
    'notifications': 5
}
```

### Superadmin Dashboard (`superadmin/dashboard.html`)
```python
schools = [
    SimpleNamespace(name="Central High"),
    SimpleNamespace(name="Westside Academy"),
    ...
]
```

### Instructor Dashboard (`instructor/dashboard.html`)
```python
todays_classes = [
    SimpleNamespace(name="Mathematics", time="08:00 — 09:00", section="Section A"),
    ...
]
```

### Attendance Record (`attendance/record.html`)
```python
students = [SimpleNamespace(name="Student 1", student_id="S1001"), ...]
class_info = SimpleNamespace(subject="Math", section="A", instructor="Alan Smith")
date = "2025-11-30"
```

### Notifications (`notifications/preview.html`)
```python
notifications = [
    SimpleNamespace(title="Notice", message="...", timestamp="...", read=False),
    ...
]
```

## 🛠️ Technology Stack

- **Backend**: Flask 3.1+
- **Templates**: Jinja2
- **Styling**: Tailwind CSS (CDN)
- **Icons**: Heroicons (inline SVG)
- **Python**: 3.8+

## 📱 Responsive Breakpoints

- **Mobile**: < 640px
- **Tablet**: 640px - 1024px
- **Desktop**: > 1024px

All dashboards and tables are fully responsive with mobile-optimized navigation.

## 🔧 Development Notes

### App Factory Pattern
The app uses Flask's application factory pattern (`create_app()`) for modularity:
- Blueprints are registered in `attendguard/__init__.py`
- Each feature has its own blueprint module
- Templates folder is configured to use the project-level `templates/` directory

### Placeholder Data
All routes currently return hardcoded placeholder data. To connect to a database:
1. Add SQLAlchemy models
2. Replace `SimpleNamespace` objects with ORM queries
3. Add form handling and validation

### No JavaScript
Templates are purely HTML + Tailwind CSS. Interactive features (attendance buttons, toggles) are visual-only and would require:
- HTMX or Alpine.js for interactivity (recommended)
- Or custom JavaScript for form submissions

## 🚧 Future Enhancements

- [ ] Add real authentication (Flask-Login)
- [ ] Database integration (SQLAlchemy + PostgreSQL/MySQL)
- [ ] Parent portal
- [ ] Email/SMS notifications integration
- [ ] Attendance reports and analytics
- [ ] CSV import/export
- [ ] API endpoints for mobile app

## 📄 License

This is a demo/prototype project. Adapt as needed for your school's requirements.

## 🤝 Contributing

This is a starter template. Feel free to:
- Add more features
- Improve the design
- Connect to a real database
- Add unit tests

---

**Built with ❤️ for modern schools**
# Project0
