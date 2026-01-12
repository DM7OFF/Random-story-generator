import streamlit as st
from story.generator import create_story
from story.characters import load_characters, add_character

st.title("AI Story Generator")

st.header("Create a character")
name = st.text_input("Name")
role = st.text_input("Role")
traits = st.text_area("Personality traits")

if st.button("Save character"):
    add_character(name, role, traits)
    st.success("Character saved")

characters = load_characters()
character_names = [c["name"] for c in characters]

selected_name = st.selectbox("Choose a character", character_names)
character = next(c for c in characters if c["name"] == selected_name)

genre = st.selectbox("Genre", ["Sci-Fi", "Fantasy", "Horror"])
tone = st.selectbox("Tone", ["Dark", "Serious", "Light"])

if st.button("Generate story"):
    story = create_story(
        {"genre": genre, "tone": tone},
        character
    )
    st.write(story)
