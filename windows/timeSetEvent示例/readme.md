# timeSetEvent示例

该api已被废弃，要使用CreateTimerQueueTimer   
```c
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#pragma comment(lib,"Winmm.lib")


# define ONE_MILLI_SECOND 1 //The definition of 1ms and 2S clock interval, the unit is MS ,
# define TWO_SECOND 2000
# define TIMER_ACCURACY 1 //Define the clock resolution, the unit is MS
void PASCAL OneMilliSecondProc(UINT wTimerID, UINT msg, DWORD dwUser, DWORD dwl, DWORD dw2)
{
	printf("11111111111\n");
	exit(0);
}

int main()

{
	HANDLE hHandle;

	UINT wTimerRes_1ms, wTimerRes_2s;//Define the time interval
	UINT wAccuracy; //The definition of resolution
	UINT TimerID_1ms, TimerID_2s; //Defines the timer handler
	wTimerRes_1ms = 5000;
	wAccuracy = 1;
	if ((TimerID_1ms = timeSetEvent(wTimerRes_1ms, wAccuracy, (LPTIMECALLBACK)OneMilliSecondProc, // The callback function
		(DWORD)(1), // The user is transmitted to the callback function data,
		TIME_PERIODIC)) == 0)//The timing function calling cycle
	{
		printf("start!!!!!!!!!!!\n");
	}
	else
	{
		printf("end!!!!!!!!!!!\n");
	}

	while (1)
	{
		printf("hello!\n");
		Sleep(1000);
	}

	return 0;
}
```

参考: https://www.programering.com/a/MTM4ITMwATE.html  
https://docs.microsoft.com/en-us/previous-versions/ms713423(v=vs.85)  


2019/11/20  
