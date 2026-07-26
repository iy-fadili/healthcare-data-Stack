import os
from pathlib import Path
import subprocess
import sys
import time

from sqlalchemy import create_engine, text


ROOT_DIR = Path(__file__).resolve().parents[1]
DBT_DIR = ROOT_DIR / "dbt"
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://data_user:password123@localhost:5432/clinic_db",
)
INGESTION_SCRIPTS = [
    ROOT_DIR / "ingestion" / "load_data.py",
    ROOT_DIR / "ingestion" / "load_dataD.py",
    ROOT_DIR / "ingestion" / "load_dataV.py",
    ROOT_DIR / "ingestion" / "load_dataT.py",
]


def run_command(command, cwd=ROOT_DIR):
    print()
    print(f"Commande: {' '.join(str(part) for part in command)}")
    subprocess.run(command, cwd=cwd, check=True)


def wait_for_database(max_attempts=20):
    engine = create_engine(DATABASE_URL)
    for attempt in range(1, max_attempts + 1):
        try:
            with engine.connect() as connection:
                connection.execute(text("select 1"))
            return
        except Exception:
            print(f"Attente PostgreSQL... tentative {attempt}/{max_attempts}")
            time.sleep(2)
    raise RuntimeError("PostgreSQL ne repond pas.")


def start_postgres():
    print()
    print("[1/5] Demarrage de PostgreSQL avec Docker Compose")
    run_command(["docker", "compose", "up", "-d"], cwd=ROOT_DIR)
    wait_for_database()


def reset_public_schema():
    print()
    print("[2/5] Reinitialisation du schema public")
    engine = create_engine(DATABASE_URL)
    with engine.begin() as connection:
        connection.execute(text("drop schema if exists public cascade"))
        connection.execute(text("create schema public"))
        connection.execute(text("grant all on schema public to data_user"))
        connection.execute(text("grant all on schema public to public"))


def ingest_sources():
    print()
    print("[3/5] Chargement des fichiers CSV dans PostgreSQL")
    for script in INGESTION_SCRIPTS:
        run_command([sys.executable, str(script)], cwd=ROOT_DIR)


def run_dbt_models():
    print()
    print("[4/5] Execution des transformations dbt")
    run_command(["dbt", "run"], cwd=DBT_DIR)


def run_dbt_tests():
    print()
    print("[5/5] Execution des tests dbt")
    run_command(["dbt", "test"], cwd=DBT_DIR)


def etl_pipeline():
    start_postgres()
    reset_public_schema()
    ingest_sources()
    run_dbt_models()
    run_dbt_tests()
    print()
    print("Pipeline terminee avec succes.")


if __name__ == "__main__":
    etl_pipeline()
