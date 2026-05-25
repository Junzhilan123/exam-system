#!/bin/bash
# 在阿里云 ECS（Ubuntu/CentOS）上一键部署 exam-system
# 用法（在 ECS 上执行）:
#   curl -fsSL https://raw.githubusercontent.com/Junzhilan123/exam-system/main/deploy/aliyun-ecs-install.sh | bash
# 或:
#   git clone https://github.com/Junzhilan123/exam-system.git && cd exam-system && bash deploy/aliyun-ecs-install.sh

set -euo pipefail

APP_DIR="${APP_DIR:-/opt/exam-system}"
REPO="${REPO:-https://github.com/Junzhilan123/exam-system.git}"
BRANCH="${BRANCH:-main}"

echo "==> 安装 Docker..."
if ! command -v docker &>/dev/null; then
  if [ -f /etc/redhat-release ]; then
    yum install -y yum-utils
    yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    yum install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
  else
    apt-get update
    apt-get install -y ca-certificates curl gnupg
    install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" > /etc/apt/sources.list.d/docker.list
    apt-get update
    apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
  fi
  systemctl enable docker
  systemctl start docker
fi

echo "==> 拉取代码到 ${APP_DIR}..."
if [ -d "$APP_DIR/.git" ]; then
  cd "$APP_DIR"
  git fetch origin
  git checkout "$BRANCH"
  git pull origin "$BRANCH"
else
  git clone -b "$BRANCH" "$REPO" "$APP_DIR"
  cd "$APP_DIR"
fi

echo "==> 配置环境变量..."
if [ ! -f .env ]; then
  cp .env.example .env
  SECRET=$(python3 -c "import secrets; print(secrets.token_hex(32))" 2>/dev/null || openssl rand -hex 32)
  sed -i "s/change-me-to-a-random-string/${SECRET}/" .env
  sed -i "s/TEACHER_PASSWORD=change-me/TEACHER_PASSWORD=$(openssl rand -hex 8)/" .env
  echo "已生成 .env，教师密码见: grep TEACHER_PASSWORD .env"
fi

echo "==> 启动服务（国内镜像）..."
docker compose -f docker-compose.yml -f docker-compose.cn.yml up -d --build

echo ""
echo "=========================================="
echo " 部署完成！"
echo " 访问: http://$(curl -s --max-time 3 ifconfig.me 2>/dev/null || hostname -I | awk '{print $1}'):80"
echo " 教师后台: /teacher"
echo " 数据目录: docker volume exam-system_exam_data"
echo "=========================================="
docker compose ps
