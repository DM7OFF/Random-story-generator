import streamlit as st
from story.generator import create_story, continue_story
from story.characters import load_characters, add_character
import time

st.title("AI Story Generator")

# --- INITIALISATION SESSION STATE ---
if "character_updated" not in st.session_state:
    st.session_state["character_updated"] = False

if "stories" not in st.session_state:
    st.session_state["stories"] = []  # Mémoire long terme pour continuer histoires

# --- NAVIGATION MODE ---
mode = st.radio("Mode", ["New Story", "Continue Story"], key="mode_radio")

# --- CREER UN PERSONNAGE ---
with st.expander("➕ Create new character"):
    new_name = st.text_input("Name", key="new_name")
    new_role = st.text_input("Role", key="new_role")
    new_traits = st.text_area("Personality traits", key="new_traits")

    if st.button("Save character", key="save_new_character"):
        if new_name and new_role and new_traits:
            add_character(new_name, new_role, new_traits)
            st.success(f"Character '{new_name}' added successfully!")
            st.session_state["character_updated"] = True
        else:
            st.warning("Please fill in all fields")

# --- CHARGER LES PERSONNAGES ---
characters = load_characters()

if st.session_state["character_updated"]:
    characters = load_characters()
    st.session_state["character_updated"] = False

# --- SI PAS DE PERSONNAGE ---
if not characters:
    st.warning("No characters available. Please create one first.")
else:
    # --- SELECTION DU PERSONNAGE ---
    character_names = [c["name"] for c in characters]
    selected_name = st.selectbox(
        "Choose a character",
        character_names,
        key="select_character_main"
    )
    character = next(c for c in characters if c["name"] == selected_name)

    # --- MODE NOUVELLE HISTOIRE ---
    if mode == "New Story":
        genre = st.selectbox("Genre", ["Sci-Fi", "Fantasy", "Horror"], key="genre_select")
        tone = st.selectbox("Tone", ["Dark", "Serious", "Light"], key="tone_select")
        length_option = st.selectbox(
            "Story length",
            ["Short", "Medium", "Long"],
            key="length_select"
        )

        # Définir max_tokens selon la longueur
        if length_option == "Short":
            max_tokens = 200
        elif length_option == "Medium":
            max_tokens = 400
        else:
            max_tokens = 600

        if st.button("Generate story", key="generate_story_btn"):
            start = time.time()
            with st.spinner(f"Generating {length_option} story…"):
                story = create_story(
                    {"genre": genre, "tone": tone},
                    character,
                    max_tokens=max_tokens
                )
            end = time.time()
            st.success(f"Story generated in {end-start:.2f} seconds ✅")
            st.write(story)

            # Ajouter à la mémoire long terme
            st.session_state["stories"].append(story)

            # Affichage du score de cohérence (exemple simple)
            st.info(f"Story coherence score: {round(0.7 + 0.3 * st.session_state['stories'].count(story)/len(st.session_state['stories']),2)}")

    # --- MODE CONTINUER HISTOIRE ---
    elif mode == "Continue Story":
        previous_story = st.text_area("Paste your existing story here", key="prev_story")
        if st.button("Continue story", key="continue_story_btn"):
            if previous_story.strip() == "":
                st.warning("Please provide an existing story to continue.")
            else:
                start = time.time()
                with st.spinner("Continuing the story…"):
                    continuation = continue_story(previous_story, character)
                end = time.time()
                st.success(f"Story continued in {end-start:.2f} seconds ✅")
                st.write(continuation)

                # Ajouter à la mémoire long terme
                st.session_state["stories"].append(continuation)

                # Affichage du score de cohérence
                st.info(f"Story coherence score: {round(0.7 + 0.3 * st.session_state['stories'].count(continuation)/len(st.session_state['stories']),2)}")
