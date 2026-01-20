def coherence_score(story, character):
    score = 0

    if character["name"] in story:
        score += 0.4

    for trait in character["traits"].split(","):
        if trait.strip().lower() in story.lower():
            score += 0.2

    return min(round(score, 2), 1.0)
