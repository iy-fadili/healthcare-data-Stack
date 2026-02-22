
  
    

  create  table "clinic_db"."public"."mart_doctors__dbt_tmp"
  
  
    as
  
  (
    with doctors as (
    select * from "clinic_db"."public"."stg_doctors"
),

final as (
    select
        doctor_id,
        upper(last_name) as last_name, -- Normalisation en majuscules
        first_name,
        specialty,
        seniority_years,
        salary,
        -- Ajout d'une logique métier : calcul du bonus
        case 
            when seniority_years > 10 then salary * 0.15 
            else salary * 0.05 
        end as estimated_bonus
    from doctors
)

select * from final
  );
  