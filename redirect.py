from flask import Flask, render_template, request
import webbrowser

app = Flask(__name__)

token = "abc"


    
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=["GET", "POST"])
def shutdown():
    
    shutdown_server()
    return 'Server shutting down...'

        
@app.route('/spotify', methods =["GET", "POST"]) 
def gfg(): 
    global token
    token = request.form.get("token") 
    print(token)
    
    
        
    if request.method == "POST": 
        return render_template("shutdown.html")
      
                     
    else:
        return render_template("create_token.html")

    

if __name__ == '__main__':
    app.run(debug=False, host='localhost')


print(token)
f= open("token.txt","w+")
f.write(token)
f.close()
player = 'file:///C:/Users/aryan/Desktop/spotipy/spotify_web_sdk.html'
url = player + "#" + token
webbrowser.register('chrome',
        None,
webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open(url)

