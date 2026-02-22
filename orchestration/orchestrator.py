from prefect import flow, task
import subprocess

@task(retries=2, retry_delay_seconds=10)
def ingest():
    # Lance ton script Python local qui alimente le Postgres Docker
    # Note : Vérifie que load_data.py pointe bien vers localhost:5432
    print("🚀 Début de l'ingestion...")
    subprocess.run(["python", r"C:\Users\FD\data-stack\ingestion\load_data.py"], check=True)

@task(retries=1, retry_delay_seconds=5)
def transform():
    print("🏗️ Début des transformations dbt...")
    subprocess.run(
        ["dbt", "run", "--profiles-dir", r"C:\Users\FD\.dbt"],
        cwd=r"C:\Users\FD\data-stack\analytics",
        check=True
    )


@flow(name="Pipeline_Clinique_DB")
def etl_pipeline():
    ingest()
    transform()

if __name__ == "__main__":
    etl_pipeline()