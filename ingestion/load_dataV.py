import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine


ROOT_DIR = Path(__file__).resolve().parents[1]
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://data_user:password123@localhost:5432/clinic_db",
)

engine = create_engine(DATABASE_URL)

csv_path = ROOT_DIR / "data" / "visits.csv"
df = pd.read_csv(csv_path, encoding="latin-1")
df.to_sql("visits", engine, if_exists="replace", index=False)

print(f"Donnees chargees dans clinic_db.public.visits: {len(df)} lignes")
