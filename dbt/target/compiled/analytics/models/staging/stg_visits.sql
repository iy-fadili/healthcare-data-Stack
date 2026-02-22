-- models/staging/stg_visits.sql

select
  visit_id::int,
  patient_id::int,
  doctor_id::int,
  date_visite::date,
  motif,
  duree_attente_min::int,
  prix::int,
  paye::boolean
from "clinic_db"."public"."visits"