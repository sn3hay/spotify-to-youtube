# Project Name
Spotify to Youtube

## Description

A python project that converts your spotify playlists into Youtube Playlists. These converted playlists also show up in the Youtube Music app.

## Installation

This project requires the following libraries:

- requests
- spotipy
- python-dotenv
- google_auth_oauthlib
- googleapiclient


To install these libraries, you can use pip:

```bash
pip install requests
pip install spotipy
pip install python-dotenv
pip install google-auth-oauthlib
pip install google-api-python-client

## Requirements for Authentication
The .env file should be placed at the root of the src folder with three varibales defined in it:
SPOTIFY_CLIENT_ID=''
SPOTIFY_CLIENT_SECRET=''
SPOTIFY_REDIRECT_URI= ''

The client_secrets.json contains the API key from youtube required for Google OAuth.
