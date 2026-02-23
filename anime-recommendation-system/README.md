# Anime Recommendation System

## Overview
A hybrid genre-based anime recommendation system built using Python and deployed with Streamlit.

The system allows users to select preferred genres and receive top-rated anime recommendations based on filtering logic.

## Features
- Genre-based filtering
- Top-N recommendation logic
- Interactive Streamlit GUI
- Genre popularity visualization using Plotly

## Tech Stack
- Python
- Streamlit
- Pandas
- Plotly

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the app:
   streamlit run app.py

## Project Structure
- app.py (Streamlit frontend)
- process_data.py (Data cleaning & preprocessing)
- recommendation_logic.py (Recommendation engine)
- viz_patterns.py (Visualization module)
- anime.csv (Dataset)
