# gdb---设置基址

```r
Errata: Dealing with PIE

Position-Dependent Executables are loaded at a static address in memory.
Position-Independent Executables are not...

gdb tries to help by always loading them (depending on gdb and kernel version)
at 0x0000555555554000 or 0x7ffff7ffc000.

Easiest way to deal with this is to put this in your .gdbinit:
    set $base = 0x7ffff7ffc000

Afterwards, you can do stuff like:
    break *($base + 0x1023)
```

原始链接: https://pwn.college/intro-to-cybersecurity/reverse-engineering/


2025/5/18
