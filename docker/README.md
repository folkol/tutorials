Previously:

brew cask install virtualbox
brew install docker
(brew install go)
brew install boot2docker
boot2docker init
boot2docker up

eval "$(boot2docker shellinit)

docker run -i -t ubuntu /bin/bash


Good-to-knows:
Docker keep a local repository for images
Docker relies on Linux kernel modules, so it won't run on Mac natively -- boot2docker for VirtualBox



Now:

 - brew update
 - brew install boot2docker
 - brew install Caskroom/cask/dockertoolbox
 - Start 'Docker Quickstart Terminal'
 - DID NOT WORK

Now, without brew:
 - https://www.docker.com/products/docker-toolbox
 - Download for mac
 - 

Docker toolbox:
 - Docker CLI client for running Docker Engine to create images and containers
 - Docker Machine so you can run Docker Engine commands from Mac OS X terminals
 - Docker Compose for running the docker-compose command
 - Kitematic, the Docker GUI
 - the Docker QuickStart shell preconfigured for a Docker command-line environment
 - Oracle VM VirtualBox

or...

 - Docker Machine for running the docker-machine binary
 - Docker Engine for running the docker binary
 - Docker Compose for running the docker-compose binary
 - Kitematic, the Docker GUI
 - a shell preconfigured for a Docker command-line environment
 - Oracle VM VirtualBox


Normal shell:
 - docker-machine create --driver virtualbox default
 - eval $(docker-machine env default)
 - docker-machine start / stop
 - docker-machine ls
 - docker-machine --help

 - docker run -d -P --name web nginx # -d for daemon/keepalive, -P for publish ports
 - docker ps # List containers
 - docker port web # View exposed ports
 - docker-machine ip # ip of Docker host
 - docker stop web
 - docker rm web

 - When you start a container, docker automatically shares your /Users/username dir.
 - docker run -d -P -v $HOME/site:/usr/share/nginx/html --name mysite nginx

In short:
docker-machine to interact with the virtual linux docker host
docker to inteact with the docker daemon
the exposed ports are exposed on the DOCKER HOST!



List containers:
 - docker ps -a


Standalone MongoDB with docker:
 - docker run --name some-mongo -d mongo
( - docker attach some-mongo # If you want to login to the machine, and the container was started as a shell )
 - docker exec -it some-mongo bash # run bash in container, with streams connected to this terminal
 - docker stop some-mongo
 - docker rm some-mongo

Mongo example:
 - docker run -P --name mongo_1 -d mongo
 - docker run -it --link mongo_1:mongo --rm mongo sh -c 'exec mongo "$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT/test"'

 - docker run --name some-app --link some-mongo:mongo -d application-that-uses-mongo



Log in to docker host:
 - docker-machine ssh


Demo with temporary MongoDB:
 - docker run -d -P mongo
 - docker ps # e0f04a0bac97        mongo               "/entrypoint.sh mongo"   14 minutes ago      Up 14 minutes       0.0.0.0:32775->27017/tcp   mongo_1
 - mongo $(docker-machine ip):32775
 - use smartcms
 - db.cloneDatabse("192.168.1.212"); // Might require net: bindIp: 0.0.0.0
 - db.clicks.find()






boot2docker vs. docker-machine:

boot2docker docker-machine      docker-machine description
init        create              Creates a new docker host.
up          start               Starts a stopped machine.
ssh         ssh                 Runs a command or interactive ssh session on the machine.
save        -                   Not applicable.
down        stop                Stops a running machine.
poweroff    stop                Stops a running machine.
reset       restart             Restarts a running machine.
config      inspect             Prints machine configuration details.
status      ls                  Lists all machines and their status.
info        inspect             Displays a machine’s details.
ip          ip                  Displays the machine’s ip address.
shellinit   env                 Displays shell commands needed to configure your shell to interact with a machine
delete      rm                  Removes a machine.
download    -                   Not applicable.
upgrade     upgrade             Upgrades a machine’s Docker client to the latest stable release.


References:
 - http://penandpants.com/2014/03/09/docker-via-homebrew/
 - https://docs.docker.com/mac/step_one/

Reading list:
 - Docker compose (multi container apps)
 - https://docs.oracle.com/cd/E52668_01/E54669/html/section_rsr_p2z_fp.html
 - https://docs.docker.com/engine/examples/mongodb/
 - http://blog.trifork.com/2013/12/24/docker-from-a-distance-the-remote-api/
