import streamlit as st
from transformers import pipeline

# Charger le pipeline une seule fois (Streamlit cache)
@st.cache_resource(show_spinner=False)
def get_generator():
    return pipeline(
        "text-generation",
        model="distilgpt2",   # plus léger et rapide
        pad_token_id=50256
    )

generator = get_generator()

def generate_text(prompt, max_tokens=400):  # réduire le nombre de tokens pour aller plus vite
    output = generator(
        prompt,
        max_new_tokens=max_tokens,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2,
        do_sample=True
    )
    return output[0]["generated_text"][len(prompt):].strip()
