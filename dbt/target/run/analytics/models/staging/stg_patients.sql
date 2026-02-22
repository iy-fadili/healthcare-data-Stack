
  create view "clinic_db"."public"."stg_patients__dbt_tmp"
    
    
  as (
    -- models/staging/stg_patients.sql

with source_data as (
  
    select * from "clinic_db"."public"."patients"
)

select
    patient_id,
    prenom,
    nom,
    sexe,
    -- On convertit explicitement en date ici pour plus de sécurité
    date_naissance::date as date_naissance, 
    -- On ajoute ::date à la colonne pour que la fonction age() fonctionne
    extract(year from age(current_date, date_naissance::date)) as age
from source_data
  );