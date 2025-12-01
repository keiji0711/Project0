#!/usr/bin/env python3
"""
Update all schooladmin templates to use top tab navigation instead of sidebar
"""
import re
from pathlib import Path

templates_dir = Path("templates/schooladmin")
files = [
    "dashboard.html",
    "subjects.html",
    "students.html",
    "instructors.html",
    "sections.html",
    "schedules.html",
]

for name in files:
    path = templates_dir / name
    if not path.exists():
        print(f"❌ {name} missing, skipping")
        continue
    html = path.read_text()

    # Import macro: admin_sidebar -> admin_nav
    html = re.sub(
        r"{%\s*from\s*'schooladmin/_nav.html'\s*import\s*admin_sidebar\s*%}",
        "{% from 'schooladmin/_nav.html' import admin_nav %}",
        html,
    )

    # Macro call: {{ admin_sidebar('page') }} -> {{ admin_nav('page') }}
    html = re.sub(r"\{\{\s*admin_sidebar\('([\w-]+)'\)\s*\}\}", r"{{ admin_nav('\1') }}", html)

    # Content wrapper: remove ml-64 and use max width container
    html = re.sub(r'class="ml-64\s+([^\"]*)"', r'class="max-w-7xl mx-auto \1"', html)

    # If no ml-64 existed, ensure main container has max width
    html = re.sub(
        r"<div class=\"([^\"]*?)p-6\"">",
        r"<div class=\"max-w-7xl mx-auto \1p-6\"">",
        html,
    )

    path.write_text(html)
    print(f"✅ Updated {name}")

print("\n🎉 Switched schooladmin templates to top tab navigation.")
