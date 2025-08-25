import streamlit as st
import pickle
import os
import requests

# --- Page Config ---
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# --- Google Drive Direct Download Links ---
MOVIE_FILE_URL = "https://drive.google.com/uc?id=1QkHASca9UN7s0wM6606OubC5nAofGVtZ"
SIMILARITY_FILE_URL = "https://drive.google.com/uc?id=1K758ZfEFyF7oQfCjFqFO6sFh8WJoz03N"

MOVIE_FILE = "movie_list.pkl"
SIMILARITY_FILE = "similarity.pkl"

# --- Download function ---
def download_file(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
    else:
        st.error(f"Failed to download {filename}.")

# --- Ensure files exist ---
if not os.path.exists(MOVIE_FILE):
    st.warning("Downloading movie list file...")
    download_file(MOVIE_FILE_URL, MOVIE_FILE)
    st.success("Movie list downloaded!")

if not os.path.exists(SIMILARITY_FILE):
    st.warning("Downloading similarity matrix...")
    download_file(SIMILARITY_FILE_URL, SIMILARITY_FILE)
    st.success("Similarity matrix downloaded!")

# --- Load Data ---
movies = pickle.load(open(MOVIE_FILE, 'rb'))
similarity = pickle.load(open(SIMILARITY_FILE, 'rb'))

# --- Recommendation Function ---
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# --- Sidebar ---
with st.sidebar:
    st.title("🍿 About this App")
    st.write("This Movie Recommender suggests films similar to your favorites using ML.")
    st.markdown("---")
    st.write("Select a movie to begin your cinematic journey!")

# --- Main Content ---
st.title("🎥 Movie Recommender System")
st.write("Find movies similar to your favorites and discover hidden gems.")

col1, col2 = st.columns([2, 3], gap="large")

with col1:
    st.header("🎬 Choose Your Movie")
    selected_movie = st.selectbox(
        "Movie Title:",
        movies['title'].values,
        help="Pick a movie you like from this list."
    )
    go = st.button("🔍 Recommend Movies")

with col2:
    st.header("🎯 Recommendations")
    if go:
        recommendations = recommend(selected_movie)
        for idx, title in enumerate(recommendations, 1):
            st.markdown(f"### {idx}. {title}")
    else:
        st.info("Choose a movie and click 'Recommend Movies' to see suggestions.")

# --- Footer ---
st.markdown("---")
st.caption("Made with ❤️ by Ashwani")
