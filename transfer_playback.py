import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getpremtoken():
    url = "https://open.spotify.com/get_access_token?reason=transport&productType=web_player"

    payload={}
    headers = {
      'authority': 'open.spotify.com',
      'scheme': 'https',
      'path': '/get_access_token?reason=transport&productType=web_player',
      'cache-control': 'max-age=0',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'same-origin',
      'sec-fetch-dest': 'empty',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'en-US,en;q=0.9',
      'cookie': 'sp_adid=c811cb01-b03c-46d1-8242-f51084acf3cf; _ga_0KW7E1R008=GS1.1.1575216648.1.1.1575216855.0; sp_t=64fe879894e1cdb9a84c878731a27f1c; _fbp=fb.1.1590078875405.1976385900; sp_dc=AQCf2OZhttz9imbq4NOgA-PNzHcSKwKz4iH6AXStPE9wbfH59ZQYEvC7BsEcrD-FJlgDwRpGLouOwy06sWJIEUSkwzf8FdL2YjFfzZm2pY0; sp_key=fe0ca0b2-2720-456b-a99b-82a630ea39cf; optimizelyEndUserId=oeu1592656983958r0.7922028574886284; optimizelySegments=%7B%226174980032%22%3A%22search%22%2C%226176630028%22%3A%22none%22%2C%226179250069%22%3A%22false%22%2C%226161020302%22%3A%22gc%22%7D; optimizelyBuckets=%7B%7D; LPVID=Q3MTU0OTNhZjUyNDBjZDAy; _scid=268370b1-e7d6-499d-a4b5-cab9d47d13b2; _pin_unauth=dWlkPU9EVTBabUk0TWpndE5HWTBNeTAwWkdFM0xXRmhZakF0WTJJd01UaG1OalF3WWpSaA; ki_t=1590254409639%3B1604919421906%3B1604919709765%3B8%3B14; ki_r=aHR0cHM6Ly90LmNvLw%3D%3D; _ts_yjad=1606669492178; OptanonAlertBoxClosed=2020-12-09T09:42:49.911Z; _gaexp=GAX1.2.Bnkwt3kpQ3WEKyKXua5KQg.18706.1; _hjid=ecaa1140-da1d-4c91-ae0c-c3c41cc1f2c5; sp_last_utm=%7B%22utm_campaign%22%3A%22nav-upgrade%22%2C%22utm_medium%22%3A%22product-KM%22%2C%22utm_source%22%3A%22spotify%22%7D; sp_phash=09904ea376420d759e8f6fa16ec25ccdaec7ed11; sp_gaid=0088fc448b49eb3a5b8ccb373e50f5479e79ca4026a0ef02bbb06d; sp_m=es; spot=%7B%22t%22%3A1590240614%2C%22m%22%3A%22es%22%2C%22p%22%3Anull%7D; sss=1; _sctr=1|1610908200000; _derived_epik=dj0yJnU9bWdrZWZlWE1ZbHB0aVRtTkp2XzBpZEVOTTRQblZmZ3Qmbj1ycTBRTU56MlBlR3Y1VGZsNmQ0MVBRJm09MSZ0PUFBQUFBR0FGNHU0JnJtPTEmcnQ9QUFBQUFHQUY0dTQ; LPSID-2422064=BCbU2-PpSgmOoDECqp-MoQ; _ga_S35RN5WNT2=GS1.1.1611427141.21.0.1611427141.60; _ga=GA1.2.691895153.1575216648; OptanonConsent=isIABGlobal=false&datestamp=Fri+Feb+05+2021+10%3A09%3A13+GMT%2B0530+(India+Standard+Time)&version=6.12.0&hosts=&consentId=ad211c7b-0d27-42d5-a61b-e2acb991761b&interactionCount=1&landingPath=NotLandingPage&groups=t00%3A1%2Cs00%3A1%2Cf00%3A1%2Cm00%3A1%2Ci00%3A1&AwaitingReconsent=false&geolocation=IN%3BHR; sp_landing=https%3A%2F%2Fopen.spotify.com%2Fservice-worker.js.map; sp_landing=https%3A%2F%2Fopen.spotify.com%2Fget_access_token%3Freason%3Dtransport%26productType%3Dweb_player; sp_t=64fe879894e1cdb9a84c878731a27f1c'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    response = json.loads(response.text)
    prem_access = response['accessToken']
    return prem_access

def transferplayback():

    getpremtoken()
    premtoken = format(getpremtoken())
    print (premtoken)
    sp = spotipy.Spotify(auth=premtoken)
    device_id = "554d497b2fc24f614fccedaefee3da011ff1e981"
    sp.transfer_playback(device_id, force_play=False)


