def recommend_anime(df, preferred_genres, top_n=10):
    """
    Recommend top N anime based on user-selected genres.
    """
    # Filter the dataset by selected genres
    filtered_df = df[df['genre'].apply(lambda genres: any(genre in genres for genre in preferred_genres))]
    
    # Return the top N anime based on rating
    return filtered_df.nlargest(top_n, 'rating')[['name', 'rating', 'genre']]
