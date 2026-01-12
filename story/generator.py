from ai.model import generate_text
from ai.prompt import build_prompt

def create_story(settings, character):
    prompt = build_prompt(settings, character)
    return generate_text(prompt)
