#!/usr/bin/python3
import urllib.request ,sys , readline , re
from ssf import *
HOST = None
name = "Banner Finder"
author = "@Aμιρ-0x0 (AMJ)"
info = "a Tool for Grab Informations of websites...."
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
    print ("host                  ",HOST)
    print(" \033[95mYou Must Enter URL with Protocol (Example : https://site.com or http://site.com)")
    print(" \033[95mYou Must Write / at The End of URL EX: www.site.com/")

def run():

    
    site = urllib.request.urlopen(HOST)
    for key , value in site.headers.items():
        print (key + ":"+ value)

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
