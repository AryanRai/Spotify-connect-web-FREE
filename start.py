import eel

eel.init('web')

def my_other_thread():
    while True:
        print("I'm a thread")
        eel.sleep(1)
        if int(input()) > 0:
            eel.nowplaying()        # Use eel.sleep(), not time.sleep()

#eel.spawn(my_other_thread)

#eel.nowplaying()

eel.start('start/start.html', block=False)
while True:
    print("I'm a main loop")
    eel.sleep(1)

    



