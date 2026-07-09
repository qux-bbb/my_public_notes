# Wazuh Token 超时时间修改脚本
# 修改下面四个变量即可适配不同环境

WAZUH_IP = "192.168.116.150"     # Wazuh 服务器 IP
API_USER = "wazuh"               # API 用户名
API_PASS = "wazuh"               # API 密码
TOKEN_TIMEOUT = 86400            # Token 超时秒数（最小30秒，无上限；默认900=15分钟；86400=24小时）

# ====== 以下无需修改 ======
import urllib.request, json, ssl, base64

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Basic Auth 获取 Token
creds_b64 = base64.b64encode(f"{API_USER}:{API_PASS}".encode()).decode()
req = urllib.request.Request(f"https://{WAZUH_IP}:55000/security/user/authenticate")
req.add_header("Authorization", f"Basic {creds_b64}")
resp = urllib.request.urlopen(req, context=ctx, timeout=10)
token = json.loads(resp.read())["data"]["token"]

# 修改超时时间
body = json.dumps({"auth_token_exp_timeout": TOKEN_TIMEOUT}).encode()
req2 = urllib.request.Request(
    f"https://{WAZUH_IP}:55000/security/config",
    data=body, method="PUT"
)
req2.add_header("Authorization", f"Bearer {token}")
req2.add_header("Content-Type", "application/json")
resp2 = urllib.request.urlopen(req2, context=ctx, timeout=10)
print("配置更新:", json.loads(resp2.read())["message"])

# 重新认证验证
req3 = urllib.request.Request(f"https://{WAZUH_IP}:55000/security/user/authenticate")
req3.add_header("Authorization", f"Basic {creds_b64}")
resp3 = urllib.request.urlopen(req3, context=ctx, timeout=10)
token2 = json.loads(resp3.read())["data"]["token"]

req4 = urllib.request.Request(f"https://{WAZUH_IP}:55000/security/config")
req4.add_header("Authorization", f"Bearer {token2}")
resp4 = urllib.request.urlopen(req4, context=ctx, timeout=10)
cfg = json.loads(resp4.read())["data"]
print(f"当前 auth_token_exp_timeout: {cfg['auth_token_exp_timeout']} 秒 = {cfg['auth_token_exp_timeout']/3600:.0f} 小时")
