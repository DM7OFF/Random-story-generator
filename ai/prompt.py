def build_prompt(settings):
    """
    Construit un prompt structuré pour guider l'IA.
    """
    return (
        f"Write a short story.\n"
        f"Genre: {settings['genre']}\n"
        f"Tone: {settings['tone']}\n"
        f"Structure:\n"
        f"Act 1: Introduction\n"
        f"Act 2: Conflict\n"
        f"Act 3: Resolution with a twist\n"
        f"Rules:\n"
        f"- Keep the main character consistent\n"
        f"- Max 600 words\n\n"
        f"Story:\n"
    )
