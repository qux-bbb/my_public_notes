# 写驱动程序

驱动程序的基本概念：驱动程序是一个“回调集合”，经初始化后，会在系统有需要时等待系统调用。  
这可能是新设备到达事件、用户模式应用程序的 I/O 请求、系统电源关闭事件、另一个驱动程序的请求，或用户意外拔出设备时的意外删除事件。  

DriverEntry 是所有驱动程序的入口点(名称可更改)，就像 Main() 适用于许多用户模式应用程序一样。  
DriverEntry 的任务是初始化驱动程序范围的结构和资源。  


## 简介
按照这个流程走：  
https://docs.microsoft.com/zh-cn/windows-hardware/drivers/gettingstarted/writing-your-first-driver  


## 安装工具
1. [Microsoft Visual Studio](https://go.microsoft.com/fwlink/p/?LinkId=698539)
2. [Windows SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk)
3. [Windows Driver Kit (WDK)](https://go.microsoft.com/fwlink/p/?LinkId=733614)

每个都下载安装最新版的即可，其它的按流程走好了  

可能会遇到 Spectre-缓解库 缺失问题，解决方法：  
```r
工具 -> 获取工具和功能
切换到"单个组件"，向下翻到已经勾选的  
"MSVC v142 - VS 2019 C++ x64/x86 生成工具(v14.28)"  
上面会有一个对应的  
"MSVC v142 - VS 2019 C++ x64/x86 Spectre 缓解库(v14.28)"  
勾选之后安装即可  

可能版本会有差异，是这个对应关系就可以  
```


## 一些缩写
UMDF, User Mode Driver Framework, 用户模式驱动程序框架  
KMDF, Kernel Mode Driver Framework, 内核模式驱动程序框架  
PnP, Plug and Play, 即插即用  


## KMDF程序代码示例
```cpp
// Ntddk.h 包含所有驱动程序的核心 Windows 内核定义，而 Wdf.h 包含基于 Windows 驱动程序框架(WDF) 的驱动程序的定义。
#include <ntddk.h>
#include <wdf.h>
DRIVER_INITIALIZE DriverEntry;
EVT_WDF_DRIVER_DEVICE_ADD KmdfHelloWorldEvtDeviceAdd;

NTSTATUS
DriverEntry(
    _In_ PDRIVER_OBJECT     DriverObject,
    _In_ PUNICODE_STRING    RegistryPath
)
{
    // NTSTATUS variable to record success or failure
    NTSTATUS status = STATUS_SUCCESS;

    // Allocate the driver configuration object
    WDF_DRIVER_CONFIG config;

    // Print "Hello World" for DriverEntry
    KdPrintEx((DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL, "KmdfHelloWorld: DriverEntry\n"));

    // Initialize the driver configuration object to register the
    // entry point for the EvtDeviceAdd callback, KmdfHelloWorldEvtDeviceAdd
    WDF_DRIVER_CONFIG_INIT(&config,
        KmdfHelloWorldEvtDeviceAdd
    );

    // Finally, create the driver object
    status = WdfDriverCreate(DriverObject,
        RegistryPath,
        WDF_NO_OBJECT_ATTRIBUTES,
        &config,
        WDF_NO_HANDLE
    );
    return status;
}

NTSTATUS
KmdfHelloWorldEvtDeviceAdd(
    _In_    WDFDRIVER       Driver,
    _Inout_ PWDFDEVICE_INIT DeviceInit
)
{
    // We're not using the driver object,
    // so we need to mark it as unreferenced
    UNREFERENCED_PARAMETER(Driver);

    NTSTATUS status;

    // Allocate the device object
    WDFDEVICE hDevice;

    // Print "Hello World"
    KdPrintEx((DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL, "KmdfHelloWorld: KmdfHelloWorldEvtDeviceAdd\n"));

    // Create the device object
    status = WdfDeviceCreate(&DeviceInit,
        WDF_NO_OBJECT_ATTRIBUTES,
        &hDevice
    );
    return status;
}
```


## devcon安装驱动
在开发机器上找到devcon，可能是这样的路径：  
```r
D:\Windows Kits\10\Tools\x64\devcon.exe  
C:\Program Files (x86)\Windows Kits\10\Tools\x64\devcon.exe  
```
复制到目标机器包含驱动程序文件的文件夹  

```r
# 使用方法
devcon install <INF file><hardware ID>
# 使用示例
c:\tools\devcon install kmdfhelloworld.inf root\kmdfhelloworld
```


---
2020/11/30  
