# Portable Hacking Station
A portable hacking station with the purpose of penetrating and taking control over cyber-physical systems

# Presented use case
The below device is able to be used for any cyberphysical system prone to wpa/wpa2 network attacks. This github repository presents attack methods specifically for Tello Edu drone manufactured by DJI partner Ryze.

# Hardware Used
1) Raspberry Pi 1 B+
2) PiJuice External Battery
3) RTL8188eu wifi card (used for connecting to drones, and connecting drones together)
4) RTL8812au wifi card (used for packet injection)
5) External keyboard
6) External screen with capactive touch

# Hardware Setup
1) Mounting Kali Linux
* Get the version of kali linux for you respective raspberry pi model. 
  * Download links for kalipi available here: https://www.kali.org/get-kali/#kali-arm 
* Mount the downloaded image to a formated sd card of your choosing.
  * If you don't already have an sd card etcher downloaded I personally reccomend Balena.
  * Download links for balena available here: https://www.balena.io/etcher/
2) Setting up kalipi environment 
* Once your sd card is plugged in the raspberry pi will run its course for the installation, at this point ensure that you are plugged into an ethernet port to do so. 
  * kali is the default password and username once installed, for the purpose of this readme those shall remain unchanged. However, in accordance to good security practices please customize those. You wanna be the hacker, not the hacked!
* Once your kali linux environment has installed on the raspberry pi its time to install the neccesary hardware drivers

# Required Firmware for Hardware
1) PiJuice Firmware
* The PiJuice firmware described as per their respective tutorial functions properly and should just be followed. 
3) RTL8188eu (managed mode wifi card)
* The first step to getting the RTL8188eu to work on the portable hacking station is dowloading them from this github repository: https://github.com/drygdryg/rtl8188eus
* Once downloaded there are a couple extra required steps for it to function properly.
  * Step 1: Blacklist an already pre-installed kali linux driver. You can do this using the below command.
 ```
 echo 'blacklist r8188eu'|sudo tee -a '/etc/modprobe.d/realtek.conf'
 ```
  * Step 2: Using this issue solution: https://github.com/aircrack-ng/rtl8188eus/issues/156 replace the code in your the github library as specified 
  * Step 3: Compile either using docker or on the raspberry, be warned compiling on the machine will take a long amount of time. As well it is not enough to simply make && make install. Due to certain deprecated assets still being part of the kali raspberry pi image make must be done in the way specified below.
```
make CC=gcc-10
```
4) RTL8812au (monitor mode wifi card)
* The RTL8812au drivers come pre-installed and work as prescribed with no issues as of the latest commit. 
6) Bluetooth transmitter
7) 7 inch screen with capactive touch
*No firmware is required the capacitive touch screen attached 

# Libraries Used
1) Tello SDK 2.0
3) aircrack-ng

# Python Libraries Required
1) keyboard
# Cracking Scripts
1) crack.py
2) connect.py
3) crackNconnect.py

# Example Attack Scripts
1) telloLand.py
2) telloPilot.py
3) telloSmash.py

# Tello Pilot Commands
This online course will walk you through using Python to program your Tello drone for autonomous flight. As of 4/1/18 the commands supported by Tello are:

command
takeoff
land
up xx (fly up a distance from 20 - 500 cm)
down xx (fly down a distance from 20 - 500 cm)
left xx (fly left a distance from 20 - 500 cm)
right xx (fly right a distance from 20 - 500 cm)
forward xx (fly forward a distance from 20 - 500 cm)
back xx (fly backward a distance from 20 - 500 cm)
go x y z speed (fly x y z distance with speed)
cw xx (yaw clockwise with angle from 1 - 3600 degrees)
ccw xx (yaw counter clockwise with angle from 1 - 3600 degrees)
flip x (flip l/r/f/b/bl/br/fl/fr)
l = left
r = right
f = forward
b = backward
bl = backward left
br = backward right
fl = forward left
fr = forward right
speed x (set speed from 1 - 100 cm/s)
speed? (get current speed)
battery? (get current battery percentage)
time? (get current flight time)
