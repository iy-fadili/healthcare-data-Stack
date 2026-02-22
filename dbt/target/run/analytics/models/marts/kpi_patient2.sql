
  
    

  create  table "clinic_db"."public"."kpi_patient2__dbt_tmp"
  
  
    as
  
  (
    select
    count(distinct patient_id) as total_patients
from "clinic_db"."public"."stg_patient2"
  );
  