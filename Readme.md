
# AI Story Generator 

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Interactive-orange)](https://streamlit.io/)
[![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Transformers-purple)](https://huggingface.co/)

**AI Story Generator** est une application web interactive qui utilise l’IA pour générer des histoires personnalisées avec des personnages persistants et évolutifs.  
Ce projet met en valeur **l’intégration IA + UI interactive + gestion de la mémoire long terme**.

---

##  Fonctionnalités clés

###  Gestion des personnages
- Créez et gérez des personnages avec nom, rôle et traits de personnalité
- Personnages persistants pour générer plusieurs histoires
- Interface intuitive via **expander** pour ajouter de nouveaux personnages

### 📖 Génération d’histoires
- Nouvelle histoire basée sur le personnage choisi
- Choix de **genre** (Sci-Fi, Fantasy, Horror) et **tonalité** (Dark, Serious, Light)
- Choix de **longueur** : Short / Medium / Long
- Spinner et timer pour UX professionnelle

### 🔄 Mode “Continuer l’histoire”
- Collez une histoire existante et générez la suite
- Mémoire long terme pour suivre l’évolution des personnages et histoires
- Permet un storytelling interactif et dynamique

### 📊 Score de cohérence
- Indicateur simple pour mesurer la cohérence des histoires
- Extensible avec NLP embeddings pour des scores avancés

### 🖥️ Interface utilisateur
- Navigation entre **New Story** et **Continue Story** via radio buttons
- Tous les widgets avec `key` unique → pas d’erreurs Streamlit
- Responsive et facile à utiliser  

---

## 🛠️ Technologies utilisées

- **Python 3.13**  
- **Streamlit** pour l’interface web interactive  
- **Hugging Face Transformers** (distilgpt2) pour la génération de texte  
- **Session State** pour la mémoire long terme  
- Prompting et logique personnalisée pour chaque personnage  

---

## 🚀 Installation

1. Clonez le dépôt :

```bash
git clone https://github.com/votreusername/ai-story-generator.git
cd ai-story-generator
````

2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

3. Lancez l’application :

```bash
streamlit run app.py
```

---

## 🎮 Utilisation

### 1️⃣ Créer un personnage

* Cliquez sur **“➕ Create new character”**
* Remplissez le **nom**, **rôle** et **traits**
* Cliquez sur **Save character** pour ajouter le personnage à la liste

### 2️⃣ Nouvelle histoire

* Sélectionnez un personnage existant
* Choisissez **genre**, **ton** et **longueur**
* Cliquez sur **Generate story**
* La story générée s’affiche avec un **timer** et un **score de cohérence**

### 3️⃣ Continuer l’histoire

* Collez une histoire existante
* Cliquez sur **Continue story** pour générer la suite
* Les histoires précédentes sont mémorisées pour suivre l’évolution des personnages

---

## 📸 Aperçu de l’interface

![AI Story Generator Screenshot](#)
*Nouvelle histoire avec sélection de personnage et longueur*

![AI Story Generator Screenshot](#)
*Mode Continuer l’histoire avec mémoire long terme*

---

## 💡 À propos du projet

Ce projet démontre :

* L’intégration d’IA générative dans un produit interactif
* La gestion de **mémoire long terme et évolution de personnages**
* Une interface intuitive et responsive avec Streamlit
* Optimisation de la génération de texte avec **pipeline cache** et **contrôle du nombre de tokens**

---

## 🚀 Améliorations futures

* Personnages évolutifs selon les histoires générées
* Score de cohérence basé sur **embeddings NLP réels**
* Story branching → choix utilisateur influençant la suite de l’histoire
* UI plus riche avec **sidebar**, thèmes, et animations

---

## 📂 Structure du projet

```
ai-story-generator/
├── app.py                # Interface principale Streamlit
├──data/
│   ├── characters.json   # stockage characters predefinis
├── story/
│   ├── generator.py      # Logique de génération d’histoire
│   └── characters.py     # Gestion des personnages
├── ai/
│   └── model.py          # Pipeline HuggingFace
├── requirements.txt      # Dépendances
└── README.md
```

---

## 🔗 Liens

* [Streamlit](https://streamlit.io/)
* [Hugging Face Transformers](https://huggingface.co/transformers/)

---

### Auteur

**Dm7** – Portfolio personnel / Projet IA interactif

```
