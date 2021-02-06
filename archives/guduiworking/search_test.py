import webbrowser, os, sys




import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
search = input('search?')


#sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="4c38a534539b4510b8bdc79b4ec86f00",
                                                           #client_secret="2db41f2ee49c49af84d018dc1b744e17"))

token = "BQBTYm_K9XfliSMZhuSmt4JyL8igqW9SaBIYN-JYdsypAaPS7jgcvb2iqEp7pw1-T3WweooBwR3sLyQSz_yaWSpYxAr2yN8Lq-_HM_B4If1zkEinA7hEmGs9pRpXrxFQGzBgC-m3NX2uo35jxdc_qMP0rNB8D7OqpnSaJHxJDDmhTl9gU5MLFzdPPztJ4QR4LNSZsMYBEKIO-BERjgTx0Vf920DBREWMBN5gs1F2dNOijsGQdV9PaRlAvrY0behmk6W8kL75b4CBP1r0rbNuji3Wf0YBgcmClCM4D2SdwpfuHx_ZA2A"
sp = spotipy.Spotify(auth=token)

results = sp.search(q=search)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['uri'])
uri = track['uri'] 
url = uri.replace(':', '/')
url = url.replace('spotify', 'open.spotify.com')
print (url)
device_id = "554d497b2fc24f614fccedaefee3da011ff1e981"
sp.transfer_playback(device_id, force_play=True)
#button = driver.find_element_by_name("Connect to a device")
#button.click()


#https://open.spotify.com/track/3eekarcy7kvN4yt5ZFzltW

