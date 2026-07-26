# Dashboards Power BI crees

Ce dossier contient le nouveau rapport Power BI propre :

```text
powerbi/dashboard_healthcare_clean.pbix
```

L'ancien fichier `dashboard.pbix` a ete retire du suivi Git et remplace par ce nouveau livrable.

## Donnees utilisees

Le rapport s'appuie sur les tables chargees dans PostgreSQL et exposees a Power BI :

| Domaine | Tables principales | Utilisation |
|---|---|---|
| Patients | `public stg_patients`, `public mart_patients` | total patients, age moyen, repartition par sexe |
| Medecins | `public doctors`, `public mart_doctors` | specialites, activite, salaire, anciennete |
| Visites | `public visits`, `public mart_visits` | volume, revenus, attente, paiement |
| Traitements | `public treatments` | volume et cout des traitements |

## Pages du rapport

Le fichier `dashboard_healthcare_clean.pbix` contient 6 pages.

### 1. Vue Executive

Objectif : donner une vision rapide de la performance globale de la clinique.

KPI affiches :

- total visites ;
- total patients ;
- chiffre d'affaires total ;
- attente moyenne.

Graphiques :

- revenus par specialite ;
- repartition paye / non paye.

### 2. Activite Medicale

Objectif : suivre le volume des consultations et les delais d'attente.

KPI affiches :

- total visites ;
- prix moyen par visite ;
- attente moyenne.

Graphiques :

- visites par motif ;
- attente moyenne par motif ;
- visites par medecin.

### 3. Revenus Paiements

Objectif : analyser les revenus et les comportements de paiement.

KPI affiches :

- chiffre d'affaires total ;
- prix moyen ;
- nombre de statuts de paiement.

Graphiques :

- revenus par medecin ;
- revenus par motif.

### 4. Medecins Specialites

Objectif : mesurer l'activite et la structure des equipes medicales.

KPI affiches :

- total medecins ;
- salaire moyen ;
- anciennete moyenne.

Graphiques :

- medecins par specialite ;
- salaire moyen par specialite ;
- visites par specialite.

### 5. Traitements

Objectif : analyser les actes, leurs volumes et leurs couts.

KPI affiches :

- total traitements ;
- cout total traitements ;
- cout moyen traitement.

Graphiques :

- cout par type de traitement ;
- nombre de traitements par type.

### 6. Patients

Objectif : analyser la demographie des patients.

KPI affiches :

- total patients ;
- age moyen ;
- groupes par sexe.

Graphiques :

- patients par sexe ;
- age moyen par sexe.

## KPI principaux du fichier Power BI

- Total visites
- Total patients
- Total medecins
- Chiffre d'affaires total
- Prix moyen par visite
- Attente moyenne
- Total traitements
- Cout total traitements
- Cout moyen traitement
- Salaire moyen
- Anciennete moyenne
- Patients par sexe

## Corrections faites dans le projet

### `mart_visits.sql`

Le fichier a ete corrige. Il ne duplique plus `mart_patients` et produit maintenant une table d'activite par medecin et specialite avec :

- total visites ;
- revenu total ;
- revenu paye ;
- revenu impaye ;
- attente moyenne ;
- prix moyen par visite.

### Scripts d'ingestion

Les scripts `ingestion/load_data*.py` utilisent maintenant des chemins relatifs au projet et la variable optionnelle `DATABASE_URL`.

### `.gitignore`

Les artefacts generes dbt et logs sont ignores :

- `dbt/target/`
- `dbt/logs/`
- `logs/`
- captures Power BI temporaires.

Le fichier final `powerbi/dashboard_healthcare_clean.pbix` reste suivi par Git.

## Ameliorations possibles

- Ajouter une table calendrier `DimDate` pour les analyses mensuelles.
- Renommer les tables dans Power BI en `FactVisits`, `FactTreatments`, `DimPatients` et `DimDoctors`.
- Ajouter les mesures DAX du fichier `MESURES_DAX.md` si le rapport doit evoluer avec des calculs plus avances.
- Corriger ou enrichir `patients.csv` si l'on veut relier directement patients et visites avec des identifiants coherents.
