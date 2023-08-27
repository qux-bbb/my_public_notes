# 控制CPU占用率

大概原理就是一段时间计算另一段时间休眠，占比宏观上就可以体现成CPU占用率，由于机器上还有其它程序运行，所以不会很精确。  

## 代码
### Windows版本
```c
#include <stdio.h>
#include <windows.h>

DWORD WINAPI ThreadFunc(void* data) {
    const int interval = 100; // 总时间间隔（毫秒）
    const int workTime = 30;  // 工作时间（毫秒）
    const int sleepTime = interval - workTime; // 休眠时间（毫秒）

    while (1) {
        DWORD startTime = GetTickCount();
        while ((GetTickCount() - startTime) <= workTime) {
        }
        Sleep(sleepTime);
    }

    return 0;
}

int main() {
    SYSTEM_INFO sysinfo;
    GetSystemInfo(&sysinfo);
    int numCPU = sysinfo.dwNumberOfProcessors;

    printf("Number of CPU cores: %d\n", numCPU);

    HANDLE* threads = (HANDLE*)malloc(numCPU * sizeof(HANDLE));
    if (threads == NULL) {
        fprintf(stderr, "Memory allocation failed.\n");
        return 1;
    }

    for (int i = 0; i < numCPU; ++i) {
        threads[i] = CreateThread(NULL, 0, ThreadFunc, NULL, 0, NULL);
        if (threads[i] == NULL) {
            fprintf(stderr, "Error creating thread %d\n", i);
            return 1;
        }
    }

    WaitForMultipleObjects(numCPU, threads, TRUE, INFINITE);

    free(threads);

    return 0;
}

```


### Linux版本
```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/sysinfo.h>
#include <time.h>

void *ThreadFunc(void *data) {
    const int interval = 100000000; // 总时间间隔（纳秒）
    const int workTime = 30000000;  // 工作时间（纳秒）
    const int sleepTime = interval - workTime; // 休眠时间（纳秒）

    struct timespec ts;
    ts.tv_sec = sleepTime / 1000000000;
    ts.tv_nsec = sleepTime % 1000000000;

    while (1) {
        struct timespec startTime, currentTime;
        clock_gettime(CLOCK_REALTIME, &startTime);
        do {
            clock_gettime(CLOCK_REALTIME, &currentTime);
        } while ((currentTime.tv_sec - startTime.tv_sec) * 1000000000 + (currentTime.tv_nsec - startTime.tv_nsec) <= workTime);
        nanosleep(&ts, NULL);
    }

    return NULL;
}

int main() {
    int numCPU = get_nprocs();
    printf("Number of CPU cores: %d\n", numCPU);

    pthread_t *threads = (pthread_t *)malloc(numCPU * sizeof(pthread_t));
    if (threads == NULL) {
        fprintf(stderr, "Memory allocation failed.\n");
        return 1;
    }

    for (int i = 0; i < numCPU; ++i) {
        if (pthread_create(&threads[i], NULL, ThreadFunc, NULL)) {
            fprintf(stderr, "Error creating thread %d\n", i);
            return 1;
        }
    }

    for (int i = 0; i < numCPU; ++i) {
        pthread_join(threads[i], NULL);
    }

    free(threads);

    return 0;
}

```

编译：  
```r
gcc cpu_control.c -o cpu_control -lpthread
```


## 来源
chatgpt  


---
2023/8/27  
