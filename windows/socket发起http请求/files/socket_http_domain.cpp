#include<iostream>
#include <WINSOCK2.H>
#pragma comment(lib,"ws2_32.lib")
#define LEN 4096    //接收数据的大小
using namespace std;

#pragma warning(disable : 4996)


int get_webpage(char* domain)
{
	//加载套接字库
	WORD wVersionRequested;
	WSADATA wsaData;
	int err;

	wVersionRequested = MAKEWORD(1, 1);    //初始化Socket动态连接库,请求1.1版本的winsocket库

	err = WSAStartup(wVersionRequested, &wsaData);
	if (err != 0) {
		return 0;
	}

	SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);//建立socket
	if (sock == INVALID_SOCKET)
	{
		cout << "建立访问socket套接字失败!" << endl;
		return 0;
	}
	sockaddr_in hostadd;
	hostent* host = gethostbyname(domain);//取得主机的IP地址
	if (host == NULL)
	{
		cout << "主机处于没有联网状态;" << endl;
		return 0;
	}
	cout << "主机处于联网状态，现在可以进行通信!" << endl;
	memcpy(&hostadd, host->h_addr, sizeof(hostadd));//将返回的IP信息Copy到地址结构
	hostadd.sin_family = AF_INET;
	hostadd.sin_port = htons(80);

	char buf[LEN] = "GET / HTTP/1.1\r\nHost: ";//构造Http请求数据包
	strcat(buf, inet_ntoa(hostadd.sin_addr));
	strcat(buf, " \r\nContent-Length: 10\r\n\r\n");
	strcat(buf, "Connection:close");

	int time = 10000;    //超时时间
	setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, (char*)&time, sizeof(time));

	if (connect(sock, (sockaddr*)&hostadd, sizeof(hostadd)) == SOCKET_ERROR)//连接请求
	{
		cout << "与网页建立连接失败!" << endl;
		return 0;
	}
	if (SOCKET_ERROR == send(sock, buf, strlen(buf) + 1, 0))//发送构造好的Http请求包
	{
		cout << "发送数据包失败!" << endl;
		return 0;
	}
	memset(buf, 0, LEN);
	recv(sock, buf, LEN, 0);               //接收返回的数据
	cout << "从网页中获取的数据为:" << buf;
	closesocket(sock);
	WSACleanup();
	return 0;
}


int main()
{
	char domain[] = "www.baidu.com";
	get_webpage(domain);

	return 0;
}