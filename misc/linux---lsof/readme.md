# linux---lsof

keywords: 端口找进程 文件找进程  

列出打开的文件和相应的进程  

> Lists open files and the corresponding processes.
> Note: Root privileges (or sudo) is required to list files opened by others.

Find the processes that have a given file open:  
`lsof {{path/to/file}}`  

Find the process that opened a local internet port:  
`lsof -i :{{port}}`  

Only output the process ID (PID):  
`lsof -t {{path/to/file}}`  

List files opened by the given user:  
`lsof -u {{username}}`  

List files opened by the given command or process:  
`lsof -c {{process_or_command_name}}`  

List files opened by a specific process, given its PID:  
`lsof -p {{PID}}`  

List open files in a directory:  
`lsof +D {{path/to/directory}}`  

Find the process that is listening on a local TCP port:  
`lsof -iTCP:{{port}} -sTCP:LISTEN`  


原链接: https://github.com/tldr-pages/tldr/blob/master/pages/common/lsof.md  


2021/9/11  
