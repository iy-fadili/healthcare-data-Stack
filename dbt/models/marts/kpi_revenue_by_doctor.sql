-- models/marts/kpi_revenue_by_doctor.sql

select
  d.doctor_id,
  d.specialty,
  sum(v.prix) as total_revenue
from {{ ref('stg_visits') }} v
join {{ ref('stg_doctors') }} d
  on v.doctor_id = d.doctor_id
where v.paye = true
group by 1,2