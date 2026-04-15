# Flight Test System - Backend

Django backend for managing flight test requirements, test plans, test points, and test events.

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (development)

---

## Features

- Relational domain models:
  - Requirements
  - Test Plans
  - Test Points
  - Test Events
- Django Admin interface for data management
- REST API built with Django REST Framework
- Nested serializers for test plan detail views
- Workflow action for approving test plans

---

## API Endpoints

### Test Plans
- GET /api/testplans/  
- GET /api/testplans/{id}/  
- POST /api/testplans/  
- POST /api/testplans/{id}/approve/

### Other Resources
- GET /api/testpoints/  
- GET /api/testevents/  
- GET /api/requirements/

---

## Setup

```bash
cd backend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

### Run the Server

```bash
python manage.py migrate
python manage.py runserver
```

### Access
* API Root: http://127.0.0.1:8000/api/
* Admin Panel: http://127.0.0.1:8000/admin/

---

## Notes
* Uses Django REST Framework for API development
* Status fields include both code values and display labels
* Designed to support frontend integration via REST API