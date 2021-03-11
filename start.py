import eel
from settings import *
#from btdevice import *

device_id = "none"

eel.init('web')

#@eel.expose
#def get_device_id(spotify_id):
    #device_id = spotify_id
    #print(device_id)

def my_other_thread():
    while True:
        print("I'm a thread")
        if device_id != "none":
            detector(device_id, BT_ADDR, 4)
        eel.sleep(0.1)
        
        #if int(input()) > 0:
            #eel.nowplaying()        # Use eel.sleep(), not time.sleep()

eel.spawn(my_other_thread)


eel.start('start/start.html', block=False)
while True:
    print("I'm a main loop")
    eel.sleep(0.1)
    



