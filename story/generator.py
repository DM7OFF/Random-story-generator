from ai.transformer_model import rewrite_story

def generate_story(base_story: str, character: dict) -> str:
    return rewrite_story(base_story, character)
