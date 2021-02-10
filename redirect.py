from flask import Flask, render_template, request
import webbrowser, os, sys

app = Flask(__name__)

authcode = "abc"


   
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
    global authcode
    authcode = request.form.get("authcode")
    print(authcode)
   
   
       
    if request.method == "POST":
        return render_template("shutdown.html")
     
                     
    else:
        return render_template("create_code.html")

   

if __name__ == '__main__':
    app.run(debug=False, host='localhost')


print(authcode)
#f= open("authcode.txt","w+")
#f.write(authcode)
#f.close()
player = 'file:///home/pi/Spotify-connect-web-FREE/spotify_web_sdk.html'
url = player + "#" + authcode

chrome_path = '/usr/lib/chromium-browser/chromium-browser'
webbrowser.get(chrome_path).open(url)
