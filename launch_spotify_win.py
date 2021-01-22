import webbrowser
global token
global player
global url

def launch():
    f=open("token.txt", "r")
    token =f.read()
    player = 'file:///C:/Users/aryan/Desktop/spotipy/spotify_web_sdk.html'
    url = player + "#" + token


    webbrowser.register('chrome',
            None,
    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)

   


        
	
        





