# pcap流量包---键盘鼠标相关脚本

提取键盘鼠标操作的脚本。  

键盘  
```python

mappings = { 0x04:"A",  0x05:"B",  0x06:"C", 0x07:"D", 0x08:"E", 0x09:"F", 0x0A:"G",  0x0B:"H", 0x0C:"I",  0x0D:"J", 0x0E:"K", 0x0F:"L", 0x10:"M", 0x11:"N",0x12:"O",  0x13:"P", 0x14:"Q", 0x15:"R", 0x16:"S", 0x17:"T", 0x18:"U",0x19:"V", 0x1A:"W", 0x1B:"X", 0x1C:"Y", 0x1D:"Z", 0x1E:"1", 0x1F:"2", 0x20:"3", 0x21:"4", 0x22:"5",  0x23:"6", 0x24:"7", 0x25:"8", 0x26:"9", 0x27:"0", 0x28:"\n", 0x2a:"[DEL]",  0X2B:"    ", 0x2C:" ",  0x2D:"-", 0x2E:"=", 0x2F:"[",  0x30:"]",  0x31:"\\", 0x32:"~", 0x33:";",  0x34:"'", 0x36:",",  0x37:"." }
nums = []
keys = open('usbdata.txt')
for line in keys:
    if line[0]!='0' or line[1]!='0' or line[3]!='0' or line[4]!='0' or line[9]!='0' or line[10]!='0' or line[12]!='0' or line[13]!='0' or line[15]!='0' or line[16]!='0' or line[18]!='0' or line[19]!='0' or line[21]!='0' or line[22]!='0':
         continue
    nums.append(int(line[6:8],16))
keys.close()
output = ""
for n in nums:
    if n == 0 :
        continue
    if n in mappings:
        output += mappings[n]
    else:
        output += '[unknown]'
print 'output :\n' + output
————————————————
版权声明：本文为CSDN博主「EvilGenius-」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_36609913/article/details/78578406
```


鼠标  
```python
nums = [] 
keys = open('data.txt','r') 
posx = 0 
posy = 0 
for line in keys: 
if len(line) != 12 : 
     continue 
x = int(line[3:5],16) 
y = int(line[6:8],16) 
if x > 127 : 
    x -= 256 
if y > 127 : 
    y -= 256 
posx += x 
posy += y 
btn_flag = int(line[0:2],16)  # 1 for left , 2 for right , 0 for nothing 
if btn_flag == 1 : 
    print posx , posy 
keys.close()
————————————————
版权声明：本文为CSDN博主「EvilGenius-」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_36609913/article/details/78578406
```

原链接: https://blog.csdn.net/qq_36609913/article/details/78578406  
键位资料: https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf  


---
2019/9/25  
