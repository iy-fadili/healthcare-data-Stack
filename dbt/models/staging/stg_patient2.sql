select
    patient_id,
    upper(prenom) as prenom,
    upper(nom) as nom,
    sexe,
    date_naissance

from {{ source('raw', 'patients') }}
    where patient_id is not null