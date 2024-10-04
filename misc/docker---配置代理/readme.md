# docker---配置代理

如果遇到这样的错误，果断配置代理就可以了  
```r
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
docker: Error response from daemon: Get "https://registry-1.docker.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers).
See 'docker run --help'.
```

```r
sudo tee /etc/docker/daemon.json << EOF
{
  "proxies": {
    "http-proxy": "socks5://127.0.0.1:20170",
    "https-proxy": "socks5://127.0.0.1:20170",
    "no-proxy": "127.0.0.0/8"
  }
}
EOF

sudo systemctl restart docker
```


参考链接: https://xiaowangye.org/posts/china-docker-registry-proxy-guide/#3docker-客户端代理配置  


2024/10/4  
