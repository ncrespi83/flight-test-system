# Flight Test System App

Flight plan app that utilizes Django ORM & Python on the backend, and JavaScript (Vue 3) on the frontend



## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (development)

## Features

- Relational domain models
  - Requirements
  - Test Plans
  - Test Points
  - Test Events
- Django Admin interface for data management
- REST API built with Django REST Framework
- Nested plan detail endpoint exposing related test points and events
- Workflow action for approving test plans

## Example API Endpoints

GET /api/testplans/  
GET /api/testplans/{id}/  
POST /api/testplans/  
POST /api/testplans/{id}/approve/

GET /api/testpoints/  
GET /api/testevents/  
GET /api/requirements/

## Status

Backend API complete for core domain models.

Next steps:
- Vue 3 frontend interface
- authentication
- filtering & pagination
- additional workflow rules

## Getting Started

### 1. Clone the repository

git clone https://github.com/ncrespi83/flight-test-app.git
cd flight-test-app


### 2. Create and activate a virtual environment

python -m venv venv

macOS/Linux:
source venv/bin/activate

Windows:
venv\Scripts\activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Apply database migrations

python manage.py migrate


### 5. Run the development server

python manage.py runserver


### 6. Access the application

Admin interface:
http://127.0.0.1:8000/admin/

API root:
http://127.0.0.1:8000/api/
