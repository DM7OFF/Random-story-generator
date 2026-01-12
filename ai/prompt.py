def build_prompt(settings, character):
    return (
        f"Write a {settings['tone'].lower()} {settings['genre'].lower()} story.\n"
        f"The story must strictly follow a three-act structure.\n\n"
        f"Main character:\n"
        f"Name: {character['name']}\n"
        f"Role: {character['role']}\n"
        f"Personality traits: {character['traits']}\n\n"
        f"Rules:\n"
        f"- The main character must stay consistent\n"
        f"- Do not rename the character\n"
        f"- End with an unexpected twist\n\n"
        f"Act 1:\n"
    )
