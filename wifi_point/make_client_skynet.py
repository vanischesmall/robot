#sudo apt update
#sudo apt full-upgrade

import os

MAKE_POINT=0

if MAKE_POINT:
    os.system('sudo cp /home/pi/robot/wifi_point/hostapd.conf /etc/hostapd/hostapd.conf')
    os.system('sudo cp /home/pi/robot/wifi_point/dhcpcd.conf.point /etc/dhcpcd.conf')

else:
    #make route connect to SkyNet
    os.system('sudo cp /home/pi/robot/wifi_point/dhcpcd.conf.route /etc/dhcpcd.conf')
print("Make client, reboot")
print("|STOPED")
os.system('sudo shutdown -r now')

