# LuaJIT---处理与恢复

LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language.  

官网: https://luajit.org/luajit.html  

## 安装
```bash
git clone https://luajit.org/git/luajit.git
cd luajit
make && sudo make install
```

## 处理lua脚本
```bash
# 处理
luajit -b test.lua test_jit
# 执行处理后的脚本
luajit test_jit
```

## 恢复

python版本的工具，老版本的应该都可以处理: https://github.com/Aussiemon/ljd  
用法: `python3 ./main.py --recursive ./<input directory> --dir_out ./<output directory> --catch_asserts`  

exe版本的工具，可以处理新版本的文件，应该得在win10及以上系统里运行: https://github.com/marsinator358/luajit-decompiler-v2  

原链接: https://stackoverflow.com/a/77540765/7164926  


---
2024/6/7  
