# angr---带参数使用

yg写的脚本：  
```python
# coding:utf8

import angr
import claripy
 
p = angr.Project('rev_v2')
flag_chars = [claripy.BVS('flag_%d' % i, 8) for i in range(21)]
flag = claripy.Concat(*flag_chars + [claripy.BVV(b'\n')])
st = p.factory.full_init_state(
    args=['./rev_v2', flag],       #如果作为命令执行参数，加在args列表中
    add_options=angr.options.unicorn,
)
 
st.solver.add(flag_chars[0] == 0x63)
st.solver.add(flag_chars[1] == 0x74)
st.solver.add(flag_chars[2] == 0x66)
st.solver.add(flag_chars[3] == 0x7B)
st.solver.add(flag_chars[20] == 0x7D)
 
sm = p.factory.simulation_manager(st)
sm.explore(find=0x400481, avoid=[0x400471])
found = sm.found[0]
#found.posix.dumps(0)
 
flag = b''
for i in range(21):
    flag = flag + found.solver.eval(flag_chars[i], cast_to = bytes)
 
print(flag)

# b'ctf{ropchain_is_g00d}'
```


网上找的例子改一下：  
```python
# coding:utf8

# 参考：https://www.jianshu.com/p/bf9657eb9a14

import angr
import claripy

p = angr.Project('rev_v2')
argv1 = claripy.BVS('argv1', 21 * 8)  # 构造了21个字节
initial_state = p.factory.entry_state(args=['./rev_v2', argv1])  # 构造程序入口点的参数 ,第一个是filename，第二开始是程序参数

sm = p.factory.simulation_manager(initial_state)  # 从入口点出创建一个模拟器来进行符号执行

sm.explore(find=0x400481, avoid=[0x400471])

found = sm.found[0]

solution = found.solver.eval(argv1, cast_to=bytes)  # 获得正确结果中相对应的argv1符号的值，转换成bytes. cast_to支持的类型有int和bytes
print(bytes.decode(solution).strip('\x00')) # 先解码转换成str，再去掉\x00

# ctf{ropchain_is_g00d}
```

感谢yg(xy)  


2020/6/25  
