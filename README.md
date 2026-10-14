# CRUD

Simple FastAPI CRUD application.

## Overview
My first FastAPI CRUD app demonstrating basic create, read, update, and delete operations on a Todo resource.
Data is stored in-memory and resets when the server restarts.

## Endpoints

| Method | Path              | Description              |
|--------|-------------------|--------------------------|
| POST   | `/todos`          | Create a new todo        |
| GET    | `/todos`          | List all todos          |
| GET    | `/todos/{id}`     | Get a single todo       |
| PUT    | `/todos/{id}`     | Update a todo           |
| DELETE | `/todos/{id}`     | Delete a todo           |

Interactive API docs are available at `/docs` (Swagger UI) and `/redoc`.

## Run

```bash
uv sync
uv run uvicorn test:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

**Note:** The FastAPI application is defined in `test.py`. `main.py` is a simple placeholder script.

## Example

```bash
curl -X POST http://127.0.0.1:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "todo": "Learn FastAPI", "completed": false}'
```

Updated: 2026-10-14
