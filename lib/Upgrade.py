#CopyRight Apache-2.0
#Powered By Python 3.X
#Author : @Aμιρ (AMJ)

import os , requests
from shutil import copyfile

def upgrade():
        if  os.geteuid() == 0:
                try:
                        option = input ("Are You Want to Full Upgrade SSF ?[Y/n]")
                        if option == "y" or option == "Y" or option == "yes" or option == "Yes":
                                try:
                                        requests.get("https://google.com/")
                                except:
                                        print ("Please Check Your Internet Connections")
                                os.system("git clone https://github.com/auip_0x0/sandsploit.git")
                                src = "sandsploit/*"
                                dst = "/opt/sandsploit/"
                                copyfile(src, dst)
                                """
                                path = "/opt/sandsploit"
                                with zipfile.ZipFile("/opt/sandsploit/files.zip", 'r') as zip_ref:
                                        zip_ref.extractall(path)
                                """
                                
                                print ("Successful. :)")
                        else:
                                print ("Cancelled.... :( ")
                except:
                        print ("Unknown Error!!!")
        else:
                print ("Please Run Sandsploit with root user to Starting Update...!")
                
