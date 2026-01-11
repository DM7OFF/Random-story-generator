from ai.model import generate_text
from ai.prompt import build_prompt
from utils.seed import set_seed

def create_story(settings, seed=None):
    """
    Orchestration complète de la génération.
    """
    if seed is not None:
        set_seed(seed)

    prompt = build_prompt(settings)
    story = generate_text(prompt)

    return story
