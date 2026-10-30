# CRUD

Simple FastAPI CRUD application.

## Overview
My first FastAPI CRUD app demonstrating basic create, read, update, and delete operations on a Todo resource.
Data is stored in-memory (a Python list) and resets when the server restarts. Ideal for learning and local demos.

**Note:** Because storage is in-memory, all data is lost on server restart. For persistent storage, consider integrating a database like SQLite or PostgreSQL in a future iteration.

## Requirements
- Python 3.10+
- [uv](https://docs.astral.sh/uv/) for dependency management (recommended)

## Data Model
Each Todo item has the following fields:
- `id` (int): Unique identifier
- `todo` (str): Description of the task
- `completed` (bool): Whether the task is done

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

**Tip:** If port 8000 is busy, use `uv run uvicorn test:app --reload --port 8001`.

**Note:** The FastAPI application is defined in `test.py`. `main.py` is a simple placeholder script that prints usage instructions.

## Example

Create a todo:
```bash
curl -X POST http://127.0.0.1:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "todo": "Learn FastAPI", "completed": false}'
```

List all todos:
```bash
curl http://127.0.0.1:8000/todos
```

Update a todo:
```bash
curl -X PUT http://127.0.0.1:8000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "todo": "Master FastAPI", "completed": true}'
```

Delete a todo:
```bash
curl -X DELETE http://127.0.0.1:8000/todos/1
```

Updated: 2026-10-30
