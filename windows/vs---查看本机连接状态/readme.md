# vs---查看本机连接状态

```cpp
#include <Windows.h>
#include <Wininet.h>
#include <stdio.h>
#pragma comment(lib,"Wininet.lib")


int main() {
	DWORD state;
	bool result = InternetGetConnectedState(&state, 0);
	if (result) {
		printf("yes, there is an active modem or a LAN Internet connection.\n");
	}
	else {
		printf("no, there is no Internet connection.\n");
	}

	printf("state\tnum\tmeaning\n");
	// 可能是几种状态的结合，所以不能用双等号判断
	if (state & INTERNET_CONNECTION_CONFIGURED) {
		printf("INTERNET_CONNECTION_CONFIGURED\t0x40\tLocal system has a valid connection to the Internet, but it might or might not be currently connected.\n");
	}
	if (state & INTERNET_CONNECTION_LAN) {
		printf("INTERNET_CONNECTION_LAN\t0x02\tLocal system uses a local area network to connect to the Internet.\n");
	}
	if (state & INTERNET_CONNECTION_MODEM) {
		printf("INTERNET_CONNECTION_MODEM\t0x01\tLocal system uses a modem to connect to the Internet.\n");
	}
	if (state & INTERNET_CONNECTION_MODEM_BUSY) {
		printf("INTERNET_CONNECTION_MODEM_BUSY\t0x08\tNo longer used.\n");
	}
	if (state & INTERNET_CONNECTION_OFFLINE) {
		printf("INTERNET_CONNECTION_OFFLINE\t0x20\tLocal system is in offline mode.\n");
	}
	if (state & INTERNET_CONNECTION_PROXY) {
		printf("INTERNET_CONNECTION_PROXY\t0x04\tLocal system uses a proxy server to connect to the Internet.\n");
	}
	if (state & INTERNET_RAS_INSTALLED) {
		printf("INTERNET_RAS_INSTALLED\t0x10\tLocal system has RAS installed.\n");
	}

	getchar();
	return 0;
}
```

参考链接：  
1. https://docs.microsoft.com/en-us/windows/win32/api/wininet/nf-wininet-internetgetconnectedstate
2. https://stackoverflow.com/questions/11182516/c-internetgetconnectedstate-loop


2022/5/5  
