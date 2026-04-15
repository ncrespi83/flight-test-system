# Flight Test System – Frontend

Vue 3 frontend for the Flight Test System. This application consumes a Django REST API to display and manage flight test data.

---

## Tech Stack

- JavaScript
- Vue 3
- Vite
- Axios

---

## Features

- Fetches test plans from backend API
- Displays test plan list view
- Handles loading and error states
- Structured for future expansion (detail views, forms, workflows)

---

## Setup

```bash
cd frontend
npm install
```

### Run Development Server

```bash
npm run dev
```

Frontend runs at:
  * http://localhost:5173



### API Integration
* Connects to Django backend at:
    * http://127.0.0.1:8000/api/
* Uses Axios for HTTP requests
* Centralized API client (`src/api.js`)

---

## Next Steps
- Implement test plan detail view (nested data)
- Add create/edit forms
- Add filtering and pagination
- Improve UI/UX styling

## Notes
* CORS must be enabled in the backend for local development
* Designed as a reactive frontend consuming RESTful endpoints
