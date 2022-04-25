# kvm---虚机内时间加速问题

编辑相应快照  
```r
virsh snapshot-edit GuestName SnapshotName
```

找到 clock 元素:  
```r
<clock offset='localtime' >
    <timer name='rtc' tickpolicy='catchup' />
    ...
</clock>
```

将 `catchup` 改为 `delay`，保存退出再恢复快照, 时钟正常了, 不会加速走表  


tickpolicy 可选值 参考 [25.11. Virtual machine timer management with libvirt](https://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/Virtualization_Deployment_and_Administration_Guide/sect-Virtualization-Tips_and_tricks-Libvirt_Managed_Timers.html)


原链接：https://www.zhihu.com/question/39628689


2020/8/7  
