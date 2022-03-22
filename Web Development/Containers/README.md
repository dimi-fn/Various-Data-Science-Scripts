# Containers

Contents
===============
* [Docker](#docker)
* [Containers - Miscellaneous](#containers--miscellaneous)


------

# Docker

The purpose of containerization is to create a re-producable environment across your project application.

* [Docker Cheatsheet - options](https://www.docker.com/sites/default/files/d8/2019-09/docker-cheat-sheet.pdf)
* [What is the difference between a Docker image and a container?](https://stackoverflow.com/questions/23735149/what-is-the-difference-between-a-docker-image-and-a-container)
* [Virtual Machines (VMs) vs Containers](https://www.atlassian.com/continuous-delivery/microservices/containers-vs-vms)
    * *The key differentiator between containers and VMs is that VMs virtualize an entire machine down to the hardware layers and containers only virtualize software layers above the operating system level.*
        * Containers have no host operating system, so they are independent of the device they run on

<br>

* `Image`: set of layers
* `Container`: an instance of an image
    * You can have many running containers of the same image

<br>

* Accessing your local data in a container
    * via: `volumes`, `bind mounts`, or `tmpfs` (temporary files)
    * with detached mode (`-d`), or interactive mode (`-i`)
        * [Detached mode means that a container runs in the background](https://stackoverflow.com/questions/34029680/docker-detached-mode)

<br>

**Commands**

|Command | Description|
|-------|---------|
| `docker --help`| |
| `docker images` | display images|
|`docker rmi <image-id>`| remove an image|
|`docker ps`| display running containers|
|`docker ps -a`| display all containers (running and stopped ones)|
|`docker rm <container-id>`| remove a container|
|`docker system prune` |remove all containers|
|`docker system prune -a` |remove all docker items|
|`docker start <container-name-or-id>` (`-d` for detached mode, `-i` for interactive mode)| start a container|
|`docker stop <container-name-or-id>`|stop a container|
|`docker run <option> <image> <command>`||
|`docker run -it --name <option> ubuntu bash` | enter in ubuntu OS with a specified name |
|`docker pull`| e.g. docker pull node:version|
| *********************** | *********************** |
|`docker exec <name-of-container> <bash command>` |execute some stuff in a container|
|`docker exec -it <name-of-database> psql -U <POSTGRES_USER> <POSTGRES_DB>`| enter postgreSQL with docker|
| *********************** | *********************** |
|`docker-compose up`| start container|
| `docker-compose down`| stop container but maintain the data on the database|
| `docker-compose down --volumes --remove-orphans` | stop and remove all artifacts |
|`docker volume prune --force` |reclaim space from removing the volumes |


------

# Containers - Miscellaneous

* [Docker vs Kubernetes](https://www.freecodecamp.org/news/kubernetes-vs-docker-whats-the-difference-explained-with-examples/?fbclid=IwAR2jLOOMMYtHTH0yBU1xqecvXXXy8AWg7J27ySU_EX_cdzLzrJ-aEHMWPZI)

* [Kubernetes vs. Docker, by Azure](https://azure.microsoft.com/en-us/topic/kubernetes-vs-docker/)

* Docker
    * [Free Introduction to Docker eBook](https://devdojo.com/bobbyiliev/free-introduction-to-docker-ebook), [Intro to Docker - Opensource ebook by Bobby Iliev](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Web%20Development/Containers/introduction-to-docker-dark.pdf)
