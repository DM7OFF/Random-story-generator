import json
import os

def load_stories(length):
    """
    Charge les stories d'une catégorie : 'short', 'medium', 'long'
    """
    file_map = {
        "short": "data/story_library/short_story.json",
        "medium": "data/story_library/medium_story.json",
        "long": "data/story_library/long_story.json"
    }

    path = file_map[length]
    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as f:
        stories = json.load(f)
    return stories

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

