import requests
from urllib.parse import urlparse, parse_qs
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
from youtube_api import playlist_youtube

# Load environment variables from .env file
load_dotenv()

# Get your Client ID, Client Secret, and Redirect URI from environment variables
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')

# Define the scope of access
scope = 'user-library-read'

# Use the SpotifyOAuth object to get an access token
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# Step 3: Make a request to the Spotify API
# Step 3.1: Take input
url = input("Enter the Spotify playlist URL: ")

# Step 3.2: Extract playlist ID
parsed_url = urlparse(url)
playlist_id = parsed_url.path.split('/')[-1]

try:
    playlist = sp.playlist(playlist_id)
except spotipy.exceptions.SpotifyException as e:
    print(f"Failed to fetch playlist details: {e}")
else:
    # Step 4: Print the details of the playlist
    print(f"Playlist Name: {playlist['name']}")
    print(f"Description: {playlist['description']}")
    print(f"Total Tracks: {playlist['tracks']['total']}")
    
    # Fetch the list of songs and their artists
    for item in playlist['tracks']['items']:
        track = item['track']
        song = track['name']
        artists = [artist['name'] for artist in track['artists']]
        print(f"Song: {song}, Artists: {', '.join(artists)}")
        print(f"Year", track['album']['release_date'][:4])

# Initialize an empty list to store song details
song_artist_list = []

# Fetch the list of songs and their artists
for item in playlist['tracks']['items']:
    track = item['track']
    song = track['name']
    artists = [artist['name'] for artist in track['artists']]
    
    # Concatenate song name and artist names and append to the list
    song_artist_list.append(f"{song} - {', '.join(artists)}")

# Now song_artist_list contains the song name concatenated with the artist name for each song
if song_artist_list:
    playlist_youtube(song_artist_list)
