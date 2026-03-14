# Flight Test Management Backend

Django backend for managing flight test requirements, test plans, test points, and test events.

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (dev)

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