import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

def authenticate_youtube():
    # Set up OAuth 2.0 credentials
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    client_secrets_file = "/spotify-to-youtube/src/client_secrets.json" 

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server(port=0)

    # Create a YouTube Data API client
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
    
    return youtube

def playlist_youtube(song_artist_list):
    playlist_id = input("Enter the playlist ID: ")
    youtube = authenticate_youtube()
    search_and_add_to_playlist_youtube(youtube, song_artist_list, playlist_id)


def search_and_add_to_playlist_youtube(youtube, song_artist_list, playlist_id):
    # Iterate over the list of songs
    for song_name in song_artist_list:
        # Search for the song on YouTube
        search_response = youtube.search().list(
            q=song_name,
            part="snippet",
            maxResults=1
        ).execute()

        # Get the video ID of the first (and only) result
        video_id = search_response['items'][0]['id']['videoId']

        # Fetch the playlist items
        playlist_items = youtube.playlistItems().list(
            part="snippet",
            maxResults=50,  # Fetch up to 50 items, adjust as needed
            playlistId=playlist_id
        ).execute()

        # Get the video IDs of the playlist items
        playlist_video_ids = [item['snippet']['resourceId']['videoId'] for item in playlist_items['items']]

        # Check if the video is already in the playlist
        if video_id in playlist_video_ids:
            print(f"'{song_name}' is already in the playlist")
        else:
            # Add the video to the playlist
            youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist_id,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": video_id
                        }
                    }
                }
            ).execute()