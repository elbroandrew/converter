FROM mysql:latest

# Set environment variables for MySQL, remove in future!
ENV MYSQL_DATABASE=auth_db
ENV MYSQL_USER=username
ENV MYSQL_PASSWORD=passwd
ENV MYSQL_ROOT_PASSWORD=rootpaswd

#COPY data.sql /docker-entrypoint-initdb.d/
VOLUME [ "mysql/data" ]

EXPOSE 3306