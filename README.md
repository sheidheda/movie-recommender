# Movie Recommender System

This is a movie recommender system built using the ML 100K dataset, Singular Value Decomposition (SVD), and Streamlit. It provides personalized movie recommendations based on user preferences and similarity between movies.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Personalized Recommendations**: Uses SVD to analyze user-item interactions and recommend movies based on similar users' preferences.
- **Interactive Interface**: Built with Streamlit, providing a user-friendly web interface for selecting movies and viewing recommendations.
- **Movie Details**: Fetches movie details and poster images from TMDb API to enhance user experience.

## Technologies Used

- **Python**: Programming language used for backend development.
- **Pandas**: Data manipulation library used for handling dataset operations.
- **Surprise**: Python scikit for building and analyzing recommender systems.
- **Streamlit**: Open-source app framework used to build interactive web applications.
- **TMDb API**: Used to fetch movie details and poster images.

## Dataset

The system is based on the [MovieLens 100K dataset](https://grouplens.org/datasets/movielens/100k/), which contains movie ratings by users.

## Setup Instructions

1. **Clone the Repository**

   git clone https://github.com/your-repo-name.git
   cd movie-recommender

2. **Install Dependencies**

Ensure you have Python 3.7+ installed. Install the required Python packages:

    pip install -r requirements.txt

3. **Run the Application**

Start the Streamlit app:

    streamlit run app.py

4. **Provide TMDb API Key**

You need to obtain an API key from TMDb to fetch movie details and posters. Save your API key as an environment variable named TMDB_API_KEY.

export TMDB_API_KEY="your-api-key"
Alternatively, you can set it in a .env file and use a library like python-dotenv to load it.

5. **Access the Application**

Open your web browser and go to http://localhost:8501 to access the movie recommender system.

## Usage
-**Select a Movie:** Choose a movie from the dropdown list.
-**Get Recommendations:** Click the "Show Recommendation" button to view top 5 recommended movies based on your selection.
-**View Details:** Movie titles and poster images will be displayed for the recommended movies.

## Contributing
Contributions are welcome! If you have any suggestions, feature requests, or want to report issues, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


### Explanation:

- **Table of Contents**: Provides easy navigation to different sections of the README.
- **Features**: Describes the main features of your application.
- **Technologies Used**: Lists the technologies and libraries utilized.
- **Dataset**: Mentions the dataset used in the recommender system.
- **Setup Instructions**: Provides steps to clone, install dependencies, configure API keys, and run the application.
- **Usage**: Explains how to interact with the recommender system.
- **Contributing**: Offers guidelines for contributing to the project.
- **License**: States the licensing information for the project.

Feel free to customize the sections and details according to your specific project setup and requirements. This README.md template will help users understand, set up, and use your movie recommender system effectively.