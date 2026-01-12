from ai.model import generate_text
from ai.prompt import build_prompt  # si tu veux garder des prompts dynamiques

def create_story(settings, character, max_tokens=400):
    prompt = f"""
Write a {settings['tone']} {settings['genre']} story.
The story must focus on the main character named {character['name']}.
Role: {character['role']}
Personality traits: {character['traits']}
Keep the main character consistent throughout the story.
Include actions, dialogue, and internal thoughts of the main character.
Make it engaging and coherent.
Max {max_tokens} tokens.
"""
    return generate_text(prompt, max_tokens=max_tokens)

def continue_story(existing_story, character, max_tokens=400):
    prompt = f"""
Continue the following story. Make sure the main character {character['name']} remains the focus:
{existing_story}

Character role: {character['role']}
Personality traits: {character['traits']}
Keep the main character consistent throughout the story.
Include actions, dialogue, and internal thoughts of the main character.
Make the continuation coherent, engaging, and connected to the previous story.
Max {max_tokens} tokens.
"""
    return generate_text(prompt, max_tokens=max_tokens)
