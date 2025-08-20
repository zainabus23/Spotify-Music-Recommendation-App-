Project Title - Spotiy Music Recommendation based on Clustered Audio Features 

## Description 
The aim of this project is to design a Streamlit web interface to recommend similar song to a spotify track based on identified clustered audio features. 
## Features 
- Enter a Spotify ID from the "songs.csv" file to get similar song from the same audio cluster.
- Features is built on Streamlit web interface

## Dataset and model 
Dataset
`songs.csv`: Contains song metadata, audio features, cluster labels, genre, mood, and popularity scores.
"data.csv"
"data_by_genres_
Model
`song_cluster_pipeline2.pkl`: A pre-trained clustering pipeline using KMEANS based on audio features like 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', and 'valence etc.

## Installing
- Stremlit, pandas, scikit-learn, joblib
- Visualization- matplotlib and seaborn ( you can use plotly express for better interactivity) 

## Executing program 
Phase 1 and 2 - Read and explore dataset
Read Spotify datasets to explore structure. Datasets used include aritists data, genres dataset - (see music.step2.ipynb file)

Phase 3
Clustering Phase : Here, i used K-Means clustering techniques to group audio based on their features. The features in the datasets include 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', and 'valence

Phase 4
- use joblib to create pretrained model: `song_cluster_pipeline2.pkl`

Phase 5 - Create app.py 
- load pretrained model and dataset
- define code to extract features for track
- define code to recommend songs from same cluster
- initiate streamlit interface to display title and input box to enter a Spotify track ID (you can find this in the songs.csv)
- define code to dispolay recommendation


