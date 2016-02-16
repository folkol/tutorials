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
