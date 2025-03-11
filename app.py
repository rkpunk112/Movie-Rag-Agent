import streamlit as st
import requests

st.title("🎬 Movie Search RAG Agent By RoHiT Thakur-->")

query = st.text_input("Enter a movie name:")
if st.button("Search"):
    response = requests.get("http://127.0.0.1:8000/search", params={"query": query})

    if response.status_code == 200:
        data = response.json()

        # Display movie details
        st.subheader("📌 Movie Details")
        movie_details = data["Movie Details"]
        if movie_details.get("Title"):
            st.write(f"🎥 **Title:** {movie_details['Title']}")
            st.write(f"⭐ **IMDB Rating:** {movie_details.get('imdbRating', 'N/A')}")
            st.write(f"📅 **Release Year:** {movie_details.get('Year', 'N/A')}")
            st.write(f"📖 **Plot:** {movie_details.get('Plot', 'N/A')}")
            st.image(movie_details.get("Poster"), width=250)
        else:
            st.write("❌ Movie not found!")

        # Display YouTube trailer
        st.subheader("🎞️ Trailer")
        if "No trailer found" not in data["Trailer"]:
            st.video(data["Trailer"])
        else:
            st.write("❌ No trailer available.")
