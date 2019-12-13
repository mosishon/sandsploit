#CopyRight Apache-2.0
#Powered By Python 3.X
#Author : @Aμιρ-0x0 (AMJ)
import os , sys ,readline , re , platform
from colorama import Fore
from os.path import expanduser
from lib.Banner import banner 
from lib.update import update
from lib.version import version
from lib.Completor import *
from lib.Upgrade import upgrade
from core.listener import *
from core.RSMaker import RSMaker
from datetime import datetime
##################################################


def Commands():
    try:
    
        while True:
            getcwd = os.getcwd()
            getdir = getcwd.split("/")
            pwd =  getdir[-1]
            plat = platform.node()
            point = "→"
            
            option = input (Fore.RESET+"\n[SSF@%s](%s) %s "%(plat,pwd,point))
            
            option2 = option.split(" ")
            if option2[0] == "cd":
                
                def cd(path):
                    os.chdir(os.path.expanduser(path))
                try:
                    cd(option2[1])
                
                except:
                    print ("ERROR: No such file or directory: ",option2[1])
            elif option2[0] == 'run':
                
                    try:
                        
                        if option == "run":
                            print ("enter help to see how to use this command")
                        else:
                            run = option.split("run ")[1]
                            os.system("./"+run)
                    except:
                        print ("No file to execute")
            
            elif option2[0] == 'use':
                try:
                    os.chdir("/opt/sandsploit/module/"+option2[1])
                except:
                    print ("Part Not Found")
            elif option2[0] == "list":
                if "/opt/sandsploit/module/exploits/" in getcwd or "/opt/sandsploit/module/scripts/" in getcwd:
                    LIST()

            elif option == 'help':
                print ('''

Command     Description
========    ============
banner      Change Banner
bash        Run Bash Shell
list        Show Files List In Exploits & Scripts Parts
listener    Sniffing Port
python      Interactive Shell(Debuging Purposes)
RSMaker     Make Reverse Shell For Desktop Operating Systems
run         Run Exploits & Tools
use         Interact with one of the two sections of scripts or exploits
version     Show version of SandSploit
upgrade     Full Upgrade Freamworks
update      Update Exploits & Scripts Parts
exit        Exit From SSF
                ''')
            elif option == "version":
                version()
            elif option == "update":
                update()
            elif option == "upgrade":
                upgrade()
            elif option == "banner":
                banner()
            elif option == "RSMaker":
                RSMaker()
            elif option == "listener":
                #listener()
                main()
                Commands()
            elif option == "exit":
                break
            else:
                os.system(option)

    except EnvironmentError:
        print ("\nUnknown Error......")
        print ("Enter ""help"" to show commands....")
        Commands()
    except KeyboardInterrupt:
        print ("\nInterrupt: use the 'exit' command to quit")
        Commands()
