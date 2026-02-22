select
    count(distinct patient_id) as total_patients
from {{ ref('stg_patient2') }}
