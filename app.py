from __future__ import annotations

import os
import sqlite3
import sys

from flask import Flask, jsonify


def create_app() -> Flask:
    """Create a minimal Flask app used for environment readiness checks."""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-only-key")

    @app.get("/")
    def index():
        return "TEAM bootstrap app is running."

    @app.get("/health")
    def health():
        # Basic sqlite check to ensure the standard library db module is usable.
        with sqlite3.connect(":memory:") as conn:
            conn.execute("SELECT 1")

        return jsonify(
            {
                "status": "ok",
                "python_version": sys.version.split()[0],
                "flask_version": Flask.__version__,
                "message": "Environment is ready for team development.",
            }
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
