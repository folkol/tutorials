$ brew install docker
$ cat Dockerfile
FROM fedora
RUN yum install mongodb
EXPOSE 22 27017 27018 27019 28017

Start docker?


$ docker build -t folkol/mongo .