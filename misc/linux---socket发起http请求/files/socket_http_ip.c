// Client side C/C++ program to demonstrate Socket programming
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>
#define LEN 4096    //接收数据的大小

int main(int argc, char const *argv[])
{
	int sock = 0, valread;
	struct sockaddr_in serv_addr;

	if ((sock = socket(AF_INET, SOCK_STREAM, IPPROTO_IP)) < 0)
	{
		printf("\n Socket creation error \n");
		return -1;
	}

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(80);
	
	// Convert IPv4 and IPv6 addresses from text to binary form
	if(inet_pton(AF_INET, "110.242.68.4", &serv_addr.sin_addr)<=0)
	{
		printf("\nInvalid address/ Address not supported \n");
		return -1;
	}

    char buf[LEN] = "GET / HTTP/1.1\r\nHost: ";//构造Http请求数据包
	strcat(buf, "110.242.68.4");
	strcat(buf, " \r\nContent-Length: 10\r\n\r\n");
	strcat(buf, "Connection:close");

	if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
	{
		printf("\nConnection Failed \n");
		return -1;
	}

	send(sock, buf, strlen(buf), 0 );
	memset(buf, 0, LEN);
    valread = read(sock, buf, LEN);
	printf("%s\n", buf);
	return 0;
}
