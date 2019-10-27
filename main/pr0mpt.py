import time
import os
import sys
import getpass
import socket
import webbrowser
from datetime import date
import platform

# variables
today = date.today()
username = getpass.getuser()
host = socket.gethostname()
start_msg = 'Pr0mpt [Version 1.0.0]\n(c) 2019 parad0x & michael\n'
OS = platform.system()
architecture = platform.architecture()
# welcome screen
print(start_msg)
time.sleep(0.1)

# cmd list
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
    else:
    	print('')
    	print('Given command invalid\n')
