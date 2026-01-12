import streamlit as st
from story.generator import create_story
from story.characters import load_characters, add_character
import time

st.title("AI Story Generator")

# --- CHARGER PERSONNAGES EXISTANTS ---
characters = load_characters()
character_names = [c["name"] for c in characters]

# Ajouter une option spéciale pour créer un nouveau personnage
character_names_with_create = character_names + ["➕ Create new character"]
selected_name = st.selectbox("Choose a character", character_names_with_create)

# --- SI L'UTILISATEUR VEUT CREER UN PERSONNAGE ---
if selected_name == "➕ Create new character":
    # Modal pour créer un personnage
    with st.modal("Create a new character"):
        st.header("New Character")
        new_name = st.text_input("Name")
        new_role = st.text_input("Role")
        new_traits = st.text_area("Personality traits")
        
        if st.button("Save character"):
            if new_name and new_role and new_traits:
                add_character(new_name, new_role, new_traits)
                st.success(f"Character '{new_name}' added successfully!")
                st.experimental_rerun()  # Recharger la page pour mettre à jour la liste
            else:
                st.warning("Please fill in all fields")

# --- SINON ON CHOISIT UN PERSONNAGE EXISTANT ---
elif characters:  # s'assurer qu'il y a au moins un personnage
    character = next(c for c in characters if c["name"] == selected_name)

    # --- PARAMETRES DE L'HISTOIRE ---
    genre = st.selectbox("Genre", ["Sci-Fi", "Fantasy", "Horror"])
    tone = st.selectbox("Tone", ["Dark", "Serious", "Light"])

    # Choix de la longueur de l'histoire
length_option = st.selectbox(
    "Story length",
    ["Short", "Medium", "Long"]
)

# Définir max_tokens selon le choix
if length_option == "Short":
    max_tokens = 200
elif length_option == "Medium":
    max_tokens = 400
else:  # Long
    max_tokens = 600


    # --- GENERER L'HISTOIRE ---
if st.button("Generate story"):
    start = time.time()
    with st.spinner(f"Generating {length_option} story…"):
        story = create_story(
            {"genre": genre, "tone": tone},
            character,
            max_tokens=max_tokens  # <-- on passe le max_tokens ici
        )
    end = time.time()
    st.success(f"Story generated in {end-start:.2f} seconds ✅")
    st.write(story)


else:
    st.warning("No characters available. Please create one first.")
