# Trivy

Trivy是一个安全扫描程序，扫描容器、git仓库等。

发音: tri is pronounced like trigger, vy is pronounced like envy.

官网: https://trivy.dev/  
github地址: https://github.com/aquasecurity/trivy

Targets (what Trivy can scan):
- Container Image
- Filesystem
- Git Repository (remote)
- Virtual Machine Image
- Kubernetes

Scanners (what Trivy can find there):
- OS packages and software dependencies in use (SBOM)
- Known vulnerabilities (CVEs)
- IaC issues and misconfigurations
- Sensitive information and secrets
- Software licenses


```powershell
# 默认会下载数据库，如果出错"failed to download vulnerability DB"，可以指定数据库地址下载
.\trivy.exe filesystem --db-repository ghcr.io/aquasecurity/trivy-db --download-db-only
# 扫文件夹
.\trivy.exe filesystem D:\hello_projects
```


信息来源: https://b23.tv/lwJtifw


2025/4/28
