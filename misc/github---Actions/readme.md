# github---Actions

github的Actions可以自动化发起测试、部署流程。  

最简单的使用方法：  
在项目首页切换到"Actions"标签页，选择相应的工作流，改改内容提交就好了  
右边的文档有一些提示，应该做什么，可以填什么值之类的  

一个简单的例子：
```yml
name: build binary

on:
  workflow_dispatch:  # 手动触发

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - name: prepare
      run: chmod +x pre_install.sh && sudo ./pre_install.sh
    - name: make client
      run: make client
    - name: Upload a Build Artifact  # 将需要的文件传出来
      uses: actions/upload-artifact@v6.0.0
      with:
        name: dist-files
        path: dist
```

我用了"Python application"，可以自动化运行测试功能  
