# real-time-crypto-tracker
Une pipeline de données en temps réel en Python qui collecte les prix de cryptomonnaie stocke des series temporelles et les visualise

📈 #Suivi des Prix de Cryptomonnaies en Temps Réel
Présentation

Ce projet est un pipeline de données en temps réel qui collecte les prix de cryptomonnaies depuis une API externe, les stocke dans une base de données, puis les affiche dans un tableau de bord interactif.

Il met en pratique les concepts de pipeline de données, intégration d’API, stockage persistant, et visualisation en temps réel en Python.

Que fait le projet ?

Concrètement, le projet :

Récupère les prix de cryptomonnaies en temps réel via une API externe (Binance)

Stocke les prix avec des timestamps dans une base de données SQLite

Affiche le prix actuel, l’évolution dans le temps et des statistiques sur un dashboard

Architecture du Pipeline
[ API Binance ]
       ↓
PriceCollector (Ingestion)
       ↓
DatabaseManager (Stockage - SQLite)
       ↑
DashboardApp (Visualisation)


Le projet suit une architecture classique de pipeline de données :

Ingestion

Transformation légère

Stockage

Restitution / Visualisation

Structure du Projet
price-tracker/
│
├── config.py          # Configuration globale (symboles, API, DB)
├── storage.py         # DatabaseManager (gestion SQLite)
├── collector.py       # PriceCollector (collecte des données)
├── app.py             # DashboardApp (interface Streamlit)
├── requirements.txt   # Dépendances Python
└── data/
    └── prices.db      # Base de données SQLite (créée automatiquement)

Technologies Utilisées

Python

SQLite (stockage des données)

API REST Binance (source des données)

Streamlit (tableau de bord interactif)

Plotly (visualisation graphique)

Pandas (manipulation des données)

Composants Principaux
1️⃣ PriceCollector

Récupère les prix depuis l’API Binance

Fonctionne en continu avec un intervalle fixe

Gère les erreurs d’API sans bloquer le pipeline

Envoie les données valides vers la base de données

2️⃣ DatabaseManager

Initialise la base de données SQLite

Stocke les prix avec des timestamps

Récupère le dernier prix et l’historique

Sert de source de vérité pour les données

3️⃣ DashboardApp

Lit les données depuis la base (lecture seule)

Affiche :

le prix actuel

l’évolution du prix dans le temps

des statistiques simples (min, max, moyenne, variation)

Se rafraîchit automatiquement pour rester à jour

Les Timestamps

Chaque prix est associé à un timestamp, ce qui permet :

d’ordonner correctement les données

de tracer des séries temporelles

de calculer des statistiques dans le temps

de vérifier si les données sont à jour

Comment Lancer le Projet
1) Installer les dépendances
pip install -r requirements.txt

2) Lancer le collecteur de données
python collector.py


Cela permet :

de créer la base de données si elle n’existe pas

de commencer la collecte des prix

3) Lancer le dashboard
streamlit run app.py


Un lien s’affichera dans le terminal pour ouvrir le tableau de bord dans le navigateur.

Configuration

Tous les paramètres sont centralisés dans le fichier config.py :

symboles suivis

endpoints de l’API

chemin de la base de données

intervalle de collecte

Cela permet de modifier le comportement du projet sans toucher à la logique.

Pourquoi c’est un Pipeline de Données

Ce projet est un pipeline de données en temps réel car il :

ingère des données externes en continu

les traite de manière incrémentale

les stocke de façon persistante

les restitue sous forme de visualisation

Améliorations Possibles

Utiliser WebSocket au lieu du polling REST

Ajouter des logs et des métriques

Supporter d’autres sources (actions, forex)

Déployer le dashboard en ligne

Ajouter des alertes de prix
