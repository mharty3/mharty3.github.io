---
title: 'Attach shell to running container (docker)'
---
To attach a shell to a running container, first find the container name or id by running:

`docker ps` or `docker container ls`

Then execute the bash command in interactive mode (`-i`) and pseudo-TTY mode (`-t`).

`docker exec -i -t <container name/id> /bin/bash`

Note, if the container is built on Alpine Linux, it will not have bash installed, use `/bin/sh` instead.