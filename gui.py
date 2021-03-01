import eel

eel.init('web')

def my_other_thread():
    while True:
        print("I'm a thread")
        eel.sleep(1.0)
        if int(input()) > 0:
            eel.nowplaying() 

eel.spawn(my_other_thread)
eel.start('')
