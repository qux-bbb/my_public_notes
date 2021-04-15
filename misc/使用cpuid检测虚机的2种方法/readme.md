# 使用cpuid检测虚机的2种方法
## 检测方式
1. EAX = 1，获取CPU功能信息，如果ECX第31位为1， 则表明有hypervisor存在，即环境是虚拟的。
2. EAX = 0x40000000, 获取hypervisor信息，返回12字节长度字符串：
    ```
    "KVMKVMKVM\0\0\0"    KVM
    "Microsoft Hv"       Microsoft Hyper-V or Windows Virtual PC
    "VMwareVMware"       VMware
    "XenVMMXenVMM"       Xen
    "prl hyperv  "       Parallels
    "VBoxVBoxVBox"       VirtualBox
    ```

经测试，第2种方法在kvm下创建的windows虚机，返回的是"Microsoft Hv"  

参考链接: https://consen.github.io/2016/09/11/Anti-VM-via-CPUID/  


## 调整返回结果
### vmware
假设虚机是win7_x64_1，先关闭虚机，然后编辑win7_x64_1.vmx，在最后添加如下内容：  
```
cpuid.40000000.eax="0000:0000:0000:0000:0000:0000:0000:0000"
cpuid.40000000.ebx="0000:0000:0000:0000:0000:0000:0000:0000"
cpuid.40000000.ecx="0000:0000:0000:0000:0000:0000:0000:0000"
cpuid.40000000.edx="0000:0000:0000:0000:0000:0000:0000:0000"
```
这样可以调整`EAX = 0x40000000`时cpuid指令返回的结果，重启生效  

参考链接: https://rayanfam.com/topics/defeating-malware-anti-vm-techniques-cpuid-based-instructions/  

### virtualbox
```bash
# 列出vm
VBoxManage list vms
# 修改cpuid [--cpuid-set <leaf[:subleaf]> <eax> <ebx> <ecx> <edx>]
VBoxManage modifyvm win7_x64_1 --cpuid-set 1 0 0 0 0
```
&&&&&&& 但这么设置之后开不了机  

参考链接: https://forums.virtualbox.org/viewtopic.php?f=2&t=77211#p359428  

### kvm
kvm这里写了一种方法修改，但是测试失败了，暂时没有办法修改  
https://security.stackexchange.com/questions/220357/fake-output-of-cpuid-instruction  
kvm收到了一个新的回答：https://stackoverflow.com/questions/64460675/how-to-modify-the-return-value-of-cpuid-of-windows-created-by-kvm/65387651#65387651 ，有机会试试看吧，先记下来（&&&&&&&）  
