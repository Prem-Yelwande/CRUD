"""Placeholder entry point for the CRUD project.

The actual FastAPI application lives in test.py.
This file is intentionally minimal so the real app can be started independently.

Run the server with:
    uv run uvicorn test:app --reload

If you prefer a different port:
    uv run uvicorn test:app --reload --port 8001

Docs: http://127.0.0.1:8000/docs
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
    print("Docs available at http://127.0.0.1:8000/docs once running.")
    print("Tip: Use --port <number> if the default port is busy.")
    print("For more details, see the README.md.")


if __name__ == "__main__":
    main()
