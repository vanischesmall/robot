import sys
import os
#python2 set_password.py 123
#arg = sys.argv[1]
myhost = os.uname()[1]

# arg=""

import hashlib
# pass_hash = hashlib.sha224(arg.encode('utf-8')).hexdigest()[:3]


#тут надо указать свой пароль
password="wre"


pass_hash = hashlib.sha224(password.encode('utf-8')).hexdigest()[:3]

dir = "/home/pi/robot/"
if myhost.find("ras") == 0:
    dir = "/home/pi/robot/"
else:
    dir = "/root/robot/"

file = open(dir+'password', 'w+')
#file = open('/root/robot/password', 'w+')
print(pass_hash)
file.write(pass_hash)
file.close()

import os
#os.system('sudo shutdown -r now')
# os.system('sudo reboot')



