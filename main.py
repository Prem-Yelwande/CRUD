"""Placeholder entry point for the CRUD project.

The actual FastAPI application lives in test.py.
This file is intentionally minimal so the real app can be started independently.

Run the server with:
    uv run uvicorn test:app --reload

If you prefer a different port:
    uv run uvicorn test:app --reload --port 8001

If you need to bind to a specific host (e.g. for network access):
    uv run uvicorn test:app --reload --host 0.0.0.0 --port 8000

Docs: http://127.0.0.1:8000/docs
OpenAPI schema: http://127.0.0.1:8000/openapi.json

Note: Data is stored in-memory and will be lost on server restart.
For persistence, consider adding a database in a future iteration.
"""

from fastapi import FastAPI
from typing import Optional


def main(port: Optional[int] = None) -> None:
    """Print helpful usage instructions for the CRUD project.

    Args:
        port: Optional custom port number to suggest in the instructions.
    """
    print("CRUD project — usage helper")
    print("The FastAPI app is defined in test.py (not this file).")
    if port:
        print(f"Start the server with: uv run uvicorn test:app --reload --port {port}")
    else:
        print("Start the server with: uv run uvicorn test:app --reload")
    print("To allow external access, add: --host 0.0.0.0")
    print("Interactive docs: http://127.0.0.1:8000/docs")
    print("OpenAPI JSON:   http://127.0.0.1:8000/openapi.json")
    print("Tip: Use --port <number> if the default port is busy.")
    print("")
    print("Data model reminder:")
    print("  - id (int), todo (str), completed (bool)")
    print("")
    print("Note: Todos are stored in-memory; all data resets when the server restarts.")
    print("Consider integrating a database (e.g., SQLite via SQLAlchemy) for production use.")
    print("For more details, see the README.md.")


if __name__ == "__main__":
    main()
