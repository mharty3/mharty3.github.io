---
title: "Creating a bind mount into a docker container (docker)"
---
By default, data in a container does not persist when a running container is stopped. Also, it is difficult to get data out of a running container if it is needed by another process. 

One way to get around this is to store files on the host machine using a *bind mount*. (The other way is by using *volumes*, which are similar but have some important differences not discussed here.)

Bind mounts map an existing directory on the host machine to a directory in the container. Bind mounts are particularly useful when developing within a container. Any changes to the source code in a bind mounted directory on the host machine are immediately available within the container.

Bind mounts can be created either with the `-v`/`--volume` flag or with the `--mount` flag. It is recommended to use the `--mount` syntax.

```bash
docker run -d \
  -it \
  --name devtest \
  --mount type=bind,source="$(pwd)"/target,target=/app \
  nginx:latest
  ```

## From the [Docker docs](https://docs.docker.com/storage/bind-mounts/)
  --mount: Consists of multiple key-value pairs, separated by commas and each consisting of a <key>=<value> tuple. The --mount syntax is more verbose than -v or --volume, but the order of the keys is not significant, and the value of the flag is easier to understand.

 * The `type` of the mount, which can be `bind`, `volume`, or `tmpfs`. This topic discusses bind mounts, so the type is always bind.
 * The `source` of the mount. For bind mounts, this is the path to the file or directory on the Docker daemon host. May be specified as `source` or `src`.
 * The `destination` takes as its value the path where the file or directory is mounted in the container. May be specified as `destination`, `dst`, or `target`.
 * The `readonly` option, if present, causes the bind mount to be mounted into the container as read-only.
 * The `bind-propagation` option, if present, changes the bind propagation. May be one of `rprivate`, `private`, `rshared`, `shared`, `rslave`, `slave`.
 * The `--mount` flag does not support `z` or `Z` options for modifying selinux labels.


[Docker Docs storage overview](https://docs.docker.com/storage/)