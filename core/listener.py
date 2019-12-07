import os
def listener():
        port = input("Please Enter Port To Start Sniffing : ")
        os.system("nc -nvlp "+port)