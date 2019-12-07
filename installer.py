#!/usr/bin/python3
#CopyRight Apache-2.0
#Author : @Aμιρ-0x0 (AMJ) & Roham Oghani
import os 
import time 
import sys  
import zipfile 
import shutil
from distutils.dir_util import copy_tree
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)
def setup():
    """
    with zipfile.ZipFile("files.zip", 'r') as zip_ref:
        zip_ref.extractall(path)
    """
    copy_tree("../sandsploit",path)
    os.symlink("/opt/sandsploit/Sandsploit.py","/usr/bin/sandsploit")
    copy_tree("../sandsploit",path)
    os.chmod("/opt/sandsploit/Sandsploit.py",0o755)
    shutil.copy("/opt/sandsploit/sandsploit.desktop","/usr/share/applications/sandsploit.desktop")
    cp = "/opt/sandsploit/module"
    for root, dirs, files in os.walk(cp):
        for d in dirs:
            os.chmod(os.path.join(root, d),0o755)
        for f in files:
            os.chmod(os.path.join(root, f), 0o755)
    os.system("pip install bs4 builtwith")
    print ("Installation completed successfully.....")
if not os.geteuid() is 0:
    sys.exit("\n Run only with root access \n")

path = "/opt/sandsploit"
if "sandsploit" not in "/usr/bin":
    while True:
        uname = os.system("uname -a")
        #option = input ("enter your distro base :")
        try:
            if "arch" or "Manjaro" in uname:
                slowprint("[!] Install the required items ")
                time.sleep(1)
                os.system("pacman -S python2 python2-pip python-pip torsocks")
                setup()
                break
            elif "Debian" or "ubuntu" in uname:
                slowprint("[!] Install the required items ")
                time.sleep(1)
                os.system("apt install tor python2 python2-pip python-pip torsocks")
                setup()
                break
            elif "FreeBSD" in uname:
                slowprint("[!] Install the required items ")
                time.sleep(1)
                os.system("pkg install tor python2 python2-pip python-pip torsocks")
                setup()
                break
        except:
            print("Please Check Internet and option Number...")
else:
    print ("Sandsploit has Exist In /usr/bin/ I Can't install Sandsploit....")
