#!/usr/bin/python3
import requests , readline , sys
sys.path.append("/opt/sandsploit/core/")
from complator import *
host = None
payfile = None

name = "XSS Scanner"
author = "Invisible Rabbit (Mahdis)"
info = "Scan Xss Vulnerability in the Website"


def help():
    print ("author              to show author name")
    print ("help                to show this massage")
    print ("info                To show description of the tool ")
    print ("show_options        to show options of Tools")
    print ("")
def options():
    print ("options               value")
    print ("==========            ============")
    print ("host                ",host)
    print ("payfile             ",payfile)
    print("\n\033[95mYou Must Enter IP without Protocol (Example : 127.0.0.1)")



def run ():
	try:
		payload_file = open(payfile,'r')
	except:
		print ("payload file not Found")
		return 0
	for payload in payload_file:
		pay = payload.replace("\n", " ")
		get_request=requests.get(host+pay)
		if get_request.status_code==200:
			if pay in get_request.text:
				print("target is vulnebilte! ")
				print ("Target Payload "+pay)
				break
