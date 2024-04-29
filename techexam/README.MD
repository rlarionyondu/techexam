# Digital API Developer - Technical Examination

This is a simple API project that will provide endpoints to create, update, list and retrieve records of Provinces and Regions in the Philippines

## Installation

1. Unzip Project file: `django.zip`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Start the development server: `python manage.py runserver`


## Access API using Postman

### Generate Auth Token
POST http://127.0.0.1:8000/api/v1/token/auth/
Body:
    username: onie
    password: pass

### Add Region
POST http://127.0.0.1:8000/api/v1/region/
Headers:
    Key: Authorization
    Value: generated token
    Body (raw, JSON):
        {
            "name": "XII"
        }

### List Regions
GET http://127.0.0.1:8000/api/v1/region?page=1&per_page=10&name=III
Headers:
    Key: Authorization
    Value: generated token

### Update a Region
PATCH http://127.0.0.1:8000/api/v1/region/4/
Headers:
    Key: Authorization
    Value: generated token
Body (raw, JSON):
    {
    "name": "IV - update"
    }

### Add Province
POST http://127.0.0.1:8000/api/v1/province/
Headers:
    Key: Authorization
    Value: generated token
Body (raw, JSON):
    {
    "name": "Cotabato",
    "region": 12
    }

### List Provinces
GET http://127.0.0.1:8000/api/v1/province/?page=1&per_page=10&name=Aurora
Headers:
    Key: Authorization
    Value: generated token