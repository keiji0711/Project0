#!/usr/bin/env python3
"""
Update all schooladmin templates to use sidebar navigation
"""

import re
from pathlib import Path

# Define the templates directory
templates_dir = Path("templates/schooladmin")

# Template files to update
template_files = [
    "dashboard.html",
    "subjects.html",
    "students.html",
    "instructors.html",
    "sections.html",
    "schedules.html"
]

for template_file in template_files:
    file_path = templates_dir / template_file
    
    if not file_path.exists():
        print(f"❌ Skipping {template_file} - file not found")
        continue
    
    print(f"📝 Processing {template_file}...")
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace admin_nav with admin_sidebar
    content = re.sub(
        r'{% from \'schooladmin/_nav\.html\' import admin_nav %}',
        r"{% from 'schooladmin/_nav.html' import admin_sidebar %}",
        content
    )
    
    # Replace the navigation call and wrapper
    content = re.sub(
        r'<div class="min-h-screen bg-slate-50">\s*\{\{ admin_nav\(\'(\w+)\'\) \}\}',
        r"<div class=\"min-h-screen bg-slate-50\">\n    {{ admin_sidebar('\1') }}",
        content
    )
    
    # Change main content to have margin for sidebar (ml-64 = 256px sidebar width)
    content = re.sub(
        r'<div class="max-w-7xl mx-auto px-6 pb-12">',
        r'<div class="ml-64 p-6">',
        content
    )
    
    # Write back
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Updated {template_file}")

print("\n🎉 All templates updated with sidebar navigation!")
