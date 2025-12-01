import re

pages = {
    'subjects': 'Manage Subjects',
    'students': 'Manage Students', 
    'instructors': 'Manage Instructors',
    'sections': 'Manage Sections',
    'schedules': 'Manage Schedules'
}

for page_name, page_title in pages.items():
    filepath = f'templates/schooladmin/{page_name}.html'
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Add macro import after extends
    if "from 'schooladmin/_nav.html' import admin_nav" not in content:
        content = content.replace(
            "{% extends 'base.html' %}",
            "{% extends 'base.html' %}\n{% from 'schooladmin/_nav.html' import admin_nav %}"
        )
    
    # Replace the entire sidebar section with just the nav macro call
    # Match from {% block content %} through </aside>
    pattern = r'({% block content %})\s*<div class="lg:flex lg:gap-6">.*?</aside>'
    replacement = r'\1\n  <div class="min-h-screen bg-slate-50">\n    {{ admin_nav(\'' + page_name + r'\') }}\n\n    <!-- Main Content -->\n    <div class="max-w-7xl mx-auto px-6 pb-12">'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Fix closing divs
    content = content.replace('    </div>\n  </div>\n{% endblock %}', '    </div>\n  </div>\n{% endblock %}')
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f'Updated {page_name}.html')

print('All templates updated!')
