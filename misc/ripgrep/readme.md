# rg

ripgrep可以用来搜索文件内容，和grep相比，速度更快，效果更好  

https://github.com/BurntSushi/ripgrep  

使用：
```r
rg [OPTIONS] PATTERN [PATH ...]

    --binary
        Enabling this flag will cause ripgrep to search binary files. By
        default, ripgrep attempts to automatically skip binary files in order
        to improve the relevance of results and make the search faster.

    -u, --unrestricted
        This flag reduces the level of "smart" filtering. Repeated uses (up to
        3) reduces the filtering even more. When repeated three times, ripgrep
        will search every file in a directory tree.

        A single -u/--unrestricted flag is equivalent to --no-ignore. Two
        -u/--unrestricted flags is equivalent to --no-ignore -./--hidden. Three
        -u/--unrestricted flags is equivalent to --no-ignore -./--hidden
        --binary.

        The only filtering ripgrep still does when -uuu is given is to skip
        symbolic links and to avoid printing matches from binary files.
        Symbolic links can be followed via the -L/--follow flag, and binary
        files can be treated as text files via the -a/--text flag.

    -A NUM, --after-context=NUM
        Show NUM lines after each match.

        This overrides the --passthru flag and partially overrides the
        -C/--context flag.

    -B NUM, --before-context=NUM
        Show NUM lines before each match.

        This overrides the --passthru flag and partially overrides the
        -C/--context flag.
```

示例：
```r
# 当前文件夹下的所有文件，搜索"hello"
rg -uuu hello

# 搜索"hello"，结果显示之前3行、之后2行
rg -B 3 -A 2 hello
```
