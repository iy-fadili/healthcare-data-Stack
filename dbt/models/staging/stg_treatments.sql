-- models/staging/stg_treatments
select
  treatment_id::int,
  visit_id::int,
  type_traitement,
  cout::int
from {{ source('raw', 'treatments') }}