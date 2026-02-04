# 🛒 E-Commerce Web Application (Django)

A full-stack e-commerce web application built with **Django**, focusing on clean architecture, real-world business logic, and scalable backend development.

---

## 🚀 Features

- User authentication (Register, Login, Logout)
- Google authentication using **Django Allauth**
- Product listing with category-wise filtering
- Advanced product search, price range & rating filter
- Product rating & review system (purchase verified)
- Shopping cart (add, update, remove items)
- Secure checkout & order management
- **SSLCommerz payment gateway integration**
- Order status tracking & order history
- Email confirmation after successful payment
- User profile management & password change
- Admin panel for managing products, categories & orders
- Stock management after successful order

---

## 🧰 Tech Stack

**Backend**
- Python
- Django (MVT Architecture)
- Django ORM

**Frontend**
- HTML
- CSS
- Bootstrap
- JavaScript

**Database**
- SQLite (Development)

**Authentication**
- Django Authentication
- Django Allauth (Google OAuth)

**Payment Gateway**
- SSLCommerz

**Other Tools**
- Git & GitHub
- Django Messages Framework
- Email (SMTP)

---

## 🧠 Core Concepts Applied

- Object-Oriented Programming (OOP)
- MVC / MVT architecture
- REST-style request handling
- Relational database modeling
- Secure authentication & authorization
- Session & cart management
- Payment gateway integration
- Error handling & validation

---

## 📂 Project Modules

- Products & Categories
- Cart & Cart Items
- Orders & Order Items
- Ratings & Reviews
- User Profile Management
- Payment & Email Services

---

## ⚙️ Installation & Setup

1. Clone the repository  
```bash
   git clone <your-github-repo-link>
```

2. Create & activate virtual environment
```bash
   python -m venv env
   source env/bin/activate
```

3. Install dependencies
```bash 
   pip install -r requirements.txt
```

4. Configure .env file
```bash
SECRET_KEY=your_secret_key

SSLCOMMERZ_STORE_ID=...0e
SSLCOMMERZ_STORE_PASSWORD=...
SSLCOMMERZ_PAYMENT_URL=...
SSLCOMMERZ_VALIDATION_URL=...


EMAIL_BACKEND=...
EMAIL_HOST=...
EMAIL_HOST_USER=...
EMAIL_HOST_PASSWORD=...
EMAIL_PORT=...
EMAIL_USE_TLS=...
```

5. Run migrations
```bash
   python manage.py migrate
```

 6. Start development server
```bash
   python manage.py runserver
```