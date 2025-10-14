# Évaluation de faisabilité des livrables du projet

## Contexte actuel
Le dépôt contient uniquement un README succinct et un notebook de modélisation (`V_Maxime_2_notebook_modélisation_092025.ipynb`). Les livrables demandés couvrent l'intégralité du cycle de vie d'une solution de scoring : préparation des données, modélisation, suivi des expériences avec MLflow, déploiement d'une API, monitoring (data drift), outils de test et support de présentation.

## Livrables à produire
1. **API de prédiction déployée sur le cloud**, accompagnée d'une documentation d'introduction et d'une liste des dépendances.
2. **Notebook ou scripts de modélisation** du prétraitement à la prédiction, intégrant le suivi d'expérimentations MLflow et un stockage centralisé des modèles.
3. **Accès à l'interface MLflow** (UI) et captures d'écran pour la soutenance.
4. **Dépôt versionné structuré** avec explications, requirements et code de déploiement.
5. **Tableau HTML d'analyse de data drift** généré avec Evidently.
6. **Notebook ou application Streamlit** pour tester l'API déployée.
7. **Support de présentation (≤ 30 slides)** incluant captures d'écran et preuves du pipeline de déploiement (commits, dépôt GitHub, exécution des tests, déploiement de l'API et lien cloud).

## Travaux nécessaires
- Mettre en place et valider le suivi MLflow (serveur, journalisation des expériences, registre de modèles).
- Concevoir et documenter le pipeline de préparation des données, le feature engineering et l'entraînement des modèles avec évaluation pertinente (métriques métier, cross-validation, gestion du déséquilibre, baseline, etc.).
- Produire les analyses d'importance globale et locale des variables.
- Développer, conteneuriser et déployer une API d'inférence sur le cloud choisi, avec tests automatisés.
- Générer le rapport Evidently et l'intégrer au dépôt.
- Créer l'outil de test (notebook/Streamlit) consommant l'API en production.
- Préparer le support de soutenance avec le storytelling, les captures d'écran et les preuves d'automatisation.

## Estimation du temps et risques
Réussir ces tâches depuis l'état actuel du dépôt demande plusieurs journées de travail concentré, même avec une bonne préparation. Les postes de charge principaux sont :
- Plusieurs heures pour expérimenter, expliquer et instrumenter MLflow correctement.
- Des heures supplémentaires pour développer, sécuriser et déployer l'API sur le cloud.
- Encore du temps pour le monitoring, les outils de test et la préparation du support de soutenance.

Avec ce volume et l'absence d'infrastructure existante, livrer l'ensemble des livrables en **seulement quatre heures** n'est **pas réaliste** sans disposer d'artefacts déjà prêts, testés et documentés.

## Recommandations
- Prioriser le chemin critique : finaliser le pipeline de modélisation avec MLflow, produire une API minimale fonctionnelle et documenter la structure du dépôt.
- Réutiliser tout actif existant (modèles, scripts, templates de présentation) pour gagner du temps.
- Si l'échéance de quatre heures est incompressible, alerter le commanditaire et négocier une livraison par lots, en visant d'abord le notebook, un prototype d'API et un plan de documentation.
- Planifier une phase ultérieure (plusieurs jours) pour consolider tests, monitoring, CI/CD et présentation complète.

## Prochaines étapes proposées
1. Auditer les travaux déjà disponibles (code, expériences, scripts de déploiement) afin d'identifier ce qui est réutilisable immédiatement.
2. Construire un planning réaliste sur plusieurs jours, en explicitant les dépendances et les besoins (compétences, accès cloud, budget éventuel).
3. Communiquer les contraintes au commanditaire pour ajuster le périmètre ou étendre le délai.

## Compléments recommandés pour le notebook Home Credit Default
Pour répondre aux critères d'évaluation (CE) d'OpenClassrooms et couvrir le périmètre de la compétition Kaggle « Home Credit Default Risk », structure ton notebook comme un rapport complet du prétraitement jusqu'au choix du modèle final.

### 1. Introduction et compréhension des données
- Présenter le contexte métier (score de défaut de paiement) et la cible `TARGET`.
- Documenter les sources de données externes et les différentes tables du jeu Kaggle, avec un schéma de jointure.
- Ajouter une checklist des critères CE visés pour montrer la couverture dans le notebook.

### 2. Préparation des données (CE1 à CE5)
- Charger les datasets (application_train/test, bureau, bureau_balance, previous_application, POS_CASH, installments_payments, credit_card_balance) et détailler les opérations de fusion (left joins sur `SK_ID_CURR`).
- Identifier les variables catégorielles et appliquer les transformations adaptées :
  - **OneHotEncoder** sur les colonnes nominales (CE1) avec un `ColumnTransformer`.
  - **Target/Mean encoding** sur les variables à haute cardinalité, en séparant strictement train/test pour éviter le data leakage (CE7).
- Décrire et implémenter les imputations :
  - Valeurs numériques : imputation par médiane ou modèles plus avancés (KNNImputer) en justifiant les choix.
  - Valeurs catégorielles : valeur « Missing » explicite ou mode.
- Ajouter les transformations mathématiques pertinentes (CE3) :
  - Logarithme sur les montants positifs fortement skewed (`AMT_CREDIT`, `AMT_ANNUITY`).
  - Box-Cox ou Yeo-Johnson via `PowerTransformer` pour normaliser certaines distributions.
- Normaliser/standardiser les variables numériques lorsque le modèle en a besoin (CE4), via `StandardScaler` ou `RobustScaler` dans le pipeline.

### 3. Feature engineering (CE2)
- Ajouter des variables dérivées documentées (justifier l'intérêt métier) :
  - Ratios de solvabilité : `AMT_CREDIT / AMT_INCOME_TOTAL`, `ANNUITY_INCOME_PERC`.
  - Scores d'historique de crédit : nombre de crédits actifs, durée moyenne, retards (`DPD`, `DBD`).
  - Agrégations multi-table : moyenne/max/min/sum sur `bureau`, `previous_application`, `installments_payments` regroupées par `SK_ID_CURR`.
- Inclure des features temporelles : délai depuis dernier prêt, stabilité de revenus.
- Documenter l'impact des features nouvellement créées sur la distribution et corrélation avec la cible.
- Mettre en place une section d'analyse de corrélation/importance préliminaire pour vérifier qu'aucune variable ne fuit la cible (CE7).

### 4. Gestion du déséquilibre de classes et métrique métier (CE5 & CE1 éval perf)
- Calculer la proportion de défaut (`TARGET=1`) et justifier le choix de la stratégie.
- Implémenter :
  - **Baseline** avec `DummyClassifier` (stratégie `most_frequent` et `stratified`).
  - **LogisticRegression** avec `class_weight='balanced'` et comparaison avec version sans pondération.
  - **RandomForestClassifier** avec réglage de `class_weight` ou `max_depth`, `n_estimators`, `min_samples_leaf`.
  - **XGBoost** (ou `XGBClassifier`) avec paramètre `scale_pos_weight` dérivé du ratio négatifs/positifs.
- Tester une méthode de rééchantillonnage (SMOTE/SMOTENC ou ADASYN) sur un pipeline séparé pour comparer aux approches par pondération.
- Définir un **score métier** (ex. coût économique FN/FP) et implémenter une fonction de coût personnalisée pour la recherche d'hyperparamètres (CE1 perf). Documenter les hypothèses de coûts.

### 5. Validation, tuning et suivi MLflow (CE6 à CE8 & pipeline)
- Mettre en place une séparation `train/valid/test` ou `train/test` avec `StratifiedKFold`.
- Implémenter une `Pipeline` scikit-learn orchestrant : imputations → encodages → scaling → modèle.
- Configurer `RandomizedSearchCV` ou `GridSearchCV` pour chaque algorithme (logistique, forêt, XGBoost), avec validation croisée stratifiée (CE7).
- Logguer chaque expérience dans MLflow : paramètres, métriques (AUC, F1, score métier), artefacts (confusion matrix, ROC, PR curves), modèle sérialisé.
- Conserver les résultats dans un tableau comparatif (du plus simple au plus complexe) et justifier le choix du modèle retenu (CE8).

### 6. Interprétabilité (CE9)
- Calculer les **feature importances globales** (gain pour XGBoost, permutation importance pour modèles non interprétables).
- Utiliser **SHAP** ou `shap.TreeExplainer` pour l'analyse locale (fiches clients).
- Documenter l'interprétation des variables clés et leur cohérence métier.

### 7. Contrôles de qualité et reproductibilité (CE1 pipeline)
- Fixer les seeds (`numpy`, `random`, frameworks) pour assurer la reproductibilité.
- Sérialiser le meilleur pipeline et le déposer dans un dossier `models/` enregistré via MLflow Model Registry (CE2 pipeline).
- Décrire dans le notebook comment rejouer l'expérience à partir du code et de MLflow (CE3 pipeline).

### 8. Pistes pour la suite du livrable
- Ajouter une cellule décrivant le lien entre le notebook et l'API (comment le modèle est consommé, endpoints prévus).
- Préparer l'extraction des métriques et courbes qui alimenteront la présentation (screenshots, liens MLflow).
- Mentionner les prochaines étapes pour Evidently (datasets de référence vs. production) afin d'articuler le monitoring.

### Organisation conseillée des sections du notebook
1. Contexte & objectifs
2. Chargement des données & audit qualité
3. Feature engineering multi-sources
4. Préparation des pipelines de preprocessing
5. Gestion du déséquilibre et métriques métier
6. Baselines & modèles candidats
7. Optimisation & suivi MLflow
8. Interprétabilité (global/local)
9. Sélection du modèle final & sauvegarde
10. Lien avec l'API & monitoring

En intégrant ces éléments, ton notebook démontrera l'ensemble des compétences évaluées (CE) et préparera les livrables suivants : modèle final, suivi MLflow, base pour l'API et éléments de présentation.
