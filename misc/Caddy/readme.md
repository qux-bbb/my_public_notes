# Caddy

keywords: nginx 反向代理

Caddy is a powerful, extensible platform to serve your sites, services, and apps, written in Go. 

官网: https://caddyserver.com/

Caddyfile配置示例：
```json
:11435 {
    @valid_token {
        header Authorization "Bearer your-secret-token-here"
    }

    @allowed_paths {
        path / /v1/chat/completions /api/version /api/tags /api/ps
    }

    handle @valid_token {
        handle @allowed_paths {
            reverse_proxy localhost:11434
        }

        handle {
            respond "Forbidden - Path not allowed" 403
        }
    }

    handle {
        respond "Unauthorized" 401
    }
}
```

请求示例：
```bash
# 应该代理成功
curl -H "Authorization: Bearer your-secret-token-here" http://localhost:11435/
# 没有token，应该返回 401
curl http://localhost:11435/
```
