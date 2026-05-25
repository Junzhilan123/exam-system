#!/bin/sh
# 使用 Let's Encrypt 免费证书启用 HTTPS
# 用法: ./deploy/init-letsencrypt.sh your.domain.com admin@your.domain.com

set -eu

DOMAIN="${1:-}"
EMAIL="${2:-}"

if [ -z "$DOMAIN" ] || [ -z "$EMAIL" ]; then
  echo "用法: $0 <域名> <邮箱>"
  echo "示例: $0 exam.example.com admin@example.com"
  exit 1
fi

cd "$(dirname "$0")/.."

echo "==> 确保服务已启动 (HTTP 模式)..."
docker compose up -d redis app nginx

echo "==> 申请证书..."
docker compose run --rm certbot certonly \
  --webroot \
  --webroot-path=/var/www/certbot \
  --email "$EMAIL" \
  --agree-tos \
  --no-eff-email \
  -d "$DOMAIN"

echo "==> 生成 Nginx SSL 配置..."
sed "s/__DOMAIN__/$DOMAIN/g" deploy/nginx.letsencrypt.conf.template > deploy/nginx.ssl.conf

echo "==> 切换 Nginx 到 HTTPS..."
export NGINX_CONF=./deploy/nginx.ssl.conf
docker compose up -d nginx certbot

echo ""
echo "完成！请访问: https://$DOMAIN"
echo "证书将每 12 小时自动检查续期。"
