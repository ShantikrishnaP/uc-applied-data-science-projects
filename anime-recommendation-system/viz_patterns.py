import plotly.express as px

def plot_genre_bar_chart(df):
    """
    Create an interactive vertical bar chart for genre popularity with violet color.
    """
    # Split genres and count occurrences
    genre_counts = df['genre'].str.split(', ').explode().value_counts()
    
    # Create an interactive vertical bar chart with violet color
    fig = px.bar(
        x=genre_counts.index, 
        y=genre_counts.values, 
        labels={'x': 'Genres', 'y': 'Count'},
        title='Genre Popularity',
        height=600,
        color_discrete_sequence=['#8A2BE2']  # Violet color for bars
    )
    
    # Custom layout
    fig.update_layout(
        plot_bgcolor='rgba(255,255,255,0)',  # White background for the plot
        paper_bgcolor='rgba(255,255,255,0)', # White background outside the plot
        xaxis_title="Genres",
        yaxis_title="Count",
        xaxis_tickangle=-45,
        showlegend=False,
        font=dict(
            family="Montserrat, Playfair Display",  # Custom font for the graph text
            size=14,
            color="#8A2BE2"  # Violet font color for the graph
        )
    )
    
    return fig
