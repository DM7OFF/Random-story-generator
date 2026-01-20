def apply_rules(story, character):
    name = character["name"]
    role = character["role"]
    traits = character["traits"].lower()

    if name not in story:
        story = story.replace("the character", name)
        story = story.replace("a scientist", f"{name}, a {role}")

    if "thought" not in story.lower():
        story += f"\n\n{name} reflects silently, his {traits} nature guiding his decisions."

    return story
