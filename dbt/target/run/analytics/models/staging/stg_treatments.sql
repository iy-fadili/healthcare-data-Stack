
  create view "clinic_db"."public"."stg_treatments__dbt_tmp"
    
    
  as (
    -- models/staging/stg_treatments
select
  treatment_id::int,
  visit_id::int,
  type_traitement,
  cout::int
from "clinic_db"."public"."treatments"
  );