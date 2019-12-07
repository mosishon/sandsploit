#CopyRight Apache-2.0 - Immortal Team 
#Powered By Python 3.X
#Author : D3tect0r (AMJ)
import requests, sys , urllib.request , shutil , hashlib , os , zipfile , time , tqdm , urllib
def update():
    if  os.geteuid() == 0:
        try:
                
            versionSource = open('/opt/sandsploit/module/version.txt', 'r')
            versionContents = versionSource.read()

            url = "https://dl-immortal.000webhostapp.com/DP/version.txt"
            r = requests.get(url)

            updatedatalit = r.text
            if updatedatalit != versionContents:
                print ("update available !")

                qs = input ("Do You Want to Update Tools? [y/n] ")

                if qs == 'y' or qs == 'Y' or qs == 'yes' or qs == 'Yes':

                    Durl="https://dl-immortal.000webhostapp.com/DP/files.zip"
                    
                    urllib.request.urlretrieve(Durl,'/tmp/files.zip')
                        
                    path = "/opt/sandsploit/"
                    with zipfile.ZipFile("/tmp/files.zip", 'r') as zip_ref:
                        zip_ref.extractall(path)
                    def slowprint(s):
                        for c in s + '\n' :
                            sys.stdout.write(c)
                            sys.stdout.flush()
                            time.sleep(7. / 100)
                    slowprint("################################### ")
                    print ("modules has been Updated !")
                else :
                    print ("OK...")
            else:
                print ("modules are already up-to-date")
        except:
            print ("Unknown Error! Please Check Internet Connection .....")
    else:
        print ("Please Run Sandsploit with root user to Starting Update...!")
