# ☕ Brew & Bite --- Restaurant & Café Website

A modern, responsive restaurant and café website built with **Django
5.2.17**. Brew & Bite provides a complete digital experience for
customers to explore the menu, discover the café, view the gallery and
reviews, manage their account, and make table reservations.

> **Live Demo:** > `https://restuarant-django.onrender.com/`

------------------------------------------------------------------------

## ✨ Features

### 🏠 Home

-   Restaurant hero section and brand introduction
-   Featured menu items
-   Customer rating/review highlights
-   Responsive call-to-action buttons

### 🍽️ Menu

-   Food and drink categories
-   Menu cards with images, names, prices, descriptions and categories
-   Category filtering
-   Responsive card grid
-   Consistent card heights and controlled descriptions

### 📅 Reservations

-   Table reservation functionality
-   Reservation form and confirmation workflow
-   Dedicated `reservation` Django app
-   Designed to integrate with authenticated customer accounts

### 👤 Accounts

-   User registration
-   Login/logout
-   User profile
-   Password change
-   Password reset

### 🖼️ Gallery

-   Restaurant and food gallery
-   Category filters
-   Responsive image layout

### ⭐ Reviews

-   Review statistics
-   Average rating display
-   Featured reviews

### 📖 About

-   Restaurant story
-   Brand philosophy
-   Responsive content sections

### 📞 Contact

-   Contact information
-   Responsive contact section

### 📱 Responsive UI

Optimized for desktop, laptop, tablet and mobile screens, including
responsive navigation, hero sections, menu cards, buttons and spacing.

------------------------------------------------------------------------

## 🛠️ Tech Stack

  Area                Technology
  ------------------- --------------------------
  Backend             Python 3.11
  Framework           Django 5.2.17
  Database            SQLite
  Frontend            HTML5, CSS3, JavaScript
  Templates           Django Template Language
  Static Files        WhiteNoise
  Production Server   Gunicorn
  Version Control     Git + GitHub
  Deployment          Render

------------------------------------------------------------------------

## 🏗️ Project Structure

``` text
Restruant_Project/
│
├── accounts/                 # Authentication and user accounts
├── core/                     # Main website functionality
├── menu/                     # Menu and categories
├── reservation/              # Table reservations
│
├── Restruant_Project/        # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/                   # CSS, JavaScript and images
├── templates/                # Shared Django templates
├── media/                    # Uploaded media
│
├── build.sh                  # Render build script
├── manage.py
├── requirements.txt
├── .python-version
├── .gitignore
└── README.md
```

------------------------------------------------------------------------

## 🔐 Authentication Flow

The project uses Django's authentication framework:

``` text
Visitor
   ↓
Register / Login
   ↓
Authenticated Account
   ↓
Account / Reservation Features
```

Public pages such as Home, Menu, About, Gallery, Reviews and Contact can
be browsed without an account. Account-sensitive functionality is
handled through Django authentication.

------------------------------------------------------------------------

## 📅 Reservation Flow

``` text
Customer
   ↓
Login / Register
   ↓
Book a Table
   ↓
Enter Reservation Details
   ↓
Submit Reservation
   ↓
Confirmation
```

Reservations are implemented as a separate Django application so the
feature can be extended independently.

------------------------------------------------------------------------

## 🎨 Design

Brew & Bite uses a warm café-inspired visual identity featuring:

-   Neutral backgrounds
-   Dark brown typography
-   Warm accent colors
-   Editorial-style headings
-   Food photography
-   Card-based layouts
-   Responsive navigation
-   Mobile hamburger menu
-   Consistent spacing and typography

------------------------------------------------------------------------

## ⚙️ Local Installation

### 1. Clone the repository

``` bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create a virtual environment

Windows:

``` powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

``` env
SECRET_KEY=your-secret-key
DEBUG=True
```

Never commit `.env` or production secrets to GitHub.

### 5. Run migrations

``` bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an admin account

``` bash
python manage.py createsuperuser
```

### 7. Collect static files

``` bash
python manage.py collectstatic
```

### 8. Start the development server

``` bash
python manage.py runserver
```

Open:

``` text
http://127.0.0.1:8000/
```

------------------------------------------------------------------------

## 🗄️ Database

The current project uses SQLite:

``` python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

SQLite is convenient for development and this portfolio project.

### Deployment note

The application is deployed on Render's free web-service tier. Render
free web services use an ephemeral filesystem, so local SQLite should
**not** be treated as persistent production storage. For a production
restaurant application with important reservation/customer data, use a
persistent database service.

------------------------------------------------------------------------

## 🚀 Render Deployment

The repository is configured for Render.

### Build command

``` bash
./build.sh
```

### Start command

``` bash
python -m gunicorn Restruant_Project.wsgi:application
```

### `build.sh`

``` bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

Production-sensitive settings such as `SECRET_KEY` and `DEBUG` are read
from environment variables.

------------------------------------------------------------------------

## 🔒 Security

Production configuration includes:

-   Environment-based `SECRET_KEY`
-   `DEBUG=False`
-   Secure session cookies
-   Secure CSRF cookies
-   HTTPS redirect
-   HSTS configuration
-   `X-Frame-Options`
-   Content-type sniffing protection
-   Render host configuration

Secrets should never be committed to the repository.

------------------------------------------------------------------------

## 📦 Django Apps

  App             Purpose
  --------------- -----------------------------------------------------
  `core`          Main website pages and common functionality
  `menu`          Menu items and categories
  `reservation`   Table reservation functionality
  `accounts`      Registration, authentication and account management

------------------------------------------------------------------------

## 🧪 Useful Commands

Check the project:

``` bash
python manage.py check
```

Create migrations:

``` bash
python manage.py makemigrations
```

Apply migrations:

``` bash
python manage.py migrate
```

Run server:

``` bash
python manage.py runserver
```

Create admin user:

``` bash
python manage.py createsuperuser
```

Collect static files:

``` bash
python manage.py collectstatic
```

------------------------------------------------------------------------

## 🌿 Git Workflow

``` bash
git status
git add .
git commit -m "Describe your changes"
git push origin main
```

The connected Render service can automatically deploy new commits pushed
to the configured GitHub branch.

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Persistent production database
-   Email reservation confirmations
-   SMS notifications
-   Reservation availability calendar
-   Admin reservation dashboard
-   Online food ordering
-   Shopping cart
-   Payment integration
-   Coupons and discounts
-   Advanced search
-   Customer review submission
-   Restaurant analytics dashboard
-   REST API
-   Automated tests and CI/CD
-   Docker support

------------------------------------------------------------------------

## 🎯 What This Project Demonstrates

This project demonstrates practical experience with:

-   Django project and app architecture
-   Django ORM
-   Models and migrations
-   URL routing
-   Views and forms
-   Django templates and template inheritance
-   Authentication
-   CRUD operations
-   Static and media files
-   Responsive frontend development
-   Git/GitHub
-   Environment variables
-   Gunicorn
-   WhiteNoise
-   Render deployment

------------------------------------------------------------------------

## 👨‍💻 Author

**Harsh**

BCom Background \| Python & Django Developer \| AI/ML Enthusiast

Brew & Bite was developed as a practical full-stack Django project
demonstrating backend development, authentication, database interaction,
responsive UI development and deployment.

------------------------------------------------------------------------

## 📄 License

This project is primarily intended as a learning and portfolio project.

If you reuse or modify it, please provide appropriate attribution to the
original author.

------------------------------------------------------------------------

## ⭐ Support

If you find the project useful, consider giving the repository a ⭐ on
GitHub.

------------------------------------------------------------------------

### Built with ☕ and Django

**Brew & Bite --- Where Great Food Meets Great Moments.**
