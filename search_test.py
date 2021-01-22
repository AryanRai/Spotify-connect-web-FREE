import webbrowser, os, sys



import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
search = input('search?')



sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="4c38a534539b4510b8bdc79b4ec86f00",
                                                           client_secret="2db41f2ee49c49af84d018dc1b744e17"))




results = sp.search(q=search, limit=1)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['uri'])
uri = track['uri'] 
url = uri.replace(':', '/')
url = url.replace('spotify', 'open.spotify.com')
print (url)



#https://open.spotify.com/track/3eekarcy7kvN4yt5ZFzltW

