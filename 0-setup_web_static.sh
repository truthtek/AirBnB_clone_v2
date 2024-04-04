#!/usr/bin/env bash
# This script sets up web servers for deployment of web_static

# Install Nginx if not already installed
if ! dpkg -s nginx >/dev/null 2>&1; then
    apt-get update
    apt-get -y install nginx
fi

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create or recreate symbolic link
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership of /data/ folder to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
sed -i '/^\s*location \/hbnb_static\/ {/a \
        alias /data/web_static/current/;' "$config_file"

# Restart Nginx
service nginx restart

exit 0
