#CopyRight Apache-2.0
#Powered By Python 3.X
#Author : @Aμιρ-0x0 (AMJ)

import os , requests
import shutil
def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)
def upgrade():
        if  os.geteuid() == 0:
                
                        option = input ("Are You Want to Full Upgrade SSF ?[Y/n]")
                        if option == "y" or option == "Y" or option == "yes" or option == "Yes":
                                try:
                                        requests.get("https://google.com/")
                                except:
                                        print ("Please Check Your Internet Connections")
                                os.system("git clone https://github.com/auip-0x0/sandsploit.git")
                                src = "sandsploit/"
                                dst = "/opt/sandsploit/"
                                copytree(src, dst)
                                """
                                path = "/opt/sandsploit"
                                with zipfile.ZipFile("/opt/sandsploit/files.zip", 'r') as zip_ref:
                                        zip_ref.extractall(path)
                                """
			        
                                os.chmod("/opt/sandsploit/Sandsploit.py",0o755)
			        
                                shutil.copy("/opt/sandsploit/sandsploit.desktop","/usr/share/applications/sandsploit.desktop")
                                cp = "/opt/sandsploit/module"
                                for root, dirs, files in os.walk(cp):
                                    for d in dirs:
                                        os.chmod(os.path.join(root, d),0o755)
                                    for f in files:
                                        os.chmod(os.path.join(root, f), 0o755)
		
                                print ("Successful. :)")
                        else:
                                print ("Cancelled.... :( ")
                
        else:
                print ("Please Run Sandsploit with root user to Starting Update...!")
