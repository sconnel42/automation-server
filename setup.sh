# Get my private ip address
myip=$(ifconfig | grep 'inet ' | cut -d ':' -f 2 | awk '{ print $2 }' | grep -E '^(192\.168\.[0-9]{0,3}\.[0-9]{0,3})')

# Copy over newest nginx config and restart service
cp config/automation-server /etc/nginx/sites-available/automation-server

if [ ! -f /etc/nginx/sites-enabled/automation-server ]; then
    ln -s /etc/nginx/sites-enabled/automation-server /etc/nginx/sites-available/automation-server
fi

sudo systemctl restart nginx
echo 'nginx restarted'

# Copy over latest uwsgi config and restart service
cp config/automation-server.service /etc/systemd/system/automation-server.service
sudo systemctl daemon-reload
sudo systemctl restart automation-server
echo 'uwsgi restarted'
