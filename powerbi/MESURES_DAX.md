# Mesures DAX recommandees

Ces mesures sont recommandees pour faire evoluer le rapport Power BI.

Le fichier actuel `dashboard_healthcare_clean.pbix` utilise directement les tables chargees dans le modele. Pour un modele plus propre, il est recommande de renommer les tables ainsi dans Power BI :

| Nom recommande | Source actuelle |
|---|---|
| `FactVisits` | `public visits` ou `public mart_visits` |
| `FactTreatments` | `public treatments` |
| `DimPatients` | `public stg_patients` |
| `DimDoctors` | `public doctors` ou `public mart_doctors` |
| `DimDate` | table calendrier a creer |

## Mesures principales

```DAX
Total visites =
COUNTROWS(FactVisits)
```

```DAX
Patients distincts =
DISTINCTCOUNT(DimPatients[patient_id])
```

```DAX
Total medecins =
DISTINCTCOUNT(DimDoctors[doctor_id])
```

```DAX
Total traitements =
COUNTROWS(FactTreatments)
```

```DAX
Chiffre affaires total =
SUM(FactVisits[prix])
```

```DAX
Prix moyen visite =
AVERAGE(FactVisits[prix])
```

```DAX
Attente moyenne min =
AVERAGE(FactVisits[duree_attente_min])
```

```DAX
Attente maximale min =
MAX(FactVisits[duree_attente_min])
```

## Paiements

```DAX
Visites payees =
CALCULATE(
    [Total visites],
    FactVisits[paye] = TRUE()
)
```

```DAX
Visites impayees =
CALCULATE(
    [Total visites],
    FactVisits[paye] = FALSE()
)
```

```DAX
Taux de paiement =
DIVIDE([Visites payees], [Total visites])
```

```DAX
Chiffre affaires encaisse =
CALCULATE(
    SUM(FactVisits[prix]),
    FactVisits[paye] = TRUE()
)
```

```DAX
Montant impaye =
[Chiffre affaires total] - [Chiffre affaires encaisse]
```

```DAX
Panier moyen paye =
DIVIDE([Chiffre affaires encaisse], [Visites payees])
```

## Activite medicale

```DAX
Visites par patient =
DIVIDE([Total visites], [Patients distincts])
```

```DAX
Part urgences =
DIVIDE(
    CALCULATE([Total visites], FactVisits[motif] = "Urgence"),
    [Total visites]
)
```

## Traitements

```DAX
Cout total traitements =
SUM(FactTreatments[cout])
```

```DAX
Cout moyen traitement =
AVERAGE(FactTreatments[cout])
```

```DAX
Traitements par visite =
DIVIDE([Total traitements], [Total visites])
```

## Medecins

```DAX
Salaire moyen =
AVERAGE(DimDoctors[salaire])
```

Si la table `mart_doctors` est utilisee avec les noms anglais :

```DAX
Salaire moyen =
AVERAGE(DimDoctors[salary])
```

```DAX
Anciennete moyenne =
AVERAGE(DimDoctors[anciennete])
```

Si la table `mart_doctors` est utilisee avec les noms anglais :

```DAX
Anciennete moyenne =
AVERAGE(DimDoctors[seniority_years])
```

```DAX
Masse salariale =
SUM(DimDoctors[salaire])
```

```DAX
Productivite revenu salaire =
DIVIDE([Chiffre affaires encaisse], [Masse salariale])
```

## Patients

```DAX
Age moyen =
AVERAGE(DimPatients[age])
```

```DAX
Patients femmes =
CALCULATE(
    [Patients distincts],
    DimPatients[sexe] = "F"
)
```

```DAX
Patients hommes =
CALCULATE(
    [Patients distincts],
    DimPatients[sexe] = "M"
)
```

## Intelligence temporelle

Ces mesures necessitent une table calendrier `DimDate` reliee a `FactVisits[date_visite]`.

```DAX
CA mois precedent =
CALCULATE(
    [Chiffre affaires encaisse],
    DATEADD(DimDate[Date], -1, MONTH)
)
```

```DAX
Variation CA mensuelle =
DIVIDE(
    [Chiffre affaires encaisse] - [CA mois precedent],
    [CA mois precedent]
)
```

```DAX
Visites mois precedent =
CALCULATE(
    [Total visites],
    DATEADD(DimDate[Date], -1, MONTH)
)
```

```DAX
Variation visites mensuelle =
DIVIDE(
    [Total visites] - [Visites mois precedent],
    [Visites mois precedent]
)
```

## Formats recommandes

- Pourcentage : `Taux de paiement`, `Part urgences`, `Variation CA mensuelle`, `Variation visites mensuelle`.
- Devise : chiffre d'affaires, montant impaye, panier moyen, couts, salaires.
- Nombre entier : visites, patients, medecins, traitements.
- Une decimale : attentes, anciennete, age moyen et ratios.
