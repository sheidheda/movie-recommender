import requests
from sklearn.metrics.pairwise import cosine_similarity

# Function to get movie factors from the SVD model
def get_movie_factors(svd_model, movie_id):
    movie_inner_id = svd_model.trainset.to_inner_iid(movie_id)
    return svd_model.qi[movie_inner_id]

# Function to compute similarity between movies
def compute_similarities(svd_model, selected_movie_factors):
    all_factors = svd_model.qi
    similarities = cosine_similarity([selected_movie_factors], all_factors).flatten()
    movie_ids = [svd_model.trainset.to_raw_iid(i) for i in range(len(all_factors))]
    return list(zip(movie_ids, similarities))

# Function to get movie title from movie ID
def get_movie_title(movie_id, movies_df):
    try:
        title = movies_df.loc[movies_df['movieId'] == movie_id, 'title'].iloc[0]
        return title
    except IndexError:
        return f"Movie with ID {movie_id} not found"

# Function to get TMDb ID from movie ID using links DataFrame
def get_tmdb_id(movie_id, links_df):
    try:
        tmdb_id = links_df.loc[links_df['movieId'] == movie_id, 'tmdbId'].iloc[0]
        return tmdb_id
    except IndexError:
        return None

# Function to get movie details from TMDb
def get_movie_details(tmdb_id, api_key):
    url = f'https://api.themoviedb.org/3/movie/{tmdb_id}'
    params = {
        'api_key': api_key,
        'language': 'en-US'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching TMDb details for ID {tmdb_id}: {e}")
        return None

# Function to get poster URL from TMDb ID
def get_poster_url(tmdb_id, api_key):
    movie_details = get_movie_details(tmdb_id, api_key)
    if movie_details:
        poster_path = movie_details.get('poster_path')
        if poster_path:
            return f'https://image.tmdb.org/t/p/original/{poster_path}'
    return None

# Function to recommend movies
def recommend_movies(svd_model, selected_movie_id, movies_df, links_df, api_key):
    selected_movie_title = get_movie_title(selected_movie_id, movies_df)
    
    if not selected_movie_title:
        return [], [], []  # Return empty recommendations if selected movie ID is not found
    
    selected_movie_factors = get_movie_factors(svd_model, selected_movie_id)
    similarities = compute_similarities(svd_model, selected_movie_factors)
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    top_5_recommendations = [movie_id for movie_id, _ in similarities[1:6]]  # Exclude the selected movie
    
    # Get movie titles and posters for recommendations
    top_5_titles = [get_movie_title(movie_id, movies_df) for movie_id in top_5_recommendations]
    top_5_posters = [get_poster_url(get_tmdb_id(movie_id, links_df), api_key) for movie_id in top_5_recommendations]
    
    return top_5_recommendations, top_5_titles, top_5_posters
