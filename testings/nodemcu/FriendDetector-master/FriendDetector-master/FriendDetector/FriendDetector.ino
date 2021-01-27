/* 
Friend Detector by Ricardo Oliveira, forked by Skickar 9/30/2018

A Node MCU microcontroller + mini bread board + 4 pin RGB LED to detect when devices belonging to a target are nearby.


The function of this code is to read nearby Wi-Fi traffic in the form of packets. These packets are compared
to a list of MAC addresses we wish to track, and if the MAC address of a packet matches one on the list, we turn 
on a colored LED that is linked to the user owning the device. For example, when my roommate comes home, the 
transmissions from his phone will be detected and cause the blue LED to turn on until his phone is no longer detected. 
It can detect more than one phone at a time, meaning if my phone (red) and my roommate's phone (blue) are both home, 
the LED will show purple. */

#include "./esppl_functions.h"

/*  Define you friend's list size here
 How many MAC addresses are you tracking?
 */
#define LIST_SIZE 2
/*
 * This is your friend's MAC address list
 Format it by taking the mac address aa:bb:cc:dd:ee:ff 
 and converting it to 0xaa,0xbb,0xcc,0xdd,0xee,0xff
 */
uint8_t friendmac[LIST_SIZE][ESPPL_MAC_LEN] = {
   {0x4A, 0xFE, 0xA2, 0xE8, 0x09, 0xA1}
  ,{0x20, 0xA6, 0x0C, 0xB4, 0x2B, 0x62}
  };
/*
 * This is your friend's name list
 * put them in the same order as the MAC addresses
 */
String friendname[LIST_SIZE] = {
   "Target 1"
  ,"Target 2"
  };

// start variables package - Skickar 2018 hardware LED for NodeMCU on mini breadboard //
void setup() { 
  delay(500);
  pinMode(D5, OUTPUT); // sets the pins to output mode
  pinMode(D6, OUTPUT);
  pinMode(D7, OUTPUT);
  Serial.begin(115200);
  esppl_init(cb);
}

/* You cannot use a time delay here to keep the LED on, so will need to use ratio of 
detected packets to overall packets to keep LED on for longer. If you try to use a 
delay to keep the light on for long enough to be useful, the watchdog timer kills the 
process and it dies */
int cooldown = 0; /* This variable will be a cooldown timer to keep the LED on for longer, we'll set it to 1000 if we
detect a packet from a device with a MAC address on the list, and then keep the LED on till we get 1000 packets that 
are NOT from any device on the list. */
void red() {
digitalWrite(D5, HIGH);
Serial.println("red"); 
}  // Turn ON the red LED
void blue() {
digitalWrite(D7, HIGH);
Serial.println("blue"); 
} // Turn ON the blue LED
void green() {
digitalWrite(D6, HIGH); 
Serial.println("green");
} // Turn ON the green LED
void turnoff() {
    digitalWrite(D7, LOW), digitalWrite(D5, LOW), digitalWrite(D6, LOW); 
}

/* end exparimental variable package */

bool maccmp(uint8_t *mac1, uint8_t *mac2) {
  for (int i=0; i < ESPPL_MAC_LEN; i++) {
    if (mac1[i] != mac2[i]) {
      return false;
    }
  }
  return true;
}

void cb(esppl_frame_info *info) {
  for (int i=0; i<LIST_SIZE; i++) {
    Serial.print(i);
    if (maccmp(info->sourceaddr, friendmac[i]) || maccmp(info->receiveraddr, friendmac[i])) {
      Serial.printf("\n%s is here! :)", friendname[i].c_str());
      
      cooldown = 500; // here we set it to 1000 if we detect a packet that matches our list
      if (i == 1){
        blue();} // Here we turn on the blue LED until turnoff() is called
        else {
          red();} // Here we turn on the RED LED until turnoff is called. We can also use if i == 0, or another index
    }

      else { // this is for if the packet does not match any we are tracking
        if (cooldown > 0) {
          cooldown--; } //subtract one from the cooldown timer if the value of "cooldown" is more than one
          else { // If the timer is at zero, then run the turnoff function to turn off any LED's that are on.
        
        turnoff(); } } } }


void loop() { // I didn't write this part but it sure looks fancy.
  esppl_sniffing_start();
  while (true) {
    for (int i = ESPPL_CHANNEL_MIN; i <= ESPPL_CHANNEL_MAX; i++ ) {
      esppl_set_channel(i);
      while (esppl_process_frames()) {
        //
      }
    }
  }  
}
