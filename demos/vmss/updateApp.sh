echo "message=VMSS Update 2" > /var/lib/mywebapp/docenv
docker kill webapp
docker rm webapp
docker run --name webapp -p 80:80 -d --restart always --env-file /var/lib/mywebapp/docenv twallace27603/inedemowebserver:latest
