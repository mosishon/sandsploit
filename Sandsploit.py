#!/usr/bin/python3
#CopyRight Apache-2.0 - Immortal Team 
#Author : D3tect0r (AMJ)
import sys ,os , time , readline
from lib.Banner import banner 
from lib.Console import Commands
from os.path import expanduser
if  os.geteuid() == 0:
    print ("\n\033[91m Warning! you run Framework with root user! \n")
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)
#os.system("notify-send "+"Sandsploit "+"Started")
slowprint("\033[91m[!] Starting The Sandsploit Framework console... ")
time.sleep(4)
os.system("clear")

#home = expanduser("~") 
#os.chdir(home)
banner()
Commands()