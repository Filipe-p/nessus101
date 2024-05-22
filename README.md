# Tenable / Nessus 101

This repo is to explore Tenable 101. We needed a testing environment so we can run experiemnts and not disrupt ongoing scans of active infrastructure. For this the best we can do is create a local Dev Environment that is easy to setup. 

References: https://www.tenable.com/downloads/nessus?_gl=1*16tobqy*_ga*MTU2MTM4NDcxNi4xNzE2MTk2MzM5*_ga_HSJ1XWV6ND*MTcxNjM4NTk3Mi41LjEuMTcxNjM4NTk3NS41Ny4wLjMxODQwMjQ0Mw


### Pre requisists

- Docker Installed
Or
- Podman Installed

Note: As docker desktop is not longer open source & running a deamon has become convoluted we'll be using `podman`

### Instalation

Follow and choose 

```python 
# run this to pull an image with tennable 
# $ docker pull tenable/nessus:(version-OS) #ubuntu or oracle
#$ docker pull tenable/nessus:latest-ubuntu
# or
#$ docker pull tenable/nessus

$ podman pull docker.io/tenable/nessus:latest-ubuntu

$ podman run -dt -p 8834:8834 docker.io/tenable/nessus:latest-ubuntu

# see intance here: 
https://0.0.0.0:8834/#/

# Register for Nessus Essentials to get activation key
https://tenable.com/products/nessus/nessus-essentials

```


## Podman Notes

Side notes on `podman` commands just as refresher.

```python
#exec inter active terminal to running container
$ podman exec -it  1489aff68f32 /bin/bash

```