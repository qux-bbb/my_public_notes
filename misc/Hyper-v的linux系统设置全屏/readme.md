# Hyper-v的linux系统设置全屏

1. Open Terminal
2. Type: `sudo vi /etc/default/grub`
3. Find the line starting with `GRUB_CMDLINE_LINUX_DEFAULT`, and add `video=hyperv_fb:[the resolution you want]`.  The resolution I want is `1280x720`.  So my line ends up looking like this: `GRUB_CMDLINE_LINUX_DEFAULT="quiet splash video=hyperv_fb:1280x720"`
4. Write the changes and quit vi.
5. Run: `sudo update-grub`
6. Reboot the virtual machine


原地址：https://blogs.msdn.microsoft.com/virtual_pc_guy/2014/09/19/changing-ubuntu-screen-resolution-in-a-hyper-v-vm/  


2017/12/23  
