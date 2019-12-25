#!/usr/bin/python3
#CopyRight Apache-2.0 
#Author : @Aμιρ-0x0 (AMJ)
import sys ,os , time , readline
from core.__init__ import * 
from lib.__init__ import *
from lib.termux import *
from os.path import expanduser
if  os.geteuid() == 0:
    print ("\n\033[91m Warning! you run Framework with root user! \n")
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=110))
slowprint("\033[91m[!] Starting The Sandsploit Framework console... ")
time.sleep(4)
os.system("clear")
uname = subprocess.check_output("uname -o", shell=True)
if 'Android' in uname:
    banner()
    termuxconsole()
else:
    banner()
    Commands()
