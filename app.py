import streamlit as st
import time

# ===== Imports projet =====
from story.library import get_random_story, load_stories
from story.characters import load_characters, add_character
from story.generator import generate_story
from ai.transformer_model import init_transformer

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="AI Story Generator", layout="centered")
st.title(" AI Story Generator")

# =========================
# SESSION STATE INIT
# =========================
if "generated_stories" not in st.session_state:
    st.session_state["generated_stories"] = []

if "characters_updated" not in st.session_state:
    st.session_state["characters_updated"] = False

if "last_story" not in st.session_state:
    st.session_state["last_story"] = ""

if "transformer_initialized" not in st.session_state:
    st.session_state["transformer_initialized"] = False

# =========================
# LOAD CHARACTERS
# =========================
characters = load_characters()

# =========================
# INIT TRANSFORMER (ONE-TIME)
# =========================
if not st.session_state["transformer_initialized"]:
    all_stories = []
    for length in ["short", "medium", "long"]:
        for s in load_stories(length):
            all_stories.append(s["text"])
    init_transformer(all_stories)
    st.session_state["transformer_initialized"] = True

# =========================
# NAVIGATION
# =========================
menu = st.sidebar.radio("Menu", ["Generate Story", "Continue Story", "Create Character"])

# =========================
# CREATE CHARACTER
# =========================
if menu == "Create Character":
    st.header("➕ Create a New Character")
    new_name = st.text_input("Name")
    new_role = st.text_input("Role")
    new_traits = st.text_area("Personality traits")
    new_gender = st.radio("Gender", ["Male", "Female"])
    new_level = st.selectbox("Writing level", ["Primary", "Secondary", "College"])
if st.button("Save character"):
    if new_name and new_role and new_traits:
        add_character(new_name, new_role, new_traits, new_gender, new_level)
        st.success(f"Character '{new_name}' added successfully!")
        st.session_state["characters_updated"] = True
        st.rerun()  # Relance l'app pour mettre à jour la liste des personnages
    else:
        st.warning("Please fill in all fields")

# =========================
# SELECT CHARACTER
# =========================
st.subheader("Character Selection")
character_names = [c["name"] for c in characters]
selected_name = st.selectbox("Choose a character", character_names)

# Assure que character existe
character = next((c for c in characters if c["name"] == selected_name), None)

if character is None:
    st.warning("Please create a character first!")
    st.stop()

# =========================
# STORY SETTINGS
# =========================
if menu == "Generate Story":
    st.header("Generate a New Story")

    length = st.selectbox("Story length", ["short", "medium", "long"])
    genre = st.selectbox("Genre", ["Sci-Fi", "Fantasy", "Horror"])
    theme = st.selectbox("Theme", ["Adventure", "Mystery", "Romance", "Thriller"])
    gender = st.radio("Main character gender", ["Male", "Female"])
    level = st.selectbox("Writing level", ["Primary", "Secondary", "College"])

    token_map = {"short": 200, "medium": 350, "long": 500}
    max_tokens = token_map[length]

    if st.button("Generate story"):
        with st.spinner("Generating story..."):
            # On essaie d'obtenir une story unique
            attempts = 0
            while True:
                base_story = get_random_story(length, genre, theme, gender, level)
                if base_story["text"] not in st.session_state["generated_stories"]:
                    break
                attempts += 1
                if attempts > 10:
                    break

            # Génération finale
            final_story = generate_story(base_story["text"], character)


            # Stocker dans session_state
            st.session_state["generated_stories"].append(base_story["text"])
            st.session_state["last_story"] = final_story

        st.success("Story generated ✅")
        st.markdown(f"**Genre:** {genre} | **Theme:** {theme} | **Level:** {level}")
        st.write(final_story)

# =========================
# CONTINUE STORY
# =========================
elif menu == "Continue Story":
    st.header("Continue Your Last Story")
    if not st.session_state["last_story"]:
        st.info("No story available. Please generate a story first.")
    else:
        if st.button("Continue story"):
            with st.spinner("Continuing story..."):
                continued = generate_story(st.session_state["last_story"], character)

            st.session_state["last_story"] = continued
            st.markdown(f"**Character:** {character['name']} | **Level:** {character['level']}")
            st.write(continued)
