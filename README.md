# Employee Management REST API

A backend REST API built using **Django REST Framework (DRF)** for managing employees in a company.  
This project was developed as part of a technical hiring assignment and demonstrates clean RESTful design, authentication, validation, pagination, filtering, testing, and API documentation.



## 🚀 Features

- JWT-based Authentication using SimpleJWT
- Full CRUD operations for Employees
- Email uniqueness and data validation
- Filtering by department and role
- Pagination (10 records per page)
- Proper HTTP status codes and error handling
- Swagger/OpenAPI documentation
- Unit tests for core endpoints


## 🛠️ Tech Stack

- **Backend:** Python, Django
- **API Framework:** Django REST Framework
- **Authentication:** JWT (SimpleJWT)
- **Database:** SQLite (for local development)
- **API Docs:** drf-spectacular (Swagger UI)
- **Testing:** Django Test Framework

---

## 📂 Project Structure
```bash
employee-management-api/
│
├── employee_api/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
├── employees/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ ├── tests.py
│ └── migrations/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```


## 📑 API Documentation (Swagger)

Swagger UI is available at:
https://hobatconnect.onrender.com/docs/
The Swagger interface supports JWT authentication and can be used for testing all secured endpoints.


## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/employee-management-api
cd employee-management-api
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run Development Server
```bash
python manage.py runserver
```
