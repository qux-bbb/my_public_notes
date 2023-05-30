# linuxbrew安装方法

```
安装 Linuxbrew

在安装 Linuxbrew 之前，需要先准备好依赖：

Debian/Ubuntu：

% sudo apt-get install build-essential curl git ruby libbz2-dev \
libcurl4-openssl-dev libexpat-dev libncurses-dev zlib1g-dev


Fedora：

% sudo yum groupinstall 'Development Tools' && sudo yum install \
curl git ruby bzip2-devel curl-devel expat-devel ncurses-devel zlib-devel


接着，将 Linuxbrew 从 GitHub clone 下来：

% git clone https://github.com/Homebrew/linuxbrew.git ~/.linuxbrew


并将下列内容添加到 ~/.bashrc 或 ~/.zshrc：

export PATH="$HOME/.linuxbrew/bin:$PATH"
export LD_LIBRARY_PATH="$HOME/.linuxbrew/lib:$LD_LIBRARY_PATH"


然后执行：

% source ~/.bashrc


或：

% source ~/.zshrc


这样子 Linuxbrew 就算装好了。

使用 Linuxbrew

通过 brew help 可以了解 Linuxbrew 的基本用法，例如：

% brew search <pkg>    # 搜索包
% brew install <pkg>   # 安装包
% brew uninstall <pkg> # 删除包
% brew list <pkg>      # 列出 pkg 的文件
% brew info <pkg>      # 关于 pkg 的信息
% brew update          # 更新包
% brew upgrade <pkg>   # 升级包


关于 Linuxbrew 更详细的用法，可执行 man brew 查阅

原文地址：http://www.lupaworld.com/article-236706-1.html
```


2016/11/10  
