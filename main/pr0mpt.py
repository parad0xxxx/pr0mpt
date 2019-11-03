# Imports #/***THIS IS STILL UNDER DEVELOPMENT 
import time
import os
import sys
import getpass
import socket
import webbrowser
from datetime import date
import platform
import requests
import geoip2.database # for ip tracking, coming soon.
import pyautogui
# variables and strings.
today = date.today()
username = getpass.getuser()
host = socket.gethostname()
pcIP = requests.get('https://api.ipify.org/').text
pvIP = socket.gethostbyname(socket.gethostname())
version = ' [Version 1.0.0]'
program_name = 'Pr0mpt'
c_license = '(c) 2019'
creators = ' Parad0x & Michael'
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
        date = today.strftime("%b-%d-%Y")
        print("DATE: ", date)
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
    elif command == "echo":
        echo = input("> ")
        print(echo)
    elif command == "colorA1":
        os.system("color 2")
    elif command == "colorA2":
        os.system("color 1")
    elif command == "colorA3":
        os.system("color 3")
    elif command == "colorA4":
        os.system("color 4")
    elif command == "colorA5":
        os.system("color 5")
    elif command == "colorA6":
        os.system("color 6")
    elif command == "colorA7":
        os.system("color 7")
    elif command == "dquery":
        os.system("driverquery")
    elif command == "shutdown":
        os.system("shutdown -s")
    elif command == "restart":
        os.system("shutdown /r")
    elif command == "show net profiles":
        os.system("netsh wlan show profiles")
    elif command == "py-install":
        ginstall = input(username +"py-install > ")
        os.system("pip install %s" % ginstall)
    elif command == "show net key=clr":
        keyclr = input("network > ")
        os.system("netsh wlan show profiles %s key=clear" % keyclr)
    elif command == "run":
        pyautogui.hotkey('win', 'r')
    elif command == "npad":
        files = input("> ")
        os.system("notepad %s" % files)
    elif command == "ping":
        ping = input("> ")
        os.system("ping %s" % ping)
    else:
    	print('')
    	print('[!] Given command invalid\n')
