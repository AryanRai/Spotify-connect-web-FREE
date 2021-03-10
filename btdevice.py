from bt_proximity import BluetoothRSSI
import time
import sys
from transfer_playback import *

#BT_ADDR = '20:A6:0C:B4:2B:61'  # You can put your Bluetooth address here


def print_usage():
    print(
        "Usage: python test_address.py <bluetooth-address> [number-of-requests]")


def detector(device_id, BT_ADDR, NUM_LOOP):
    avg = 0
    if len(sys.argv) > 1:
        addr = sys.argv[1]
    elif BT_ADDR:
        addr = BT_ADDR
    else:
        print_usage()
        return
    if len(sys.argv) == 3:
        num = int(sys.argv[2])
    else:
        num = NUM_LOOP
    btrssi = BluetoothRSSI(addr=addr)
    for i in range(0, num):
        #print (btrssi.request_rssi())
        a = str(btrssi.request_rssi()).replace(',', '').replace('(', '').replace(')', '')
       
       
        print (a)
       
        if a == "None":
            print("not in range")
           
       
        elif int(a) > 9:
            print ("aarush pagal hai")
            avg += 1
           
        elif int(a) < 9:
            print ("akki pagal hai")
            avg = 0    
           
        if avg >= 3:
            avg = 0
            print ("aarush and jasman pagal hai")
            transferplayback()
           
        time.sleep(0.25)

   
