gitRoot="https://raw.githubusercontent.com/Internetworkexpert/cloud-utilities/main"
serverUrl="$gitRoot/pythonWebServer.py"
serviceUrl="$gitRoot/pythonapi.service"
serverFile="/usr/local/bin/pythonWebServer.py"
serviceFile="/etc/systemd/system/pythonweb.service"
wget -O $serverFile $serverUrl
wget -O $serviceFile $serviceUrl
chmod 777 $serverFile
chmod 677 $serviceFile
systemctl daemon-reload
systemctl enable pythonweb.service
systemctl start pythonweb.service
