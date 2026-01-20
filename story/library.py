import json
import random
from pathlib import Path

STORY_DIR = Path(__file__).parent.parent / "data" / "story_library"

def load_stories_by_length(length):
    """Charge toutes les histoires d'une longueur donnée"""
    file_map = {
        "short": STORY_DIR / "short_story.json",
        "medium": STORY_DIR / "medium_story.json",
        "long": STORY_DIR / "long_story.json",
    }
    file_path = file_map.get(length)
    if not file_path.exists():
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Alias pour compatibilité avec ton app.py
load_stories = load_stories_by_length

def get_random_story(length, genre=None, theme=None, gender=None, level=None):
    """Retourne une histoire aléatoire filtrée par genre, thème, gender et level"""
    stories = load_stories(length)  # utilise l’alias
    # Filtrage selon paramètres
    if genre:
        stories = [s for s in stories if s.get("genre") == genre]
    if theme:
        stories = [s for s in stories if s.get("theme") == theme]
    if gender:
        stories = [s for s in stories if s.get("gender") == gender]
    if level:
        stories = [s for s in stories if s.get("level") == level]

    if not stories:
        return {"text": "No story found for these settings."}

    return random.choice(stories)
