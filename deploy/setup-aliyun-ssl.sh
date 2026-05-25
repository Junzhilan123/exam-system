#!/bin/sh
# 使用阿里云 SSL 证书启用 HTTPS
# 1. 在阿里云控制台下载 Nginx 格式证书
# 2. 将 .pem 证书重命名为 fullchain.pem，.key 重命名为 privkey.pem
# 3. 放入 deploy/ssl/ 目录后运行本脚本
# 用法: ./deploy/setup-aliyun-ssl.sh your.domain.com

set -eu

DOMAIN="${1:-}"

if [ -z "$DOMAIN" ]; then
  echo "用法: $0 <域名>"
  echo "示例: $0 exam.example.com"
  exit 1
fi

cd "$(dirname "$0")/.."

if [ ! -f deploy/ssl/fullchain.pem ] || [ ! -f deploy/ssl/privkey.pem ]; then
  echo "错误: 请先将证书放入 deploy/ssl/ 目录:"
  echo "  deploy/ssl/fullchain.pem  (证书链)"
  echo "  deploy/ssl/privkey.pem    (私钥)"
  exit 1
fi

echo "==> 生成 Nginx SSL 配置..."
sed "s/__DOMAIN__/$DOMAIN/g" deploy/nginx.aliyun.conf.template > deploy/nginx.ssl.conf

echo "==> 启动 HTTPS 服务..."
export NGINX_CONF=./deploy/nginx.ssl.conf
docker compose up -d

echo ""
echo "完成！请访问: https://$DOMAIN"
