# SEMA

github地址: https://github.com/csvl/SEMA  
官方文档: https://csvl.github.io/SEMA/  

SEMA, ToolChain using Symbolic Execution for Malware Analysis.  

安装方法：  
```bash
# 提前安装 git、make
# 安装docker，设置非root用户管理docker
# 如果docker网络不好，安装v2raya，使用docker的daemon.json配置代理
git clone https://github.com/csvl/SEMA.git
cd SEMA/sema_toolchain
make run-toolchain
```

安装出错，应该是docker镜像内部的问题，不知道怎么解决：  
```r
Step 24/31 : RUN pypy3 -m pip install -r /sema-scdg/requirements_pypy.txt
 ---> Running in c4d22d0409cc
Traceback (most recent call last):
  File "/usr/lib/pypy3.10/runpy.py", line 199, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/pypy3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/usr/lib/python3/dist-packages/pip/__main__.py", line 19, in <module>
    sys.exit(_main())
             ^^^^^^^
  File "/usr/lib/python3/dist-packages/pip/_internal/cli/main.py", line 73, in main
    command = create_command(cmd_name, isolated=("--isolated" in cmd_args))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pip/_internal/commands/__init__.py", line 96, in create_command
    module = importlib.import_module(module_path)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/pypy3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<builtin>/frozen importlib._bootstrap_external", line 897, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/usr/lib/python3/dist-packages/pip/_internal/commands/install.py", line 24, in <module>
    from pip._internal.cli.req_command import RequirementCommand
  File "/usr/lib/python3/dist-packages/pip/_internal/cli/req_command.py", line 15, in <module>
    from pip._internal.index.package_finder import PackageFinder
  File "/usr/lib/python3/dist-packages/pip/_internal/index/package_finder.py", line 21, in <module>
    from pip._internal.index.collector import parse_links
  File "/usr/lib/python3/dist-packages/pip/_internal/index/collector.py", line 12, in <module>
    from pip._vendor import html5lib, requests
ImportError: cannot import name 'html5lib' from 'pip._vendor' (/usr/lib/python3/dist-packages/pip/_vendor/__init__.py)
The command '/bin/sh -c pypy3 -m pip install -r /sema-scdg/requirements_pypy.txt' returned a non-zero code: 1
make: *** [Makefile:30: run-toolchain] Error 1
```


原始信息来源: https://mp.weixin.qq.com/s/1iViyl4zqYTuL12CdC1RSQ  


2024/10/3  
