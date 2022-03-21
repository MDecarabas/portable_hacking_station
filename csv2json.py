import pandas as pd

telloMacs = ["34:D2:62", "60:60:1F", "00:21:42"] #list of possible DJI mac address blocks

df = pd.read_csv('aero-01.csv') #Read the stored aeromon-ng data

for i in range(len(telloMacs)):
    networks = df[df['BSSID'].str.match(telloMacs[i])== True] #list through all possible networks

    if len(networks) != 0:
        Drone = networks[df['BSSID'].str.match(telloMacs[i])== True] # if found the add bits to json for connectPy to 
                                                                     # to read
        Bssid = Drone['BSSID'].tolist()
        Essid = Drone[' ESSID'].tolist()
        ch = Drone[' channel'].tolist()

wpaInfo = {"bssid": Bssid, "ssid": Essid, "C": ch,"password": "", }