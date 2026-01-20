# AI Story Generator 

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Interactive-orange)](https://streamlit.io/)
[![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Transformers-purple)](https://huggingface.co/)

**AI Story Generator** est une application web interactive qui utilise l’IA pour générer des histoires personnalisées avec des personnages **persistants, évolutifs et cohérents**.  
Ce projet met en valeur **l’intégration IA + UI interactive + mémoire long terme**.

---

## 🚀 Fonctionnalités clés

### 👤 Gestion des personnages
- Créez et gérez des personnages avec :
  - Nom
  - Rôle
  - Traits de personnalité
  - Sexe (Masculin / Féminin)
  - Niveau d’écriture (Primary, Secondary, College)
- Personnages persistants pour générer plusieurs histoires
- Interface intuitive via **expander** pour ajouter de nouveaux personnages

### 📖 Génération d’histoires
- Nouvelle histoire basée sur le personnage choisi
- Choix de **genre** : Sci-Fi, Fantasy, Horror
- Choix de **thème** : Adventure, Mystery, Romance, Thriller
- Choix de **longueur** : Short / Medium / Long
- Histoire unique garantie pour chaque utilisateur
- Spinner et timer pour UX professionnelle

### 🔄 Mode “Continuer l’histoire”
- Continuez une histoire générée précédemment
- Mémoire long terme pour suivre l’évolution des personnages et histoires
- Génère des histoires cohérentes avec les personnages

### 📊 Score de cohérence
- Indicateur simple pour mesurer la cohérence des histoires
- Extensible avec NLP embeddings pour des scores avancés

### 🖥️ Interface utilisateur
- Navigation via **sidebar menu** : Generate Story / Continue Story / Create Character
- Widgets Streamlit avec `key` unique → pas d’erreurs
- Responsive et facile à utiliser
- Affichage clair des tags : Genre, Thème, Niveau, Sexe du personnage

---

## 🛠️ Technologies utilisées

- **Python 3.13**
- **Streamlit** pour l’interface web interactive  
- **Hugging Face Transformers** (Mini-Transformer) pour la génération de texte  
- **Session State** pour la mémoire long terme  
- Bibliothèque JSON pour la **story library**  
- Prompting et logique personnalisée pour chaque personnage  

---

## ⚡ Installation

1. Clonez le dépôt :

```bash
git clone https://github.com/votreusername/ai-story-generator.git
cd ai-story-generator

```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```
3. Lancez l’application :
```bash
streamlit run app.py
```
🎮 Utilisation
1️⃣ Créer un personnage

Cliquez sur “➕ Create new character”

Remplissez le nom, rôle, traits, sexe et niveau d’écriture

Cliquez sur Save character pour ajouter le personnage à la liste

2️⃣ Générer une nouvelle histoire

Sélectionnez un personnage existant

Choisissez genre, thème, niveau et longueur

Cliquez sur Generate story

L’histoire générée s’affiche avec spinner, tags et score de cohérence

3️⃣ Continuer l’histoire

Allez dans Continue Story

Cliquez sur Continue story pour générer la suite

L’histoire précédente est mémorisée pour suivre l’évolution des personnages

📸 Aperçu de l’interface

Nouvelle histoire : sélection de personnage et longueur

Mode Continue Story : mémoire long terme et cohérence des personnages

💡 À propos du projet

Ce projet démontre :

L’intégration d’IA générative dans un produit interactif

La gestion de mémoire long terme et l’évolution des personnages

Une interface intuitive et responsive avec Streamlit

Optimisation de la génération de texte avec Mini-Transformer et contrôle du nombre de tokens

UI riche avec sidebar et tags visuels

🚀 Améliorations futures

Personnages évolutifs selon les histoires générées

Story branching → choix utilisateur influençant la suite

Interface “book-like” et export PDF des histoires

📂 Structure du projet
ai-story-generator/
├── app.py                      # Interface principale Streamlit
├── data/
│   ├── characters.json         # Stockage des personnages
│   └── story_library/
│       ├── long_story.json
│       ├── medium_story.json
│       └── short_story.json
├── story/
│   ├── generator.py            # Logique de génération d’histoire
│   ├── characters.py           # Gestion des personnages
│   └── library.py              # Récupération des stories depuis JSON
├── ai/
│   ├── coherence_score.py      # Calcul du score de cohérence
│   ├── rules_engine.py         # Règles personnalisées pour la génération
│   └── transformer_model.py    # Mini-Transformer pour générer/continuer histoires
├── requirements.txt            # Dépendances
└── README.md

🔗 Liens utiles

Streamlit

Hugging Face Transformers

Auteur

Dm7 – Portfolio personnel / Projet IA interactif