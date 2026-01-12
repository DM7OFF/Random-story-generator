import streamlit as st
from story.generator import create_story
from story.characters import load_characters

st.title("AI Story Generator")

characters = load_characters()
character_names = [c["name"] for c in characters]
selected_name = st.selectbox("Choose a character", character_names)
character = next(c for c in characters if c["name"] == selected_name)

genre = st.selectbox("Genre", ["Sci-Fi", "Fantasy", "Horror"])
tone = st.selectbox("Tone", ["Dark", "Serious", "Light"])

if st.button("Generate story"):
    # Affiche un spinner pendant la génération
    with st.spinner("Generating story… please wait"):
        story = create_story(
            {"genre": genre, "tone": tone},
            character
        )
    st.success("Story generated ✅")
    st.write(story)
