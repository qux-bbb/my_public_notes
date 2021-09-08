# angr

## 简介
angr is a python framework for analyzing binaries. It combines both static and dynamic symbolic ("concolic") analysis, making it applicable to a variety of tasks.  
angr 是一个用于分析二进制文件的 python 框架。它结合了静态和动态符号（"concolic"）分析，适用于各种任务。  

官网：http://angr.io/  

从这里开始看 angr 的方法：  
https://docs.angr.io/core-concepts/toplevel  


## 安装
官方建议先搞个虚拟环境，然后pip安装  
`pip install angr`  


## 示例

### 例子1
```python
import angr

proj = angr.Project('signal.exe', auto_load_libs=False)
simgr = proj.factory.simgr()
avoid_list=[0x401539, 0x4016E6]
simgr.explore(find=0x40179E, avoid=avoid_list)
print(simgr.found[0].posix.dumps(0))

# b'757515121f3d478\x00\x02*\x0e\x01\x00\x02\x0f\x00\x00\x01\x00\x08\x19\x08\x02\x02\x19\x00\x00\x02\x08\x00\x02\x02\x00\x1b\x00\x00\x00\x00\x01\x1a)\x0e\x01\x02\x08)\x0eJ\x1a\x00\x1a\x0e'
```

### 例子2
https://github.com/angr/angr-doc/tree/master/examples/CSCI-4968-MBE/challenges/crackme0x00a  

#### 写法1
通过地址确定是否成功：  
```python
import angr

FIND_ADDR = 0x08048533 # mov dword [esp], str.Congrats_ ; [0x8048654:4]=0x676e6f43 LEA str.Congrats_ ; "Congrats!" @ 0x8048654
AVOID_ADDR = 0x08048554 # mov dword [esp], str.Wrong_ ; [0x804865e:4]=0x6e6f7257 LEA str.Wrong_ ; "Wrong!" @ 0x804865e


def main():
	proj = angr.Project('crackme0x00a', load_options={"auto_load_libs": False})
	sm = proj.factory.simulation_manager()
	sm.explore(find=FIND_ADDR, avoid=AVOID_ADDR)
	return sm.found[0].posix.dumps(0).split(b'\0')[0] # stdin

def test():
	assert main() == b'g00dJ0B!'

if __name__ == '__main__':
	print(main())
```

#### 写法2
通过输出确定是否成功  
```python
import angr


def main():
	proj = angr.Project('crackme0x00a', load_options={"auto_load_libs": False})
	simgr = proj.factory.simgr()
	simgr.explore(find=lambda s: b"Congrats" in s.posix.dumps(1))
	return simgr.found[0].posix.dumps(0).split(b'\0')[0]

if __name__ == '__main__':
	print(main())

```


## 注意点
如果不指定 `auto_load_libs=False`，会很慢  

尽量把成功失败的位置找全，位置要尽量靠近判断的指令  


## 杂乱
CLE: angr's binary loading component, CLE stands for "CLE Loads Everything"  
AST: abstract syntax tree, 抽象语法树  
bbl_addrs:  basic block addresses  

```python
# 值 64，长度 64 的 bitvector 常量
one_hundred = state.solver.BVV(100, 64)

# 长度 64 的 bitvector 有符号变量
x = state.solver.BVS("x", 64)
```

大范围的内存读写  
```python
>>> s = proj.factory.blank_state()
>>> s.memory.store(0x4000, s.solver.BVV(0x0123456789abcdef0123456789abcdef, 128))
>>> s.memory.load(0x4004, 6) # load-size is in bytes
<BV48 0x89abcdef0123>
```

断点设置举例  
```python
# This will break before a memory write if 0x1000 is a possible value of its target expression
>>> s.inspect.b('mem_write', mem_write_address=0x1000)

# This will break before a memory write if 0x1000 is the *only* value of its target expression
>>> s.inspect.b('mem_write', mem_write_address=0x1000, mem_write_address_unique=True)

# This will break after instruction 0x8000, but only 0x1000 is a possible value of the last expression that was read from memory
>>> s.inspect.b('instruction', when=angr.BP_AFTER, instruction=0x8000, mem_read_expr=0x1000)
```


2020/8/9  
