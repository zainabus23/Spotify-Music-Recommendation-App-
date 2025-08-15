import streamlit as st
import joblib
import pandas as pd

# Load your cluster pipeline and dataset
cluster_pipeline = joblib.load('song_cluster_pipeline2.pkl')
df = pd.read_csv("songs.csv")  # Load your dataset with song features and clusters

def get_song_features_from_dataset(track_id, df):
    song_row = df[df['id'] == track_id]
    if not song_row.empty:
        return song_row.iloc[0].to_dict()
    return None

# Function to recommend songs
def recommend_songs(track_id, cluster_pipeline, df):
    song_features = get_song_features_from_dataset(track_id, df)
    if song_features is None:
        return None

    # Find songs in the same cluster
    cluster_label = song_features['cluster_label']
    recommended_songs = df[df['cluster_label'] == cluster_label]
    return recommended_songs[['name', 'artists']].head(10)

# Streamlit app interface
st.title('Spotify Song Recommendation System')
st.write('Enter a Spotify Track ID to get song recommendations.')

track_id = st.text_input('Enter Spotify Track ID')

if track_id:
    recommended_songs = recommend_songs(track_id, cluster_pipeline, df)
    if recommended_songs is not None and not recommended_songs.empty:
        st.write(f"Recommended songs for track {track_id}:")
        st.dataframe(recommended_songs)
    else:
        st.write("No recommendations found. Try a different track ID.")