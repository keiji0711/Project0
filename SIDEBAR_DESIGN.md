# AttendGuard - Sidebar Navigation Design

## Overview
The School Admin section now features a **professional sidebar navigation** inspired by modern POS systems.

## Design Features

### 🎨 Visual Design
- **Dark gradient sidebar**: Slate-800 to Slate-900 gradient background
- **256px width** (w-64): Fixed sidebar on the left
- **Icons + Labels**: Each menu item has an icon and descriptive text
- **Active state**: Blue-600 background with shadow for current page
- **Hover effects**: Subtle slate-700 background on hover

### 📐 Layout Structure
```
┌─────────────────────────────────────────────────┐
│ Top Navbar (AttendGuard logo, user menu)       │
├─────────┬───────────────────────────────────────┤
│ Sidebar │ Main Content Area                     │
│ 256px   │                                       │
│         │ • Dashboard stats                     │
│ • Home  │ • Tables                              │
│ • Subj. │ • Forms                               │
│ • Stud. │ • etc...                              │
│ • Inst. │                                       │
│ • Sect. │                                       │
│ • Sched │                                       │
│         │                                       │
│         │                                       │
└─────────┴───────────────────────────────────────┘
```

### 🧭 Navigation Items
1. **Dashboard** - Overview and statistics
2. **Subjects** - Subject management
3. **Students** - Student enrollment and records
4. **Instructors** - Staff management
5. **Sections** - Class sections
6. **Schedules** - Timetable management

### 🎯 Technical Implementation

#### Sidebar Component (`templates/schooladmin/_nav.html`)
```jinja2
{% macro admin_sidebar(active_page) %}
<aside class="fixed left-0 top-16 h-[calc(100vh-4rem)] w-64 bg-gradient-to-b from-slate-800 to-slate-900">
  <nav class="p-4 space-y-1">
    <!-- Menu items with icons -->
  </nav>
</aside>
{% endmacro %}
```

#### Content Area Adjustment
All pages use `ml-64` (margin-left: 256px) to make room for the fixed sidebar:
```html
<div class="ml-64 p-6">
  <!-- Page content -->
</div>
```

### 🎨 Color Scheme
- **Sidebar Background**: `from-slate-800 to-slate-900` (dark gradient)
- **Text**: White
- **Active Item**: `bg-blue-600` with shadow
- **Hover**: `bg-slate-700`
- **Icons**: White, 20px (w-5 h-5)

### ✅ Advantages Over Horizontal Tabs
1. **More vertical space** - No horizontal tab bar taking up screen space
2. **Always visible** - Navigation doesn't scroll away
3. **Professional look** - Similar to enterprise dashboards and POS systems
4. **Better icon visibility** - Icons clearly visible next to labels
5. **Scalable** - Easy to add more menu items without crowding

## Usage
All school admin templates automatically include the sidebar via:
```jinja2
{% from 'schooladmin/_nav.html' import admin_sidebar %}
{{ admin_sidebar('dashboard') }}  <!-- Pass current page name -->
```

## Responsive Behavior
- **Desktop**: Full sidebar visible (256px)
- **Tablet/Mobile**: Consider implementing a collapsible sidebar in future

## Files Updated
- `templates/schooladmin/_nav.html` - Sidebar macro
- `templates/schooladmin/dashboard.html`
- `templates/schooladmin/subjects.html`
- `templates/schooladmin/students.html`
- `templates/schooladmin/instructors.html`
- `templates/schooladmin/sections.html`
- `templates/schooladmin/schedules.html`

---
**Design inspired by**: Point POS System and modern admin dashboards
**Last updated**: November 30, 2025
