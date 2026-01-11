def validate_structure(story):
    """
    Vérifie si l'histoire contient 3 actes.
    """
    acts = ["Act 1", "Act 2", "Act 3"]
    return all(act in story for act in acts)
