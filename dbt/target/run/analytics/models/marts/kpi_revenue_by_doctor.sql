
  
    

  create  table "clinic_db"."public"."kpi_revenue_by_doctor__dbt_tmp"
  
  
    as
  
  (
    -- models/marts/kpi_revenue_by_doctor.sql

select
  d.doctor_id,
  d.specialty,
  sum(v.prix) as total_revenue
from "clinic_db"."public"."stg_visits" v
join "clinic_db"."public"."stg_doctors" d
  on v.doctor_id = d.doctor_id
where v.paye = true
group by 1,2
  );
  