
  create view "clinic_db"."public"."stg_doctors__dbt_tmp"
    
    
  as (
    with source as (
    select * from "clinic_db"."public"."doctors"
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
  );