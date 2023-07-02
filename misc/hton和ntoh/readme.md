# hton和ntoh

hton和ntoh用来将主机字节顺序和网络字节顺序互转，内容根据ChatGPT整理。  

## 字节顺序
"字节顺序"是指在计算机系统中字节的排列方式，它在处理多字节数据类型（如 int，short，long 等）时十分重要。有两种常见的字节顺序：大端字节序（Big Endian）和小端字节序（Little Endian）。  

1. 大端字节序：最高有效字节在最低内存地址处，最低有效字节在最高内存地址处。比如，一个四字节整型数 `0x12345678` 在内存中的布局（从低地址到高地址）将是 `12 34 56 78`。  
2. 小端字节序：最高有效字节在最高内存地址处，最低有效字节在最低内存地址处。同样，对于四字节整型数 `0x12345678`，在内存中的布局将是 `78 56 34 12`。  

**主机字节顺序（Host Byte Order）**：主机字节顺序指的就是主机（也就是你的计算机）存储数据的字节顺序。不同的计算机架构有不同的字节顺序，例如 Intel 的 x86 架构是小端字节序，而 Motorola 的 68000 系列是大端字节序。

**网络字节顺序（Network Byte Order）**：网络字节顺序是 TCP/IP 网络协议中使用的字节顺序，它是大端字节序。为什么网络字节顺序使用大端字节序呢？这是因为 TCP/IP 协议最初在大端字节序的机器上开发的，所以就沿用了这个传统。

由于主机字节顺序和网络字节顺序可能不一样，所以在进行网络通信时，需要使用 `hton` 和 `ntoh` 函数进行转换，确保数据在不同机器之间能正确地传输和理解。


## hton
`hton` 是网络编程中的一个重要概念，它指的是 "Host TO Network" 的缩写。在网络通信中，不同的机器可能使用不同的字节顺序来存储数据。因此，为了在网络上发送数据，我们需要确保数据的字节顺序是一致的。这就是 `hton` 函数的作用。

在 C 语言中，有 `htons` 和 `htonl` 两种函数：

1. `htons`：Host TO Network Short，将一个无符号短整型数值（16位）从主机字节顺序转换成网络字节顺序。

2. `htonl`：Host TO Network Long，将一个无符号长整型数值（32位）从主机字节顺序转换成网络字节顺序。

主机字节顺序可以是大端模式（Big Endian）或小端模式（Little Endian），但网络字节顺序通常都是大端模式。

这是一个 C 语言的 `hton` 函数使用示例：

```c
#include <stdio.h>
#include <arpa/inet.h>

int main() {
    uint16_t hs = 0x1234;
    uint32_t hl = 0x12345678;

    uint16_t ns = htons(hs); // 转换16位短整型数值
    uint32_t nl = htonl(hl); // 转换32位长整型数值

    printf("Host Order: 0x1234, Network Order: 0x%x\n", ns);
    printf("Host Order: 0x12345678, Network Order: 0x%x\n", nl);

    return 0;
}
```

在这个示例中，我们使用 `htons` 和 `htonl` 函数将 16 位和 32 位的数值从主机字节顺序转换为网络字节顺序，并将转换后的值输出到控制台。运行这段代码，如果你的计算机是小端模式，那么输出结果将会显示主机字节顺序和网络字节顺序是不一样的。

结果：  
```
Host Order: 0x1234, Network Order: 0x3412
Host Order: 0x12345678, Network Order: 0x78563412
```

注意：`arpa/inet.h` 是 Unix 和 Linux 系统中的一个头文件，在 Windows 中相应的头文件是 `winsock2.h`。


## ntoh
与 `hton` 函数相对应，`ntoh` 函数是将数据从网络字节顺序转换为主机字节顺序。`ntoh` 是 "Network TO Host" 的缩写。

在 C 语言中，有 `ntohs` 和 `ntohl` 两种函数：

1. `ntohs`：Network TO Host Short，将一个无符号短整型数值（16位）从网络字节顺序转换成主机字节顺序。

2. `ntohl`：Network TO Host Long，将一个无符号长整型数值（32位）从网络字节顺序转换成主机字节顺序。

下面是一个 C 语言的 `ntoh` 函数使用示例：

```c
#include <stdio.h>
#include <arpa/inet.h>

int main() {
    uint16_t ns = 0x3412;
    uint32_t nl = 0x78563412;

    uint16_t hs = ntohs(ns); // 转换16位短整型数值
    uint32_t hl = ntohl(nl); // 转换32位长整型数值

    printf("Network Order: 0x3412, Host Order: 0x%x\n", hs);
    printf("Network Order: 0x78563412, Host Order: 0x%x\n", hl);

    return 0;
}
```

在这个示例中，我们使用 `ntohs` 和 `ntohl` 函数将 16 位和 32 位的数值从网络字节顺序转换为主机字节顺序，并将转换后的值输出到控制台。运行这段代码，如果你的计算机是小端模式，那么输出结果将会显示主机字节顺序和网络字节顺序是不一样的。

结果：  
```
Network Order: 0x3412, Host Order: 0x1234
Network Order: 0x78563412, Host Order: 0x12345678
```

注意：`arpa/inet.h` 是 Unix 和 Linux 系统中的一个头文件，在 Windows 中相应的头文件是 `winsock2.h`。


## Windows版本
hton使用代码：  
```c
#include <stdio.h>
#include <winsock2.h>
#include <cstdint>

// link with Ws2_32.lib
#pragma comment (lib, "Ws2_32.lib")

int main() {
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        printf("WSAStartup failed.\n");
        return 1;
    }

    uint16_t hs = 0x1234;
    uint32_t hl = 0x12345678;

    uint16_t ns = htons(hs); // 转换16位短整型数值
    uint32_t nl = htonl(hl); // 转换32位长整型数值

    printf("Host Order: 0x1234, Network Order: 0x%x\n", ns);
    printf("Host Order: 0x12345678, Network Order: 0x%x\n", nl);

    WSACleanup();

    return 0;
}
```

hton结果：  
```
Host Order: 0x1234, Network Order: 0x3412
Host Order: 0x12345678, Network Order: 0x78563412
```

ntoh使用代码：  
```c
#include <stdio.h>
#include <winsock2.h>
#include <cstdint>

// link with Ws2_32.lib
#pragma comment (lib, "Ws2_32.lib")

int main() {
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        printf("WSAStartup failed.\n");
        return 1;
    }

    uint16_t ns = 0x3412;
    uint32_t nl = 0x78563412;

    uint16_t hs = ntohs(ns); // 转换16位短整型数值
    uint32_t hl = ntohl(nl); // 转换32位长整型数值

    printf("Network Order: 0x3412, Host Order: 0x%x\n", hs);
    printf("Network Order: 0x78563412, Host Order: 0x%x\n", hl);

    WSACleanup();

    return 0;
}
```

ntoh结果：  
```
Network Order: 0x3412, Host Order: 0x1234
Network Order: 0x78563412, Host Order: 0x12345678
```


---
2023/7/3  
