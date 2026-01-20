import json
import random

def load_stories_by_length(length):
    """Charge les histoires selon la longueur"""
    filename_map = {
        "short": "stories_short.json",
        "medium": "stories_medium.json",
        "long": "stories_long.json"
    }
    path = filename_map.get(length, "stories_short.json")
    with open(path, "r") as f:
        data = json.load(f)
    return data["stories"]  # liste de dict avec text, genre, theme, gender

def get_random_story(length=None, genre=None, theme=None, gender=None, level=None):
    stories = []
    if length:
        stories = load_stories_by_length(length)
    else:
        for l in ["short", "medium", "long"]:
            stories.extend(load_stories_by_length(l))
    
    # Filtrer
    if genre:
        stories = [s for s in stories if s["genre"] == genre]
    if theme:
        stories = [s for s in stories if s["theme"] == theme]
    if gender:
        stories = [s for s in stories if s["gender"] == gender]
    if level:
        stories = [s for s in stories if s["level"] == level]
    
    # Fallback
    if not stories:
        for l in ["short", "medium", "long"]:
            stories.extend(load_stories_by_length(l))
    
    return random.choice(stories)

