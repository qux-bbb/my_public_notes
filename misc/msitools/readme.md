# msitools

msitools 是 GNOME 项目提供的开源工具集，专门用于操作 MSI 文件。

项目地址: https://gitlab.gnome.org/GNOME/msitools

安装：
```bash
sudo apt install msitools
```

批量提取表内容：
```bash
msi_path=hello.msi
mkdir msi_tables  # 创建目录
msiinfo tables $msi_path | while read table; do
    echo "Exporting table $table..."
    msiinfo export $msi_path "$table" > "msi_tables/${table}.txt"
done
```


2025/4/5
