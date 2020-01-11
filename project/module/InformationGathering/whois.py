#!/usr/bin/python3
import requests , re , readline , sys
import subprocess
uname =  subprocess.check_output("uname -o", shell=True)
if 'Android' in str(uname):
    sys.path.append("/data/data/com.termux/files/usr/opt/sandsploit/core")
else:
    sys.path.append("/opt/sandsploit/lib/")
from complator import *
host = None
name = "whois"
author = "@Aμιρ-0x0 (AMJ)"
info = "a Great Tool To Whois...."

def help():
    print ("author              to show author name")
    print ("help                to show this massage")
    print ("info                To show description of the tool ")
    print ("set                 to set options such as : [set host http://google.com/]")
    print ("show_options        to show options of Tools")
    print ("exit                to quit from Tool")

def options():
    print ("options               value")
    print ("==========            ============")
    print ("host                ",host)
    print("\033[95mYou Must Enter URL \033[91mwithout \033[95mProtocol (Example : site.com or 127.0.0.1)")
    print("\033[95mYou Must Write / at The End of URL EX: site.com/")

def run():
    try:
        url = "https://api.hackertarget.com/whois/?q="
        who = (url+host)
        r = requests.get(who)
        print (r.text)
    except:
        print("a Problem!Please Check Target Url and Internet Connection ......")

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
            if op2[1] == "host":
                host = op2[2]
                print ("host => ",host)
            else:
                print ("%s Not Found",op2[2])
        elif option == "run":
            run()
        elif option == "exit":
            break
        else:
            print ("Wrong Command ! ")
    except:
        print ('Unkonwn Error !')
