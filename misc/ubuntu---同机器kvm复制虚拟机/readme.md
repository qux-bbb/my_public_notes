# ubuntu---同机器kvm复制虚拟机

使用virt-clone在同机器上复制一台虚拟机  
```r
# Clone a virtual machine and automatically generate a new name, storage path, and MAC address:
virt-clone --original vm_name --auto-clone

# Clone a virtual machine and specify the new name, storage path, and MAC address:
virt-clone --original vm_name --name new_vm_name --file path/to/new_storage --mac ff:ff:ff:ff:ff:ff|RANDOM
```

来源：  
1. tldr
2. https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/cloning-a-vm


2022/8/21  
