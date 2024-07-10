import pickle
import streamlit as st
import pandas as pd
from src.recommendation_utils import recommend_movies
import sys

# For our sanity
import warnings
warnings.filterwarnings('ignore')

st.header('Faithfuls Movie Recommender')
@st.cache_data
def load_data():
    model = pickle.load(open('files/svdmodel.pkl', 'rb'))
    movies = pickle.load(open('files/titles.pkl', 'rb'))
    links = pickle.load(open('files/links.pkl', 'rb'))
    return model, movies, links

model, movies, links = load_data()

# Load the API key from a secure location
api_key = st.secrets["tmdb_api_key"]

# Dropdown for selecting a movie title
movie_title = st.selectbox('Select a Movie', movies['title'])

# Retrieve the corresponding movie ID based on the selected title
selected_movie_id = movies.loc[movies['title'] == movie_title, 'movieId'].iloc[0]


if st.button('Show Recommendation'):
    recommended_movie_ids, recommended_titles, recommended_posters = recommend_movies(model, selected_movie_id, movies, links, api_key)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(recommended_titles[i])
            st.image(recommended_posters[i] if recommended_posters[i] else "https://via.placeholder.com/150")

