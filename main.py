from __future__ import unicode_literals
import spotipy
from spt_auth import *
from yt_auth import *
import youtube_dl
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '0'



#search YT for song name + artist, return video ID
def youtube_search_query(client, query, limit=1):
  response = client.search().list(
    part="snippet",
    q=query,
    maxResults=limit,
    type="video").execute()
  return response

#heavy lifter
def find_tunes(yt, sp, user=SPT_USERNAME, playlist_id=SPT_PL):
  x = 0
  tracklist = sp.user_playlist_tracks(user=SPT_USERNAME, playlist_id=SPT_PL)
  while tracklist:
    for tracks in tracklist['items']:
      x += 1
      try:
        #todo collect more metadata
        artist = tracks['track']['artists'][0]['name']
        track_title = tracks['track']['name']
        album = tracks['track']['album']['name']
        
        print('{0:4d}. {1:5s} -- {2:6s}'.format(x, artist, track_title))

        yt_result = youtube_search_query(client=yt, query=(artist + track_title))
        yt_id = yt_result['items'][0]['id']['videoId']
        yt_url = 'https://www.youtube.com/watch?v=' + yt_id

        print(' '*8 + '--' + yt_url)

        download_tunes(yt_url)

      except Exception as e:
        print(' '*8 + '--' + str(e))
        print(' '*8 + '--' + 'something went wrong here... moving on')
    
    #pagination
    if tracklist['next']:
      tracklist = sp.next(tracklist)
    
    #end of playlist
    else:
      tracklist = None
  
  return "Congratulations, we are done here!"




#both of these to be replaced with shell commands
def my_hook(d):
  if d['status'] == 'finished':
    print(' '*8 + '--' + 'Done downloading, now converting ...')

def download_tunes(url):
  ydl_opts = {
      'format': 'bestaudio/best',
      'quiet': True,
      'sleep_interval': 10,
      'max_sleep_interval': 30,
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '320',
      }],
      'progress_hooks': [my_hook],
  }

  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download([url])


#make it all run
YouTube = auth_youtube()
Spotify = auth_spotify()

find_tunes(yt=YouTube, sp=Spotify)

