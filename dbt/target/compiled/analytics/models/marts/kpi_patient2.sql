select
    count(distinct patient_id) as total_patients
from "clinic_db"."public"."stg_patient2"