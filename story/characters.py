import json
import os

CHARACTERS_FILE = "characters.json"

def load_characters():
    try:
        with open(CHARACTERS_FILE, "r") as f:
            return json.load(f)["characters"]
    except:
        return []

def add_character(name, role, traits, gender, level):
    characters = load_characters()
    new_char = {
        "name": name,
        "role": role,
        "traits": traits,
        "gender": gender,
        "level": level
    }
    characters.append(new_char)
    with open(CHARACTERS_FILE, "w") as f:
        json.dump({"characters": characters}, f, indent=4)
