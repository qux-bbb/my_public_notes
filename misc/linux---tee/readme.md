# linux---tee

```r
Usage: tee [OPTION]... [FILE]...
Copy standard input to each FILE, and also to standard output.
```

The tee command, named after a "T-splitter" from plumbing pipes, duplicates data flowing through your pipes to any number of files provided on the command line.  


Copy `stdin` to each file, and also to `stdout`:  
```bash
echo "example" | tee path/to/file
```


参考链接：  
https://pwn.college/linux-luminarium/piping/  
tldr  


2024/10/17  
