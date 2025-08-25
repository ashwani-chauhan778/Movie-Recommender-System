import streamlit as st
import pickle

# --- Page Config ---
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# --- Title ---
st.title("🎥 Movie Recommender System")
st.write("Find movies similar to your favorites and discover hidden gems.")

# --- File Upload Section ---
st.sidebar.header("📂 Upload Files")
st.sidebar.write("Please upload both files to continue:")

uploaded_movies = st.sidebar.file_uploader("Upload `movie_list.pkl`", type="pkl")
uploaded_similarity = st.sidebar.file_uploader("Upload `similarity.pkl`", type="pkl")

if uploaded_movies is not None and uploaded_similarity is not None:
    # Load the uploaded pickle files
    try:
        movies = pickle.load(uploaded_movies)
        similarity = pickle.load(uploaded_similarity)
        st.sidebar.success("Files loaded successfully!")
    except Exception as e:
        st.error("Error loading files. Make sure you uploaded valid pickle files.")
        st.stop()
else:
    st.warning("Please upload both `movie_list.pkl` and `similarity.pkl` to continue.")
    st.stop()

# --- Recommendation Function ---
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:  # Top 5 recommendations
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# --- UI Layout ---
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
