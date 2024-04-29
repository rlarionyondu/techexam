# Digital API Developer - Technical Examination
This is a simple API project that will provide endpoints to create, update, list and retrieve records of Provinces and Regions in the Philippines

## Installation

Unzip Project file: 
```
django.zip`
```
Go to **techexam** directory
```
cd techexam
```
Create a virtual environment: 
```
python -m venv venv
```
Activate the virtual environment: 
```
source venv/bin/activate
```
Install dependencies: 
```
pip install -r requirements.txt
```
Goto project directory
```
cd techexam
```
Run migrations: 
```
python manage.py migrate`
```
Start the development server: 
```
python manage.py runserver`
```
---
## Access API using Postman

### Generate auth token
POST http://127.0.0.1:8000/api/v1/token/auth/

##### Body
``` form-data```
|Key                     |Value
|-------------------|-------------------|
|username:          |onie
|password:          |pass
---
### Add Region
POST http://127.0.0.1:8000/api/v1/region/
##### Headers
|Key                     |Value
|-------------------|-------------------|
|Authorization      |(generated token)
##### Body
```raw: JSON```
```
{
"name": "XII"
}
```
---
### List Regions
GET http://127.0.0.1:8000/api/v1/region?page=1&per_page=10&name=III
##### Headers
|Key                     |Value
|-------------------|-------------------|
|Authorization      |(generated token)
---
### Update a Region
PATCH http://127.0.0.1:8000/api/v1/region/4/
##### Headers
|Key                     |Value
|-------------------|-------------------|
|Authorization      |(generated token)
##### Body
```raw: JSON```
```
{
"name": "IV - update"
}
```
---
### Add Province
POST http://127.0.0.1:8000/api/v1/province/
##### Headers
|Key                     |Value
|-------------------|-------------------|
|Authorization      |(generated token)
##### Body
```raw: JSON```
```
{
"name": "Abra"
}
```
---
### List Provinces
GET http://127.0.0.1:8000/api/v1/province?page=1&per_page=10&name=Aurora
##### Headers
|Key                     |Value
|-------------------|-------------------|
|Authorization      |(generated token)

