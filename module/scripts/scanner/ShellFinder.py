#!/usr/bin/python3
import requests ,os , webbrowser  , re ,readline , sys
from colorama import Fore
sys.path.append("/opt/sandsploit/core/")
import Complator

host = None
name = "Shell Finder"
author = "Invisible rabbit (mahdis)"
info = "a Tool for find shells of a websites after upload...."

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
    print("\033[95mYou Must Enter URL \033[91mwithout \033[95mProtocol (Example : www.site.com or 127.0.0.1)")
    print("\033[95mYou Must Write / at The End of URL EX: www.site.com/")

def run():
  try:  
    pach = [Fore.RED + "c00.php", "c99.php" , "c100.php" , "c10.php" , "alfa.php" , "shell.php" , "sh.php" , "r57.php" , "c999.php" , "sheller.php" , "sl.php" , "hack.php" , "s.php" , "name.php" , "fuck.php", "hacked.php"]
    for i in pach:
      link = "http://" + host + "/" +  i
      r = requests.get(link)
      rw = r.status_code
      if rw == 200:
        print (Fore.BLUE + "shell in site foand" , link)
        webbrowser.open(link)
      else:
        print (Fore.RED + "not found" , link)
  except:
    print ("Please Cheack Internet or Target...")

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