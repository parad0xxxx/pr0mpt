import time
import os
import sys
import getpass
import socket
import webbrowser
from datetime import date
today = date.today()
username = getpass.getuser()
host = socket.gethostname()
print(60 * "#")
print("#                                                          #")
print("#     Programmed by: Michael and Parad0x                   #")
print("#                                                          #")
print(60 * "#")
time.sleep(0.1)
# commands1
while True:
    command = str(input("$ " + username + " >> "))
    if command == "gethost":
        print(host)
    elif command == "youtube":
        webbrowser.open("www.youtube.com")
    elif command == "date":
        d4 = today.strftime("%b-%d-%Y")
        print("d4 =", d4)
    elif command == "nstat":
        os.system("netstat")
    elif command == "tr33":
        os.system("tree")
    elif command == "clr":
        os.system("cls")
    elif command == "ext":
        quit()
