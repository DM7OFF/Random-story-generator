from ai.model import generate_text
from ai.prompt import build_prompt

def create_story(settings, character, max_tokens=400):
    """
    Génère une histoire avec le personnage choisi
    max_tokens: longueur de l'histoire
    """
    prompt = build_prompt(settings, character)
    story = generate_text(prompt, max_tokens=max_tokens)
    return story
