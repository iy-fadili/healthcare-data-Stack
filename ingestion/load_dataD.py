import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://data_user:password123@localhost:5432/clinic_db"
)

df = pd.read_csv(r"C:\Users\FD\data-stack\data\doctors.csv", encoding='latin-1')
df.to_sql("doctors", engine, if_exists="replace", index=False)

print("✅ Données chargées dans clinic_db.public.doctors")
