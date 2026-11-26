# wget

wget用于下载文件。

比较好用的添加了一些选项的方式
```bash
wget --continue --tries=3 --timeout=30 --content-disposition your_url
# --continue：断点续传，继续下载未完成的部分
# --tries=3：设置失败重试次数为 3 次
# --timeout=30：设置网络超时时间为 30 秒
# --content-disposition：根据服务器返回的 Content-Disposition 头确定保存文件名
```
