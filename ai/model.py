from transformers import pipeline

# Charge un modèle de génération de texte local
generator = pipeline(
    "text-generation",
    model="gpt2-medium"
)

def generate_text(prompt, max_tokens=500):
    """
    Génère du texte à partir d'un prompt.

    prompt: texte d'entrée contrôlé
    max_tokens: longueur maximale de la sortie
    """
    output = generator(
        prompt,
        max_length=max_tokens,
        temperature=0.8,
        do_sample=True
    )

    return output[0]["generated_text"]
