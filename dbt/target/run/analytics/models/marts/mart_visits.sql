
  
    

  create  table "clinic_db"."public"."mart_visits__dbt_tmp"
  
  
    as
  
  (
    -- models/marts/patients_by_gender.sql

select
    sexe,
    count(patient_id) as total_patients,
    round(avg(age), 1) as age_moyen -- round pour avoir un chiffre après la virgule
from "clinic_db"."public"."stg_patients"
group by 1
  );
  