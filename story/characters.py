import json
import os

FILE = "data/characters.json"

def load_characters():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_characters(characters):
    with open(FILE, "w") as f:
        json.dump(characters, f, indent=2)

def add_character(name, role, traits):
    characters = load_characters()
    characters.append({
        "name": name,
        "role": role,
        "traits": traits
    })
    save_characters(characters)
