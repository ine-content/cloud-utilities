apt update
apt install -y mariadb-server
systemctl start mariadb.service
mysql -e "GRANT ALL PRIVILEGES ON *.* to 'student@%' IDENTIFIED BY '\!NEPassw0rd\![]123';"
mysql -e "GRANT ALL PRIVILEGES ON *.* to 'student' IDENTIFIED BY '\!NEPassw0rd\![]123';"

sed -i -e 's/127.0.0.1/0.0.0.0/g' /etc/mysql/mariadb.conf.d/50-server.cnf
echo '[mysqld]' > /etc/my.cnf
echo 'skip-networking=0' >> /etc/my.cnf
echo 'skip-bind-address' >> /etc/my.cnf
systemctl restart mysql
