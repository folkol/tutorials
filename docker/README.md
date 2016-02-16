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




References:
 - http://penandpants.com/2014/03/09/docker-via-homebrew/
 - https://docs.docker.com/mac/step_one/

Reading list:
 - Docker compose (multi container apps)
