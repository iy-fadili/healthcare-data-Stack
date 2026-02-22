
  create view "clinic_db"."public"."stg_patient2__dbt_tmp"
    
    
  as (
    select
    patient_id,
    upper(prenom) as prenom,
    upper(nom) as nom,
    sexe,
    date_naissance

from "clinic_db"."public"."patients"
    where patient_id is not null
  );