import streamlit as st
from process_data import load_data
from recommendation_logic import recommend_anime
from viz_patterns import plot_genre_bar_chart

# Set page configuration for wide layout
st.set_page_config(page_title="Anime Recommendation System", layout="wide")

# Custom CSS styling for the white background, violet title, and title font
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Playfair+Display:wght@700&display=swap');

    body {
        background-color: white;
        color: black;
    }
    .reportview-container {
        background-color: white;
        color: black;
    }
    h1 {
        color: #8A2BE2;  /* Violet color for the title */
        font-family: 'Montserrat', sans-serif;  /* Use Google Font: Montserrat for title */
        font-size: 40px;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the dataset
df = load_data('anime.csv')  # Adjust file path as needed

# Streamlit app UI with violet title
st.title("🎬 Anime Recommendation System 🎬")

# Allow users to select their preferred genres
all_genres = df['genre'].str.split(', ').explode().unique()
preferred_genres = st.multiselect('Select your preferred genres', all_genres)

# Show genre popularity bar chart
if st.checkbox('Show Genre Popularity'):
    fig = plot_genre_bar_chart(df)
    st.plotly_chart(fig)

# Recommend anime based on user preferences
if st.button('Get Recommendations'):
    if preferred_genres:
        recommendations = recommend_anime(df, preferred_genres)
        st.write(recommendations[['name', 'genre', 'rating']])
    else:
        st.write("Please select at least one genre.")
