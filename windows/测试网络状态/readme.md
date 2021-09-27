# 测试网络状态

InternetGetConnectedState
```cpp
#include <stdio.h>
#include <Windows.h>
#include <WinInet.h>
#pragma comment(lib,"Wininet.lib")

int main() {
	DWORD dwReturnedFlag;

	BOOL result = InternetGetConnectedState(&dwReturnedFlag, 0);

	if (result)
		printf("Internet good\n");
	else
		printf("Internet bad\n");

    return 0;
}
```

官方不建议用 `InternetGetConnectedState`，建议用 `INetworkListManager::GetConnectivity`，感觉太麻烦了，就先这样  


参考链接：  
1. https://docs.microsoft.com/en-us/windows/win32/api/wininet/nf-wininet-internetgetconnectedstate
2. http://www.cplusplus.com/forum/windows/191484/


2021/9/27  
