Caveats:
 - Does not work native on Mac
 - 

$ brew install docker
$ cat Dockerfile
FROM fedora
RUN yum install mongodb
EXPOSE 22 27017 27018 27019 28017

Start docker?


$ docker build -t folkol/mongo .

docker run -dP --name slave1 mongo --replSet "rs0"
docker run -dP --name slave2 mongo --replSet "rs0"

-- in mongod.conf --
replication:
   oplogSizeMB: <int>
   replSetName: <string>
   secondaryIndexPrefetch: <string>
   enableMajorityReadConcern: <boolean>

mongo
rs.initiate()
rs.conf()


rs.add('192.168.99.100:32781'); // and slave 2
