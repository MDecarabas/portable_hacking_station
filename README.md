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
* Mount the downloaded image to a formated sd card of your choosing
  * If you don't already have an sd card etcher downloaded I personally reccomend Balena.
  * Download links for balena available here: https://www.balena.io/etcher/

# Required Firmware for Hardware
1) PiJuice Firmware
2) rtl8188eu (managed mode wifi card)
3) rtl8812au (monitor mode wifi card)
4) bluetooth transmitter
5) 

# Libraries Used
1) Tello SDK 2.0
2) Wifite 2.0
3) aircrack-ng
4) t-shark

# Cracking Scripts
1) crack.py
2) connect.py
3) crackNconnect.py

# Example Attack Scripts
1) land.py
2) pilot.py
3) collect.py
