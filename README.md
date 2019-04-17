# spotify-youtubeSearch
This python project uses Spotify (via Spotipy) and YouTube APIs to find and download ID3-tagged MP3 files from a spotify playlist, or list of songs.

It is not for use with copyrighted material.  

# workflow

1.  Set up auth to YT and Spotify using OAuth2
2.  Takes a Spotify Playlist ID and pings spotify for song information
3.  Keeps track of Artist, Track name, and Album
4.  For each song, search YouTube for associated videos and pick the top match
5.  Create a urls.txt file with the video link and metadata information for each song
6.  Call youtube-dl.exe (ffmpeg) to download the video as a MP3 file, and feed it the metadata so it tags the MP3's ID3 information

# Usage

First, populate spt_auth.py and yt_auth.py with your app key/secret and account credentials.

Then, fill out songs.txt with a list of track names you'd like.  You can also modify main.py to comb through a playlist instead:

`find_tunes(yt=YouTube, sp=Spotify)`

`find_tunes(yt=YouTube, sp=Spotify, playlist_id=MY_PLAYLIST_ID)`

To run the script:

`cd myDirectory\spotify-youtube-searcher\`

`python main.py`