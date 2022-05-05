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
	if (state & INTERNET_CONNECTION_CONFIGURED)
		printf("%s\t%s\t%s\n",
			"INTERNET_CONNECTION_CONFIGURED",
			"0x40",
			"Local system has a valid connection to the Internet, but it might or might not be currently connected."
		);
	if (state & INTERNET_CONNECTION_LAN)
		printf("%s\t%s\t%s\n",
			"INTERNET_CONNECTION_LAN",
			"0x02",
			"Local system uses a local area network to connect to the Internet."
		);
	if (state & INTERNET_CONNECTION_MODEM)
		printf("%s\t%s\t%s\n",
			"INTERNET_CONNECTION_MODEM",
			"0x01",
			"Local system uses a modem to connect to the Internet."
		);
	if (state & INTERNET_CONNECTION_MODEM_BUSY)
		printf("%s\t%s\t%s\n",
			"INTERNET_CONNECTION_MODEM_BUSY",
			"0x08",
			"No longer used."
		);
	if (state & INTERNET_CONNECTION_OFFLINE)
		printf("%s\t%s\t%s\n",
			"INTERNET_CONNECTION_OFFLINE",
			"0x20",
			"Local system is in offline mode."
		);
	if (state & INTERNET_CONNECTION_PROXY)
		printf("%s\t%s\t%s\n",
			"INTERNET_CONNECTION_PROXY",
			"0x04",
			"Local system uses a proxy server to connect to the Internet."
		);
	if (state & INTERNET_RAS_INSTALLED)
		printf("%s\t%s\t%s\n",
			"INTERNET_RAS_INSTALLED",
			"0x10",
			"Local system has RAS installed."
		);

	getchar();
	return 0;
}
```

没懂原理，在reactos搜索  
InternetGetConnectedState 执行了 `TRACE("(%p, 0x%08x)\n", lpdwStatus, dwReserved);` 调用 InternetGetConnectedStateExW  
InternetGetConnectedStateExW 执行了 `TRACE("(%p, %p, %d, 0x%08x)\n", lpdwStatus, lpszConnectionName, dwNameLen, dwReserved);` 就有结果了  
不懂  


参考链接：  
1. https://docs.microsoft.com/en-us/windows/win32/api/wininet/nf-wininet-internetgetconnectedstate
2. https://stackoverflow.com/questions/11182516/c-internetgetconnectedstate-loop


2022/5/5  
