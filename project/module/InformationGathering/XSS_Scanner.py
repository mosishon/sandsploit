#!/usr/bin/python3
import requests , readline , sys
import subprocess

sys.path.append("/data/data/com.termux/files/usr/opt/sandsploit/core")
sys.path.append("/opt/sandsploit/core/")
from complator import *
HOST = None
PAYFILE = None

name = "XSS Scanner"
author = "Invisible Rabbit (Mahdis)"
info = "Scan Xss Vulnerability in the Website"


def help():
    print ("author              to show author name")
    print ("help                to show this massage")
    print ("info                to show description of the tool ")
    print ("set                 to set options such as : [set host http://google.com/]")
    print ("show_options        to show options of Tools")
    print ("exit                to quit from Tool")
    print ("run                 to Run Session")

def options():
    print ("options               value")
    print ("==========            ============")
    print ("host                ",HOST)
    print ("payfile             ",PAYFILE)
    print("\n\033[95mYou Must Enter IP without Protocol (Example : 127.0.0.1)")



def run ():
	try:
		payload_file = open(PAYFILE,'r')
	except:
		print ("payload file not Found")
		return 0
	for payload in payload_file:
		pay = payload.replace("\n", " ")
		get_request=requests.get(HOST+pay)
		if get_request.status_code==200:
			if pay in get_request.text:
				print("target is vulnebilte! ")
				print ("Target Payload "+pay)
				break

while True:
    try:
        option = input ("\033[96m┌─[SSF][\033[91m"+name+"\033[96m]\n└─▪ ")
        op2 = option.split(" ")
        if option == "help":
            help()
        elif option == "author":
            print (author)
        elif option == "info":
            print (info)

        elif option == "show_options":
            options()
        elif op2[0] == "set":
            op3 = op2[1].upper()    
            vars()[op3] = op2[2]
            print ("%s => %s"%(op2[1],op2[2]))
        elif option == "run":
            run()
        elif option == "exit":
            break
        else:
            print ("Wrong Command ! ")
    except:
        print ('Unkonwn Error !')