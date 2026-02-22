-- models/staging/stg_treatments
select
  treatment_id::int,
  visit_id::int,
  type_traitement,
  cout::int
from "clinic_db"."public"."treatments"