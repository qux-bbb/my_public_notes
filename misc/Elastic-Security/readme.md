# Elastic Security

> Elastic Security 是 Elastic Stack 内置的免费安全检测平台。通过 Agent 采集端点数据 → Fleet 集中管理 → Elasticsearch 存储分析 → Kibana Security 面板统一查看告警。支持自定义检测规则（KQL/EQL）、800+ 预置规则、MITRE ATT&CK 映射、实时告警与事件调查。

用Hermes可以快速安装使用

## 文档
| 文档 | 链接 |
|------|------|
| Elastic Stack 安装指南 | https://www.elastic.co/docs/deploy-manage/deploy/self-managed/installing-elasticsearch |
| Elasticsearch 参考指南 | https://www.elastic.co/docs/reference/elasticsearch |
| Kibana 指南 | https://www.elastic.co/docs/reference/kibana |
| Fleet & Agent 指南 | https://www.elastic.co/docs/reference/fleet |
| Elastic Security 指南 | https://www.elastic.co/docs/solutions/security |
| 检测规则创建 | https://www.elastic.co/docs/solutions/security/detect-and-alert/using-the-rule-ui |
| 预置规则列表 | https://www.elastic.co/guide/en/security/current/prebuilt-rules.html |
| EQL 查询语言 | https://www.elastic.co/docs/explore-analyze/query-filter/languages/eql |
| KQL 查询语言 | https://www.elastic.co/docs/explore-analyze/query-filter/languages/kql |

---

## 架构与组件

```
┌───────────────────────────────────────────────────────────────┐
│                    Elastic Stack 架构                          │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────┐    ┌──────────────┐    ┌──────────────┐             │
│  │Agent│───►│ Fleet Server │───►│Elasticsearch │             │
│  │     │    │(Agent管理)   │    │(存储+检索引擎)│             │
│  └─────┘    └──────────────┘    └──────┬───────┘             │
│                                        │                      │
│                                  ┌─────▼───────┐             │
│                                  │   Kibana     │             │
│                                  │(可视化+管理)  │             │
│                                  └─────────────┘             │
│                                       │                       │
│                                  ┌────▼────┐                 │
│                                  │Security │                 │
│                                  │ 面板     │                 │
│                                  └─────────┘                 │
└───────────────────────────────────────────────────────────────┘
```

## 一些注意点
```
默认只会定期采集进程列表，且有top限制，实时监控进程创建需要额外配置，获取进程命令行需要额外配置

Wazuh有比较方便使用的资产管理功能，Elastic Security查看统计日志更灵活
```

---

## Kibana 界面改中文

编辑 `kibana.yml`（路径取决于安装方式）：

| 安装方式 | 配置文件路径 |
|---------|------------|
| RPM/DEB 包 | `/etc/kibana/kibana.yml` |
| Tarball | `<kibana安装目录>/config/kibana.yml` |
| Docker | 挂载卷中的配置 |

添加一行：

```yaml
i18n.locale: "zh-CN"
```

重启 Kibana 后整个 UI（包括 Elastic Security 面板）即变为简体中文。

```bash
# systemd 方式
sudo systemctl restart kibana

# tarball 方式
# 先 kill 进程再重新启动 bin/kibana
```

> ⚠ 如果只看到部分中文，清除浏览器缓存再刷新。
