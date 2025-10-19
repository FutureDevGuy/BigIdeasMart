# 🛒 E-commerce Product API named BIGIDEASMART

A robust backend E-commerce API built with Django REST Framework (DRF) and JWT Authentication.
This project powers an online marketplace that supports user authentication, category and product management, and advanced filtering/searching.  
It’s designed as a Backend Engineering Capstone Project.

---

## Project Overview

The E-commerce Product API provides endpoints to manage products and users for an online store.  
Admins can add or update products, while users can view and search products by category, name, or price range.

---

## Features

-  **JWT Authentication** (login, register, token refresh)
-  **CRUD Operations** for Products
-  **Search and Filter** products by name, category, or price range
-  **Pagination** for large product lists
-  **Django ORM** for database management
-  **CORS support** for frontend integration
-  **Ready for Deployment** on Heroku or PythonAnywhere

---

##  Tech Stack

- **Backend Framework:** Django 5 + Django REST Framework  
- **Authentication:** Simple JWT  
- **Database:** SQLite (Development) / PostgreSQL (Production)  
- **Filtering:** django-filter  
- **Deployment:** Heroku / PythonAnywhere  
- **Other Tools:** gunicorn, whitenoise, dj-database-url, python-dotenv  

---

## ⚙️ Setup Instructions (Local Development)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/FutureDevGuy/BigIdeasMart.git
cd BigIdeasMart/ecommerce-api

2️⃣ Create and Activate a Virtual Environment
python -m venv venv
source venv/Scripts/activate  # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create a Superuser
python manage.py createsuperuser

6️⃣ Run the Server
python manage.py runserver


Server will start at:
👉 http://127.0.0.1:8000/

🔑 Authentication (JWT)
Obtain Token
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"FutureDevGuy", "password":"DevAdmin"}'

Refresh Token
curl -X POST http://127.0.0.1:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2MTQ4NTY3NywiaWF0IjoxNzYwODgwODc3LCJqdGkiOiJhOGU1MGZkMjAyOWM0Mjg1ODI4YzYxM2Q5NzIwMmUxNSIsInVzZXJfaWQiOiIxIn0.Kc3SDlTUUUk8BBH1Ksdn93jDRMOERO7t6dj9DngkSEs"}'


Use the access token in all protected requests:

Authorization: "Authorization" = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYwODg4MDc3LCJpYXQiOjE3NjA4ODA4NzcsImp0aSI6ImZkM2VkYWVlZWRkZTRhOThhMDhlMDVlYWIzY2MyYjhkIiwidXNlcl9pZCI6IjEifQ.rIxoMGgRYCWDkGtDNAlpDSXpLhxhNk-ySnpgMOF_V1c"

📦 API Endpoints
🔹 Product Endpoints
Method	Endpoint	Description
GET	/api/products/	List all products
GET	/api/products/<id>/	Retrieve product details
POST	/api/products/	Create a new product (authenticated)
PUT	/api/products/<id>/	Update product (authenticated)
DELETE	/api/products/<id>/	Delete product (authenticated)
🔹 Search & Filter
Filter	Example
Search by name	/api/products/?search=HP Laptop
Filter by category	/api/products/?category=electronics
Price range	/api/products/?price__gte=100&price__lte=1000
🧠 Example Usage (cURL)
Get All Products
curl http://127.0.0.1:8000/api/products/

Search Products
curl "http://127.0.0.1:8000/api/products/?search=HP Laptop"
  

🧩 Project Structure
ecommerce-api/
│
├── ecommerce_api/          # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── products/               # Product app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── users/                  # User app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── db.sqlite3              # Local database
├── manage.py
└── requirements.txt