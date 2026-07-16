# 🍽️ RecipeBook - Django Recipe Management System

[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A fully responsive web application built with Django that allows users to **Create, Read, Update, and Delete** recipes with a beautiful modern UI. Perfect for food lovers who want to organize their favorite recipes in one place.


## ✨ **Features**

### 🔐 **Authentication System**
- ✅ User Registration (Sign Up)
- ✅ User Login
- ✅ User Logout
- ✅ Password Protection
- ✅ Session Management
- ✅ Welcome Messages

### 📝 **CRUD Operations**
- ✅ **Create** - Add new recipes with name, description, and image
- ✅ **Read** - View all recipes in a beautiful table
- ✅ **Update** - Edit existing recipes
- ✅ **Delete** - Remove recipes with confirmation

### 🔍 **Search Functionality**
- ✅ Search recipes by name
- ✅ Search recipes by description
- ✅ Real-time search results
- ✅ Clear search option

### 🎨 **Modern UI/UX**
- ✅ Glass-morphism design
- ✅ Animated gradient backgrounds
- ✅ Responsive layout (Mobile/Tablet/Desktop)
- ✅ SweetAlert2 confirmations
- ✅ Toast notifications
- ✅ Font Awesome icons
- ✅ Google Fonts (Poppins)

### 📱 **Responsive Design**
- ✅ Mobile-first approach
- ✅ Side-by-side layout on desktop
- ✅ Stack layout on mobile
- ✅ Touch-friendly buttons
- ✅ Smooth animations

---

## 🏗️ **Project Structure**
recipe_project/
│
├── manage.py                           # Django management script
│
├── recipe_project/                     # Main project folder
│   ├── __init__.py
│   ├── settings.py                     # Project settings
│   ├── urls.py                         # Main URLs
│   ├── wsgi.py                         # WSGI configuration
│   └── asgi.py                         # ASGI configuration
│
├── recipes/                            # Main app folder
│   ├── __init__.py
│   ├── admin.py                        # Admin panel configuration
│   ├── apps.py                         # App configuration
│   ├── models.py                       # Database models (Recipe)
│   ├── views.py                        # Views (logic)
│   ├── urls.py                         # App URLs
│   ├── forms.py                        # Django forms
│   │
│   ├── templates/                      # HTML templates
│   │   └── recipes/                    # Template folder
│   │       ├── base.html               # Base template (navbar, messages)
│   │       ├── home.html               # Home/Splash page
│   │       ├── login.html              # Login page
│   │       ├── signup.html             # Signup page
│   │       ├── recipe_list.html        # Dashboard (Add + View Recipes)
│   │       ├── recipe_form.html        # Add/Update recipe form
│   │       ├── update_recipe.html      # Update recipe form
│   │       └── splash.html             # Splash screen (optional)
│   │
│   ├── migrations/                     # Database migrations
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── ...
│   │
│   └── static/                         # App-specific static files
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── script.js
│
├── media/                              # User uploaded files
│   └── recipe_images/                  # Recipe images folder
│       ├── recipe1.jpg
│       ├── recipe2.png
│       └── ...
│
├── static/                             # Global static files
│   ├── css/
│   │   └── global.css
│   └── js/
│       └── global.js
│
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Git ignore file
├── README.md                           # Project documentation
└── LICENSE                             # License file
---

## 🛠️ **Tech Stack**

### Backend
- **Django** 5.0 - Python Web Framework
- **SQLite3** - Development Database
- **Django ORM** - Object-Relational Mapping
- **Django Authentication** - User Management

### Frontend
- **HTML5** - Markup Language
- **CSS3** - Styling with Glass-morphism
- **Bootstrap** 5.3 - CSS Framework
- **JavaScript** - Interactive Elements
- **SweetAlert2** - Beautiful Alerts
- **Font Awesome** 6.5 - Icons
- **Google Fonts** (Poppins) - Typography

### Tools
- **Git** - Version Control
- **Pip** - Package Manager
- **Virtual Environment** - Isolated Python Environment

---

## 🚀 **Installation & Setup**

### Prerequisites
- Python 3.10 or higher
- Pip (Python package manager)
- Virtual Environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/recipebook.git
cd recipebook

