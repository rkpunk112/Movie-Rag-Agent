from fastapi import FastAPI
import requests

app = FastAPI()

YOUTUBE_API_KEY = "Your_youtube_api_key" # Replace with your API key
OMDB_API="Your_OMDB_API_KEY" #Replace with omdb api key
def search_movie(query):
    """Fetch movie details from OMDB API"""
    omdb_url = f"http://www.omdbapi.com/?t={query}&apikey={OMDB_API}"  # Replace with your OMDB API key
    response = requests.get(omdb_url)
    return response.json()

def search_youtube_trailer(movie_name):
    """Fetch YouTube trailer link"""
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={movie_name}+trailer&type=video&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["items"]:
            video_id = data["items"][0]["id"]["videoId"]
            return f"https://www.youtube.com/watch?v={video_id}"
    return "No trailer found."

@app.get("/search")
def get_movie_info(query: str):
    movie_details = search_movie(query)
    trailer_link = search_youtube_trailer(query)
    return {"Movie Details": movie_details, "Trailer": trailer_link}
