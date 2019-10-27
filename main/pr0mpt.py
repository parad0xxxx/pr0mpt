import time
import os
import sys
import getpass
import socket
import webbrowser
from datetime import date
import platform
import requests

today = date.today()
username = getpass.getuser()
host = socket.gethostname()
pcIP = requests.get('https://api.ipify.org/').text
pvIP = socket.gethostbyname(socket.gethostname())
version = ' [Version 1.0.0]'
program_name = 'Pr0mpt'
c_license = '(c) 2019'
creators = ' parad0x & michael'
start_msg = program_name + version + '\n' + c_license + creators + '\n'
OS = platform.system()
architecture = platform.architecture()

print(start_msg)
time.sleep(0.1)
# commands1
while True:
    command = str(input("$ " + username + " >> "))
    if command == "gethost":
        print(host)
    elif command == "youtube":
        webbrowser.open('www.youtube.com')
    elif command == "date":
        d4 = today.strftime("%b-%d-%Y")
        print("d4 =", d4)
    elif command == "nstat":
        os.system('netstat')
    elif command == "ipconfig":
        os.system('ipconfig')
    elif command == "tree":
        os.system('tree')
    elif command == "clr":
        os.system('cls')
    elif command == "ext":
    	quit()
    elif command == "dir":
    	os.system('dir')
    elif command == "os":
    	print('OS platform: ' + OS)
    elif command == "arch":
    	print(architecture)
    elif command == "ip":
    	print("Public IP: " + pcIP + '\nPrivate IP: ' + pvIP)
    else:
    	print('')
    	print('Given command invalid\n')
