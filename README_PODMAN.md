
## Podman Notes

Side notes on `podman` commands just as refresher.

```python
#exec inter active terminal to running container
$ podman exec -it  1489aff68f32 /bin/bash


podman exec -it  809e4e6a0296 /bin/bash
## Adding memory to podman

podman machine stop
podman machine set --cpus 5 --memory 5120
podman machine start


## Container specific memory
# https://jasebell.medium.com/understanding-memory-management-in-containers-with-podman-e916ea9039df

$ podman run -dt --name tenable_2 -m 5120m -p 8834:8834 docker.io/tenable/nessus:latest-ubuntu


```