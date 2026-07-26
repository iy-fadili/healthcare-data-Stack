-- models/marts/mart_visits.sql

with visits as (
    select * from {{ ref('stg_visits') }}
),

doctors as (
    select * from {{ ref('stg_doctors') }}
),

final as (
    select
        d.doctor_id,
        d.last_name,
        d.first_name,
        d.specialty,
        count(v.visit_id) as total_visits,
        sum(v.prix) as total_revenue,
        sum(case when v.paye then v.prix else 0 end) as paid_revenue,
        sum(case when not v.paye then v.prix else 0 end) as unpaid_revenue,
        round(avg(v.duree_attente_min), 2) as avg_wait_minutes,
        round(avg(v.prix), 2) as avg_visit_price
    from visits v
    join doctors d
        on v.doctor_id = d.doctor_id
    group by
        d.doctor_id,
        d.last_name,
        d.first_name,
        d.specialty
)

select * from final
