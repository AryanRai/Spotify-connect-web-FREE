# Spotify-connect-web-FREE

BACKGROUND
so as a Spotify user I wanted to use Spotify WITH 
MUSIC STREAMING on my raspi which had Gassistpi 
Running on it with magic mirror. Here comes the 
Problem. My Spotify premium expired AND SPOTIFY 
DOES ALLOW U TO USE THE CONNECT API FOR FREE USERS 
AND I KNOW WHY NOT JUST BUY IT AGAIN? BECAUSE I 
CANT. U THINK IF I COULD HAV WHY WIULD I MADE THIS 
THING EVER. so I went searching for my options.

OPTIONS
1.MAYBE USE THE SPOTIFY WEB PLAY
(JESUS SPOTIFY HATES ME) BASICALLY THERE IS A 
THING CALLED DRM CONTENT. ONLY AVAILABLE IN
'compatible' browsers WARNING IT IS NOT AVAILABLE 
ON CHROMIUM ON RASPI.

I am a stubborn person so I used this command to 
Install chromium media edition on raspi



Now Spotify works great
You can use this as the eze way if u wanna use 
Your pi as a Spotify connect client and don't wanna
Control it or play it via python or using a script
USE THIS FIR MANUAL JUST USING AS A CONNECT CLIENT.

2.
NOW COMES THE PART WHERE I HAV NO OPTION BUT TO 
DO SOME CODING.
DAMN U SPOTIFY.
NO OFFENSE.
ILY2 SPOTIFY.


NORMAL PEOPLE TO ONLY READ THIS PART *************

THIS CODE USING THE SPOTIFY WEB PLAYBACK SDK TO LOGIN AND 
STREAM MUSIC USING YOUR BROWSER FROM YOUR SPOTIFY 
ACC. IT CREATES A SPOTIFY CONNECT INSTANCE AND 
EVERYTHING ON A FREE SPOTIFY ACCOUNT YAY PROBLEM
SOLVED

**************************************************
NO SPOTIFY STILL HATES ME AND ALL ITS FREE USERS 

PLEASE MAKE THE CONNECT API AVAILABLE TO FREE USERS 
SPOTIFY PLEEASE

so problem 2.
Web playback SDK doesn't allow u to start or play 
From a url/ uri ( meaning u need to choose what 
U want to play from another device or use the 
Connect api( WHICH AGAIN IS PAID!!)

JESUS
NORMAL PEOPLE TO START READING FROM HERE AGAIN****
MY SOLUTION***************
I REVERSE ENGINEERED THE SPOTIFY WEB APP LOL
JOKES ON U SPOTIFY....
I GOT THE URL IF HOW IT GETS ITS REFRESH TOKEN USED
IN THE WEB APP AND USING THAT TOKEN IT ALLOWS U TO
USE CONNECT API AND DIESNT RETURN 403 forbidden.
Sooo yeah .......
You're welcome.
