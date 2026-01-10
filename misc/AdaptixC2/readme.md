# AdaptixC2

AdaptixC2是一个类似CobaltStrike的工具，可以列文件、看进程、执行命令

https://github.com/Adaptix-Framework/AdaptixC2

需要自己编译，可以用github action自动化编译(可生成服务端和Linux客户端，无法生成Windows客户端)，编译后下载dist-files即可
```yml
name: build binary

on:
  workflow_dispatch:

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - name: configure
      run: chmod +x pre_install_linux_all.sh && sudo ./pre_install_linux_all.sh all
    - name: make server
      run: make server-ext
    - name: make client
      run: make client
    - name: Upload a Build Artifact
      uses: actions/upload-artifact@v6.0.0
      with:
        name: dist-files
        path: dist
```

Listener的Config选择Beacon时只支持Windows，选择Gopher时支持Windows、Linux、MacOS，但是当前无法生成agent


信息来源: https://mp.weixin.qq.com/s/ZGkUIdeMo9KfjPCz1bzZaw
