# Flight Test System

Full-stack flight test management application built with **Django + Django REST Framework** on the backend and **Vue 3** on the frontend.

This system models and manages the lifecycle of flight testing operations, including requirements, test plans, test points, and scheduled test events.

---

## Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- SQLite (development)

### Frontend
- JavaScript
- Vue 3
- Vite
- Axios

---

## Features

### Backend
- Relational domain models:
  - Requirements
  - Test Plans
  - Test Points
  - Test Events
- Django Admin interface for data management
- REST API built with Django REST Framework
- Nested plan detail endpoint (includes related test points and events)
- Workflow action for approving test plans

### Frontend
- Vue 3 application with API integration
- Test plan list view (connected to backend)
- Dynamic data fetching using Axios

---

## Project Structure

```
flight-test-system/
├── backend/ # Django + DRF backend
└── frontend/ # Vue 3 frontend (Vite)
```

---

## Status

- Backend API complete for core domain models
- Frontend integration in progress
- Test plan list view implemented

### Next steps
- Implement test plan detail view (nested data)
- Add authentication
- Add filtering and pagination
- Expand workflow validation rules

---

## Quick Start

### 1. Clone the repository
```bash
git clone git@github.com:ncrespi83/flight-test-system.git
cd flight-test-system
```

### 2. Start the Backend
```bash
cd backend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Backend runs at:
 * API: http://127.0.0.1:8000/api/
 * Admin: http://127.0.0.1:8000/admin/

### 3. Start the Frontend
In a second terminal:
```bash
cd frontend

npm install
npm run dev
```

Frontend runs at:
  * http://localhost:5173

## Documentation
- [Backend Documentation](./backend/README.md)
- [Frontend Documentation](./frontend/README.md)

## Notes
* CORS is configured to allow communication between the Vue frontend and Django backend during development.
* API responses include both status codes and human-readable labels (ex. `status` and `status_display`) for frontend flexibility

## Author
Nathan Crespi