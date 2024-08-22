# Movie Recommender System

This is a simple movie recommender system built using Python, Flask, and scikit-learn. The system recommends similar movies based on user input using cosine similarity on movie tags derived from genre and overview.

## Features

- User-friendly web interface for inputting movie titles and receiving recommendations.
- Recommends similar movies based on the input movie title.
- Utilizes cosine similarity to find similarity between movies.
- Basic CSS styling for the web interface.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/movie-recommender-system.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Place your movie dataset in CSV format as `Movies_dataset.csv` in the project directory.

## Dataset

The movie dataset used for this project should be provided in CSV format with the following columns:

- `title`: Movie title
- `genre`: Movie genre
- `overview`: Movie overview

## Data Preprocessing

The preprocessing steps include:

1. Filling missing values in the 'genre' and 'overview' columns with the most frequent value (mode).
2. Combining 'genre' and 'overview' into a single 'tags' column.
3. Converting all text to lowercase to ensure uniformity.

## Recommendation Algorithm

1. **Text Vectorization**: The 'tags' column is converted into a matrix of token counts using `CountVectorizer` from scikit-learn.
2. **Cosine Similarity**: Cosine similarity is computed between the vectors to measure the similarity between movies.
3. **Recommendation**: For a given movie title, the system retrieves and sorts the movies based on similarity scores and returns the top recommendations.

## Usage

1. Run the Flask app:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://localhost:5000` to access the movie recommender system.

3. Enter a movie title and click "Recommend" to receive similar movie recommendations.

## Customization

- **Changing the Number of Recommendations**: The number of recommended movies can be adjusted in the `recommend` function in `app.py`.
- **Styling**: Customize the CSS in `static/styles.css` to change the appearance of the web interface.
- **Improving the Model**: You can improve the recommendation model by experimenting with different text vectorization methods or similarity measures.

