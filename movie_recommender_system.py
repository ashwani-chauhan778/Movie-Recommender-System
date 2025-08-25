import streamlit as st
# import pickle
# import os
# import requests

# URL to download similarity.pkl - replace this with your actual direct download link
# SIMILARITY_URL = "https://drive.google.com/file/d/1K758ZfEFyF7oQfCjFqFO6sFh8WJoz03N/view?usp=sharing"

# Function to download the large file
# def download_file(url, filename):
#     with requests.get(url, stream=True) as r:
#         r.raise_for_status()
#         with open(filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192):
#                 f.write(chunk)

# --- Page config ---
# st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# --- Load movie list ---
# movies = pickle.load(open('movie_list.pkl', 'rb'))

# --- Ensure similarity.pkl is available ---
# if not os.path.exists('similarity.pkl'):
#     st.warning("Downloading similarity data, please wait...")
#     download_file(SIMILARITY_URL, 'similarity.pkl')
#     st.success("Download complete!")

# Load similarity matrix
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
# def recommend(movie):
    # index = movies[movies['title'] == movie].index[0]
    # distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    # recommended_movies = []
    # for i in distances[1:6]:
        # recommended_movies.append(movies.iloc[i[0]].title)
    # return recommended_movies
#
# Sidebar content
# with st.sidebar:
    # st.title("🍿 About this App")
    # st.write(
        # "This Movie Recommender suggests films similar to your favorites, "
        # "using data science and machine learning under the hood."
    # )
    # st.markdown("---")
    # st.write("Select a movie to begin your cinematic journey!")
# 
# Main content
st.title("🎥 Movie Recommender System")
st.write("Find movies similar to your favorites and discover hidden gems.")

# col1, col2 = st.columns([2, 3], gap="large")

# with col1:
#     st.header("<._.> Choose Your Movie")
#     selected_movie = st.selectbox(
#         "Movie Title:",
#         movies['title'].values,
#         help="Pick a movie you like from this list."
#     )
#     go = st.button("🎬 Recommend Movies")

# with col2:
#     st.header("<._.> Recommendations")
#     if go:
#         recommendations = recommend(selected_movie)
#         for idx, title in enumerate(recommendations, 1):
#             st.markdown(f"### {idx}. {title}")
#     else:
#         st.info("Choose a movie and click 'Recommend Movies' to see suggestions.")

# Footer
# st.markdown("---")
# st.caption("Made with ❤️ - Ashwani")
