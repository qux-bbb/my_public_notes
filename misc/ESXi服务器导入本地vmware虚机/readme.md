# ESXi服务器导入本地vmware虚机

ESXi服务器版本: 6.5  
vmware版本: 15.5.7  

场景: ESXi服务器在内网，不连外网，需要在外网将vmware虚机配置好，然后放到ESXi服务器  


## 具体操作
1. 在外网安装ubuntu20虚机，安装好需要的软件，测试功能可用后，关闭虚机  
2. 文件->导出为OVF，时间较长，最终生成3个文件: ubuntu20.mf ubuntu20.ovf ubuntu20-disk1.vmdk，实际只用到后两个文件  
3. 由于ESXi服务器版本版本太老，所以需要修改ubuntu20.ovf文件
   a. 将VirtualSystemType标签中的"vmx-16"改为"vmx-13"  
   b. 将"videoRamSizeInKB"一行注释掉，注释举例: `<!-- hello -->`  
4. 登录ESXi服务器，开始部署  
   a. 选择"Virtual Machines"，菜单点击"Register VM"  
   b. 创建类型选择"Deploy a virtual machine from an OVF or OVA file"  
   c. 选择ovf和vmdk文件，后续步骤默认即可  


## 错误记录
`Unsupported hardware family vmx-16`  
解决问题链接: https://www.running-system.com/unsupported-hardware-family-vmx-10-during-ovf-import/  
逻辑：版本太高，ESXi不支持，修改为支持的版本即可，ESXi和vmware版本关系见该链接：  
https://kb.vmware.com/s/article/2007240  

`Invalid configuration for device '0'`  
解决问题链接: https://cumt.org/blog/728  
逻辑：该版本ESXi服务器不支持显存，注释"videoRamSizeInKB"行即可  


---
2021/11/1  
