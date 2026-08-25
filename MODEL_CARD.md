# Model Card – Telco Customer Churn Prediction

## 1. Informations générales

| Élément | Description |
|---------|-------------|
| Nom du modèle | Telco Customer Churn Prediction |
| Version | 1.0.0 |
| Algorithme | Régression Logistique |
| Framework | Scikit-learn |
| Optimisation | Optuna (50 essais) |
| Calibration | Platt Scaling (`CalibratedClassifierCV`) |
| Interprétabilité | SHAP |
| Auteur | Mamadou Saidou Keita |
| Date | 2026 |

---

# 2. Objectif du modèle

Ce modèle a pour objectif de prédire si un client d'un opérateur de télécommunications est susceptible de résilier son abonnement (churn).

Il permet d'estimer la probabilité de résiliation afin d'aider l'entreprise à identifier les clients à risque et à mettre en œuvre des actions de fidélisation adaptées.

---

# 3. Données d'entraînement

Le modèle est entraîné sur le jeu de données **Telco Customer Churn**.

Les variables utilisées décrivent :

- les informations démographiques ;
- les services souscrits ;
- le contrat ;
- les informations de facturation.

Variable cible :

**Churn**

- Yes
- No

---

# 4. Variables utilisées

Le modèle utilise les variables suivantes :

- gender
- SeniorCitizen
- Partner
- Dependents
- tenure
- PhoneService
- MultipleLines
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- Contract
- PaperlessBilling
- PaymentMethod
- MonthlyCharges
- TotalCharges

---

# 5. Prétraitement

Le pipeline applique automatiquement :

- imputation des valeurs manquantes ;
- standardisation des variables numériques ;
- encodage One-Hot des variables catégorielles.

Toutes ces transformations sont intégrées dans le pipeline sérialisé.

---

# 6. Performances du modèle

| Indicateur | Valeur |
|------------|:------:|
| F1-score (validation croisée) | 0.631 |
| F1-score (modèle par défaut) | 0.593 |
| Gain après optimisation | +0.038 |
| Calibration | Platt Scaling |
| Tests Pytest | 5 / 5 réussis |

---

# 7. Performance par sous-groupe

Le modèle peut être utilisé pour différents profils de clients :

- clients seniors et non seniors ;
- hommes et femmes ;
- différents types de contrats ;
- différents services Internet.

Dans ce projet, aucune différence significative de performance entre les sous-groupes n'a été étudiée. Une analyse de l'équité (fairness) pourrait être réalisée dans de futurs travaux.

---

# 8. Cas d'utilisation

Le modèle peut être utilisé pour :

- identifier les clients à risque de résiliation ;
- prioriser les campagnes de fidélisation ;
- aider les équipes marketing ;
- assister les équipes commerciales.

---

# 9. Limites du modèle

Le modèle présente plusieurs limites :

- il est entraîné sur un seul jeu de données ;
- il ne prend pas en compte l'évolution du comportement des clients au cours du temps ;
- les performances peuvent diminuer si la distribution des données évolue (data drift) ;
- il ne remplace pas une décision humaine.

---

# 10. Considérations éthiques

Les prédictions doivent être utilisées comme un outil d'aide à la décision.

Le modèle ne doit pas être utilisé comme unique critère pour prendre des décisions ayant un impact important sur les clients.

Une surveillance régulière des performances et des biais éventuels est recommandée.

---

# 11. Déploiement

Le pipeline final est sérialisé avec **Joblib** :

```
model/modele_final_calibre.joblib
```

Le modèle est déployé sous forme d'une API REST avec **FastAPI**.

---

# 12. Pourquoi une Model Card ?

Une **Model Card** est un document qui décrit les caractéristiques, les performances, les limites et les conditions d'utilisation d'un modèle de Machine Learning.

Elle favorise la transparence, la reproductibilité et l'utilisation responsable des modèles.

Les Model Cards sont devenues un standard car elles permettent aux développeurs, aux décideurs et aux utilisateurs de mieux comprendre les capacités et les limites d'un modèle avant son déploiement en production.