from bt_proximity import BluetoothRSSI
import time
import sys

BT_ADDR = '20:A6:0C:B4:2B:61'  # You can put your Bluetooth address here
NUM_LOOP = 100


def print_usage():
    print(
        "Usage: python test_address.py <bluetooth-address> [number-of-requests]")


def main():
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
        if int(a) > 9:
            print ("aarush pagal hai")
        time.sleep(1)

   
   

if __name__ == '__main__':
    main()
