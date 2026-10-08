import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")


def connect_db():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL is missing")

    return psycopg.connect(
        database_url,
        connect_timeout=10,
        sslmode="require",
        prepare_threshold=None,
    )

def create_tester():
    import hashlib
    import secrets

    code = secrets.token_urlsafe(32)
    code_hash = hashlib.sha256(code.encode("utf-8")).hexdigest()

    with connect_db() as connection:
        connection.execute(
            "INSERT INTO beta_testers (code_hash) VALUES (%s)",
            (code_hash,),
        )

    return code

def reserve_usage(code):
    import hashlib

    if not code or len(code) > 100:
        return "invalid_code"

    code_hash = hashlib.sha256(
        code.strip().encode("utf-8")
    ).hexdigest()

    with connect_db() as connection:
        # Keep simultaneous requests from exceeding the overall limit.
        connection.execute("SELECT pg_advisory_xact_lock(746201)")

        tester = connection.execute(
            """
            SELECT id FROM beta_testers
            WHERE code_hash = %s AND active = TRUE
            """,
            (code_hash,),
        ).fetchone()

        if tester is None:
            return "invalid_code"

        today = connection.execute(
            """
            SELECT (clock_timestamp()
                    AT TIME ZONE 'Europe/Lisbon')::date
            """
        ).fetchone()[0]

        already_used = connection.execute(
            """
            SELECT 1 FROM beta_daily_usage
            WHERE tester_id = %s AND usage_date = %s
            """,
            (tester[0], today),
        ).fetchone()

        if already_used:
            return "daily_limit"

        total = connection.execute(
            """
            SELECT COUNT(*) FROM beta_daily_usage
            WHERE usage_date = %s
            """,
            (today,),
        ).fetchone()[0]

        if total >= 20:
            return "beta_limit"

        connection.execute(
            """
            INSERT INTO beta_daily_usage (tester_id, usage_date)
            VALUES (%s, %s)
            """,
            (tester[0], today),
        )

    return "allowed"

if __name__ == "__main__":
    try:
        with connect_db() as connection:
            result = connection.execute("SELECT 1").fetchone()
        print("Database connection OK" if result == (1,) else "Check failed")
    except Exception as error:
        print(f"Connection failed: {type(error).__name__}")