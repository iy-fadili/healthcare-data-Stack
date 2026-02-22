# import pandas as pd
# from sqlalchemy import create_engine

# engine = create_engine(
#     "postgresql://data_user:password123@localhost:5432/clinic_db"
# )

# df = pd.read_csv(r"C:\Users\FD\data-stack\data\patients.csv", encoding='latin-1')
# df.to_sql("patients", engine, if_exists="replace", index=False)

# print("✅ Données chargées dans clinic_db.public.patients")


import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import json



# Connexion à PostgreSQL
# Assurez-vous que le conteneur 'postgres_data' est bien lancé et accessible sur le port 5432
engine = create_engine("postgresql://data_user:password123@localhost:5432/clinic_db")

# 1. Chargement du fichier CSV
df = pd.read_csv(r"C:\Users\FD\data-stack\data\patients.csv")

# 2. Injection de la date dans la colonne nommée 'data'
# On utilise .now().date() pour avoir uniquement AAAA-MM-JJ
df["data"] = datetime.now().date() 
# Convert the date objects to JSON-formatted strings

df['data'] = df['data'].apply(lambda x: json.dumps(x.isoformat()) if x else None)

# 3. Envoi vers PostgreSQL
# 'if_exists=append' ajoute les lignes sans supprimer les anciennes
df.to_sql("patients", engine, if_exists="append", index=False)

print(f"✅ {len(df)} patients ajoutés avec succès dans la colonne 'data'")



#------------------------------------------------------
# Pour afficher tasck and run dans interface perfect
#-------------------------------------------------------




# import pandas as pd
# from sqlalchemy import create_engine
# from datetime import datetime
# import json
# from prefect import flow, task # Importation des outils Prefect

# # --- TASKS ---

# @task(retries=2, retry_delay_seconds=10)
# def load_and_ingest_patients():
#     """Tâche d'ingestion des données CSV vers PostgreSQL"""
    
#     # Connexion à PostgreSQL
#     engine = create_engine("postgresql://data_user:password123@localhost:5432/clinic_db")

#     # 1. Chargement du fichier CSV
#     print("📖 Lecture du fichier CSV...")
#     df = pd.read_csv(r"C:\Users\FD\data-stack\data\patients.csv")

#     # 2. Préparation des données
#     print("📅 Ajout de la date d'ingestion...")
#     ingestion_date = datetime.now().date()
#     df["data"] = json.dumps(ingestion_date.isoformat())

#     # 3. Envoi vers PostgreSQL
#     print(f"🚀 Injection de {len(df)} lignes dans la table 'patients'...")
#     df.to_sql("patients", engine, if_exists="append", index=False)
    
#     return len(df)

# # --- FLOW ---

# @flow(name="Ingestion_Patients_Clinique")
# def main_flow():
#     """Le flux principal qui orchestre les tâches"""
#     nb_lignes = load_and_ingest_patients()
#     print(f"✅ Terminé : {nb_lignes} patients ajoutés.")

# # --- EXECUTION ---

# if __name__ == "__main__":
#     # On force la configuration avant de lancer le flow
#     from prefect.context import get_settings_context
#     print("🔗 Tentative de connexion au serveur sur http://127.0.0.1:4200")
    
#     main_flow()

