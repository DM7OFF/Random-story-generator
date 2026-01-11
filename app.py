import streamlit as st
from story.generator import create_story

st.title("AI Story Generator (Local)")

genre = st.selectbox("Genre", ["Sci-Fi", "Fantasy", "Horror"])
tone = st.selectbox("Tone", ["Dark", "Light", "Serious"])
seed = st.number_input("Seed (optional)", value=0)

if st.button("Generate"):
    story = create_story(
        {"genre": genre, "tone": tone},
        seed=seed if seed != 0 else None
    )
    st.write(story)
