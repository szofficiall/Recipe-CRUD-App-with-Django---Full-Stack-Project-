# 🍽️ RecipeBook - Django Recipe Management System

[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A fully responsive web application built with Django that allows users to **Create, Read, Update, and Delete** recipes with a beautiful modern UI. Perfect for food lovers who want to organize their favorite recipes in one place.

---

## 📑 **Table of Contents**

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation Steps](#-installation-steps)
- [Project Structure](#-project-structure)
- [Database Setup](#-database-setup)
- [Usage Guide](#-usage-guide)
- [API Endpoints](#-api-endpoints)
- [Screenshots](#-screenshots)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

---

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

## 🛠️ **Tech Stack**

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| Django | 5.0+ | Web Framework |
| SQLite3 | - | Development Database |
| Django ORM | - | Object-Relational Mapping |
| Django Auth | - | User Management |

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| HTML5 | - | Markup Language |
| CSS3 | - | Styling |
| Bootstrap | 5.3 | CSS Framework |
| JavaScript | ES6 | Interactive Elements |
| SweetAlert2 | 11+ | Beautiful Alerts |
| Font Awesome | 6.5 | Icons |
| Google Fonts | - | Typography (Poppins) |

### Tools
| Tool | Purpose |
|------|---------|
| Git | Version Control |
| Pip | Package Manager |
| Virtual Environment | Isolated Environment |
| VS Code | Code Editor |

---

## 🚀 **Installation Steps**

### Step 1: **Prerequisites**

Make sure you have the following installed:

```bash
# Check Python version
python --version
# Should be Python 3.10 or higher

# Check pip version
pip --version
# Should be pip 23.0 or higher

### Step 2: Clone the Repository
# Clone the project
git clone https://github.com/szofficiall/recipebook.git

### Step 3: Create Virtual Environment
# Navigate to project directory
cd recipebook

### Step 4: Install Dependencies
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate

# For Linux (alternative)
virtualenv venv
source venv/bin/activate

Django==5.0.6
Pillow==10.3.0
python-dotenv==1.0.1
django-crispy-forms==2.1
crispy-bootstrap5==0.7

### Install all dependencies:
pip install -r requirements.txt  
