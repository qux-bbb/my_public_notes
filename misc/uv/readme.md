# uv

uv是一个python包和项目管理工具，使用Rust编写。  
优势是快，可以很方便地管理多个python版本。

官网: https://docs.astral.sh/uv/

国内用pipx、pip安装比较方便：
```bash
pipx install uv
pip install uv
```

有一些典型的使用场景


## 创建一个虚拟环境
最新版python虚拟环境：
```bash
uv venv myenv
```

指定版本python虚拟环境：
```bash
uv venv myenv --python 3.9
```

激活虚拟环境后，可以使用 `uv pip install requests` 这样的命令安装依赖


## 创建一个项目
使用本地默认的python版本或uv维护的最新的python版本创建一个项目
```bash
uv init myproject
```

指定python版本创建一个项目
```bash
uv init myproject --python=3.7
```

可以进入项目文件夹使用 `uv add requests` 这样的命令安装依赖


## 临时修改源
```bash
uv init myproject --python=3.9 --index-url https://pypi.tuna.tsinghua.edu.cn/simple
```


---
2025/3/17
