from ai.model import generate_text
from ai.prompt import build_prompt

def create_story(settings, character, max_tokens=400):
    prompt = f"""
    Write a {settings['tone']} {settings['genre']} story.
    Main character: {character['name']} ({character['role']})
    Personality: {character['traits']}
    Max {max_tokens} tokens.
    """
    return generate_text(prompt, max_tokens=max_tokens)

def continue_story(existing_story, character, max_tokens=400):
    prompt = f"""
    Continue the following story keeping the main character {character['name']} consistent:
    {existing_story}
    Max {max_tokens} tokens.
    """
    return generate_text(prompt, max_tokens=max_tokens)

