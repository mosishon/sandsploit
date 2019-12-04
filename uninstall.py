#CopyRight Apache-2.0 - Immortal Team 
#Powered By Python 3.X
#Author : D3tect0r (AMJ)
import os , sys , shutil
if not os.geteuid() == 0:
    sys.exit("\n Run only with root access \n")
dirPath = '/opt/sandsploit'
try:
    shutil.rmtree(dirPath)
    os.remove('/usr/bin/sandsploit')
    os.remove("/usr/share/applications/sandsploit.desktop")
except:
   print('unknown Error...')
   sys.exit()
print ("Uninstalled...")
