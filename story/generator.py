from ai.rules_engine import apply_rules
from ai.transformer_model import rewrite_story

def generate_story(base_story, character):
    # Étape 1 : cohérence dure
    ruled_story = apply_rules(base_story, character)

    # Étape 2 : rewrite intelligent
    final_story = rewrite_story(ruled_story, character)

    return final_story
