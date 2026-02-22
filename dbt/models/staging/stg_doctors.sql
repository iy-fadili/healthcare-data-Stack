
with source as (
    select * from {{ source('raw', 'doctors') }}
),

renamed as (
    select
        doctor_id,
        nom as last_name,
        prenom as first_name,
        specialite as specialty,
        anciennete as seniority_years,
        salaire as salary
    from source
)

select * from renamed