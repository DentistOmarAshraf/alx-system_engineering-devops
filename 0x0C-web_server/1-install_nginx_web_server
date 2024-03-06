#!/usr/bin/env bash
# Update apt and install nginx

apt update -y
apt install nginx -y

echo "Hello World!" | tee /var/www/html/index.nginx-debian.html

systemctl start nginx
