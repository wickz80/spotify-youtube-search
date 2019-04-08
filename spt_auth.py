from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

SPT_CLIENT_SECRET = ""
SPT_CLIENT_ID = ""
SPT_USERNAME = ""

#playlist ID
SPT_PL = ""


#auth to spotify
def auth_spotify():
  client_credentials_manager = SpotifyClientCredentials(
    client_id=SPT_CLIENT_ID, 
    client_secret=SPT_CLIENT_SECRET
  )
  return spotipy.Spotify(
    client_credentials_manager=client_credentials_manager
  )