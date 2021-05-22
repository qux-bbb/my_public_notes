# vim简单配置

编辑  `/etc/vim/vimrc` 文件即可(这个文件的 注释行 为双引号 " )  
也可以只设置本用户的vim配置： `touch ~/.vimrc`  

我设置了这些东西  
```config
" tab缩进为4个空格
set tabstop=4
" 自动缩进为4个空格
set shiftwidth=4 
" 用空格代替tab
set expandtab
" 设置行号
set number
" 突出显示当前行
set cursorline
" 开启新行时使用智能自动缩进
set  smartindent
" 自动语法高亮
syntax on
" 开启即时搜索
set incsearch
" 搜索结果高亮
set hlsearch
" 总是显示状态栏(可以看到文件名)
set laststatus=2
" 设置折叠方式
set foldmethod=indent
" 设置默认不折叠
set foldlevelstart=99
```


2020/08/26  
