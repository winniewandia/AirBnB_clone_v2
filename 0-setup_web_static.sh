#!/usr/bin/env bash
# install Nginx

apt-get -y update
apt-get -y install nginx
service nginx start
mkdir /data/
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/releases/test/
mkdir /data/web_static/shared/
echo "Hello World!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '40i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
exit 0
