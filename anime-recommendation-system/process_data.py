import pandas as pd

def load_data(file_path):
    """
    Load and clean the anime dataset from the specified file path.
    """
    df = pd.read_csv(file_path)
    
    # Clean the data (e.g., handle missing values)
    df.dropna(subset=['genre'], inplace=True)
    df.fillna({'rating': 0, 'episodes': 'Unknown'}, inplace=True)  # Fill missing ratings and unknown episodes
    
    return df

def filter_data_by_genre(df, preferred_genres):
    """
    Filter the dataset to only include anime that match the user's preferred genres.
    """
    genre_filter = df['genre'].str.contains('|'.join(preferred_genres))
    return df[genre_filter]
