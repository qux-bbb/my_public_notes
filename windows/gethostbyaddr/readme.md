# gethostbyaddr

gethostbyaddr, 通过ip获取hostent结构的数据。  

```cpp
#define _WINSOCK_DEPRECATED_NO_WARNINGS

#include <winsock2.h>
#include <ws2tcpip.h>
#include <stdio.h>
#pragma comment(lib, "Ws2_32.lib")

int main(int argc, char** argv)
{

    //-----------------------------------------
    // Declare and initialize variables
    WSADATA wsaData;
    int iResult;

    DWORD dwError;
    int i = 0;
    int bIpv6 = 0;

    struct hostent* remoteHost;
    char* host_addr;
    struct in_addr addr = { 0 };
    IN6_ADDR addr6;

    char** pAlias;

    // Validate the parameters
    if (argc < 2) {
        printf("usage: %s 4 ipv4address\n", argv[0]);
        printf(" or\n");
        printf("usage: %s 6 ipv6address\n", argv[0]);
        printf("  to return the hostname\n");
        printf("       %s 4 127.0.0.1\n", argv[0]);
        printf("       %s 6 0::1\n", argv[0]);
        return 1;
    }
    // Validate parameters 
    if (atoi(argv[1]) == 4)
        bIpv6 = 0;
    else if (atoi(argv[1]) == 6)
        bIpv6 = 1;
    else {
        printf("usage: %s 4 ipv4address\n", argv[0]);
        printf(" or\n");
        printf("usage: %s 6 ipv6address\n", argv[0]);
        printf("  to return the hostname\n");
        printf("       %s 4 127.0.0.1\n", argv[0]);
        printf("       %s 6 0::1\n", argv[0]);
        return 1;
    }

    // Initialize Winsock
    iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (iResult != 0) {
        printf("WSAStartup failed: %d\n", iResult);
        return 1;
    }

    host_addr = argv[2];

    printf("Calling gethostbyaddr with %s\n", host_addr);
    if (bIpv6 == 1) {
        {
            iResult = inet_pton(AF_INET6, host_addr, &addr6);
            if (iResult == 0) {
                printf("The IPv6 address entered must be a legal address\n");
                return 1;
            }
            else
                remoteHost = gethostbyaddr((char*)&addr6, 16, AF_INET6);
        }
    }
    else {
        addr.s_addr = inet_addr(host_addr);
        if (addr.s_addr == INADDR_NONE) {
            printf("The IPv4 address entered must be a legal address\n");
            return 1;
        }
        else
            remoteHost = gethostbyaddr((char*)&addr, 4, AF_INET);
    }

    if (remoteHost == NULL) {
        dwError = WSAGetLastError();
        if (dwError != 0) {
            if (dwError == WSAHOST_NOT_FOUND) {
                printf("Host not found\n");
                return 1;
            }
            else if (dwError == WSANO_DATA) {
                printf("No data record found\n");
                return 1;
            }
            else {
                printf("Function failed with error: %ld\n", dwError);
                return 1;
            }
        }
    }
    else {
        printf("Function returned:\n");
        printf("\tOfficial name: %s\n", remoteHost->h_name);
        for (pAlias = remoteHost->h_aliases; *pAlias != 0; pAlias++) {
            printf("\tAlternate name #%d: %s\n", ++i, *pAlias);
        }
        printf("\tAddress type: ");
        switch (remoteHost->h_addrtype) {
        case AF_INET:
            printf("AF_INET\n");
            break;
        case AF_INET6:
            printf("AF_INET6\n");
            break;
        case AF_NETBIOS:
            printf("AF_NETBIOS\n");
            break;
        default:
            printf(" %d\n", remoteHost->h_addrtype);
            break;
        }
        printf("\tAddress length: %d\n", remoteHost->h_length);

        if (remoteHost->h_addrtype == AF_INET) {
            while (remoteHost->h_addr_list[i] != 0) {
                addr.s_addr = *(u_long*)remoteHost->h_addr_list[i++];
                printf("\tIPv4 Address #%d: %s\n", i, inet_ntoa(addr));
            }
        }
        else if (remoteHost->h_addrtype == AF_INET6)
            printf("\tRemotehost is an IPv6 address\n");
    }

    return 0;
}
```


原链接: https://docs.microsoft.com/en-us/windows/win32/api/winsock2/nf-winsock2-gethostbyaddr  
错误处理: https://stackoverflow.com/questions/16948064/unresolved-external-symbol-lnk2019/16948470  


2021/10/29  
