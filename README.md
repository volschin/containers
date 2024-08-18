<!---
NOTE: AUTO-GENERATED FILE
to edit this file, instead edit its template at: ./github/scripts/templates/README.md.j2
-->
<div align="center">


## Containers

_An opinionated collection of container images_

</div>

<div align="center">

![GitHub Repo stars](https://img.shields.io/github/stars/onedr0p/containers?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/onedr0p/containers?style=for-the-badge)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/onedr0p/containers/release-scheduled.yaml?style=for-the-badge&label=Scheduled%20Release)

</div>

Welcome to my container images, if looking for a container start by [browsing the GitHub Packages page for this repo's packages](https://github.com/onedr0p?tab=packages&repo_name=containers).

## Mission statement

The goal of this project is to support [semantically versioned](https://semver.org/), [rootless](https://rootlesscontaine.rs/), and [multiple architecture](https://www.docker.com/blog/multi-arch-build-and-images-the-simple-way/) containers for various applications.

It also adheres to a [KISS principle](https://en.wikipedia.org/wiki/KISS_principle), logging to stdout, [one process per container](https://testdriven.io/tips/59de3279-4a2d-4556-9cd0-b444249ed31e/), no [s6-overlay](https://github.com/just-containers/s6-overlay) and all images are built on top of [Alpine](https://hub.docker.com/_/alpine) or [Ubuntu](https://hub.docker.com/_/ubuntu).

## Tag immutability

The containers built here do not use immutable tags, as least not in the more common way you have seen from [linuxserver.io](https://fleet.linuxserver.io/) or [Bitnami](https://bitnami.com/stacks/containers).

We do take a similar approach but instead of appending a `-ls69` or `-r420` prefix to the tag we instead insist on pinning to the sha256 digest of the image, while this is not as pretty it is just as functional in making the images immutable.

| Container                                          | Immutable |
|----------------------------------------------------|-----------|
| `ghcr.io/onedr0p/sonarr:rolling`                   | ❌         |
| `ghcr.io/onedr0p/sonarr:3.0.8.1507`                | ❌         |
| `ghcr.io/onedr0p/sonarr:rolling@sha256:8053...`    | ✅         |
| `ghcr.io/onedr0p/sonarr:3.0.8.1507@sha256:8053...` | ✅         |

_If pinning an image to the sha256 digest, tools like [Renovate](https://github.com/renovatebot/renovate) support updating the container on a digest or application version change._

## Rootless

To run these containers as non-root make sure you update your configuration to the user and group you want.

### Docker compose

```yaml
networks:
  sonarr:
    name: sonarr
    external: true
services:
  sonarr:
    image: ghcr.io/onedr0p/sonarr:3.0.8.1507
    container_name: sonarr
    user: 65534:65534
    # ...
```

### Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sonarr
# ...
spec:
  # ...
  template:
    # ...
    spec:
      # ...
      securityContext:
        runAsUser: 65534
        runAsGroup: 65534
        fsGroup: 65534
        fsGroupChangePolicy: OnRootMismatch
# ...
```

## Passing arguments to a application

Some applications do not support defining configuration via environment variables and instead only allow certain config to be set in the command line arguments for the app. To circumvent this, for applications that have an `entrypoint.sh` read below.

1. First read the Kubernetes docs on [defining command and arguments for a Container](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/).
2. Look up the documentation for the application and find a argument you would like to set.
3. Set the argument in the `args` section, be sure to include `entrypoint.sh` as the first arg and any application specific arguments thereafter.

    ```yaml
    args:
      - /entrypoint.sh
      - --port
      - "8080"
    ```

## Configuration volume

For applications that need to have persistent configuration data the config volume is hardcoded to `/config` inside the container. This is not able to be changed in most cases.

## Available Images

Each Image will be built with a `rolling` tag, along with tags specific to it's version. Available Images Below

Container | Channel | Image | Latest Tags
--- | --- | --- | ---
[actions-runner](https://github.com/volschin/containers/pkgs/container/actions-runner) | stable | ghcr.io/volschin/actions-runner |![2](https://img.shields.io/badge/2-blue?style=flat-square) ![2.319](https://img.shields.io/badge/2.319-blue?style=flat-square) ![2.319.1](https://img.shields.io/badge/2.319.1-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[bazarr](https://github.com/volschin/containers/pkgs/container/bazarr) | stable | ghcr.io/volschin/bazarr |![1](https://img.shields.io/badge/1-blue?style=flat-square) ![1.4](https://img.shields.io/badge/1.4-blue?style=flat-square) ![1.4.3](https://img.shields.io/badge/1.4.3-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[calibre-web](https://github.com/volschin/containers/pkgs/container/calibre-web) | stable | ghcr.io/volschin/calibre-web |![0](https://img.shields.io/badge/0-blue?style=flat-square) ![0.6](https://img.shields.io/badge/0.6-blue?style=flat-square) ![0.6.23](https://img.shields.io/badge/0.6.23-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[home-assistant](https://github.com/volschin/containers/pkgs/container/home-assistant) | stable | ghcr.io/volschin/home-assistant |![2024.8.2](https://img.shields.io/badge/2024.8.2-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[jbops](https://github.com/volschin/containers/pkgs/container/jbops) | stable | ghcr.io/volschin/jbops |![1](https://img.shields.io/badge/1-blue?style=flat-square) ![1.0](https://img.shields.io/badge/1.0-blue?style=flat-square) ![1.0.893](https://img.shields.io/badge/1.0.893-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[lidarr](https://github.com/volschin/containers/pkgs/container/lidarr) | master | ghcr.io/volschin/lidarr |![2](https://img.shields.io/badge/2-blue?style=flat-square) ![2.4](https://img.shields.io/badge/2.4-blue?style=flat-square) ![2.4.3](https://img.shields.io/badge/2.4.3-blue?style=flat-square) ![2.4.3.4248](https://img.shields.io/badge/2.4.3.4248-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[lidarr-develop](https://github.com/volschin/containers/pkgs/container/lidarr-develop) | develop | ghcr.io/volschin/lidarr-develop |![2](https://img.shields.io/badge/2-blue?style=flat-square) ![2.5](https://img.shields.io/badge/2.5-blue?style=flat-square) ![2.5.1](https://img.shields.io/badge/2.5.1-blue?style=flat-square) ![2.5.1.4311](https://img.shields.io/badge/2.5.1.4311-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[par2cmdline-turbo](https://github.com/volschin/containers/pkgs/container/par2cmdline-turbo) | stable | ghcr.io/volschin/par2cmdline-turbo |![1.1.1](https://img.shields.io/badge/1.1.1-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[postgres-init](https://github.com/volschin/containers/pkgs/container/postgres-init) | stable | ghcr.io/volschin/postgres-init |![16](https://img.shields.io/badge/16-blue?style=flat-square) ![16.3](https://img.shields.io/badge/16.3-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[prowlarr](https://github.com/volschin/containers/pkgs/container/prowlarr) | master | ghcr.io/volschin/prowlarr |![1](https://img.shields.io/badge/1-blue?style=flat-square) ![1.21](https://img.shields.io/badge/1.21-blue?style=flat-square) ![1.21.2](https://img.shields.io/badge/1.21.2-blue?style=flat-square) ![1.21.2.4649](https://img.shields.io/badge/1.21.2.4649-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[prowlarr-develop](https://github.com/volschin/containers/pkgs/container/prowlarr-develop) | develop | ghcr.io/volschin/prowlarr-develop |![1](https://img.shields.io/badge/1-blue?style=flat-square) ![1.21](https://img.shields.io/badge/1.21-blue?style=flat-square) ![1.21.2](https://img.shields.io/badge/1.21.2-blue?style=flat-square) ![1.21.2.4649](https://img.shields.io/badge/1.21.2.4649-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[qbittorrent](https://github.com/volschin/containers/pkgs/container/qbittorrent) | stable | ghcr.io/volschin/qbittorrent |![4](https://img.shields.io/badge/4-blue?style=flat-square) ![4.6](https://img.shields.io/badge/4.6-blue?style=flat-square) ![4.6.5](https://img.shields.io/badge/4.6.5-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[qbittorrent-beta](https://github.com/volschin/containers/pkgs/container/qbittorrent-beta) | beta | ghcr.io/volschin/qbittorrent-beta |![4](https://img.shields.io/badge/4-blue?style=flat-square) ![4.6](https://img.shields.io/badge/4.6-blue?style=flat-square) ![4.6.5](https://img.shields.io/badge/4.6.5-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[radarr](https://github.com/volschin/containers/pkgs/container/radarr) | master | ghcr.io/volschin/radarr |![5](https://img.shields.io/badge/5-blue?style=flat-square) ![5.8](https://img.shields.io/badge/5.8-blue?style=flat-square) ![5.8.3](https://img.shields.io/badge/5.8.3-blue?style=flat-square) ![5.8.3.8933](https://img.shields.io/badge/5.8.3.8933-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[radarr-develop](https://github.com/volschin/containers/pkgs/container/radarr-develop) | develop | ghcr.io/volschin/radarr-develop |![5](https://img.shields.io/badge/5-blue?style=flat-square) ![5.9](https://img.shields.io/badge/5.9-blue?style=flat-square) ![5.9.0](https://img.shields.io/badge/5.9.0-blue?style=flat-square) ![5.9.0.9058](https://img.shields.io/badge/5.9.0.9058-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[readarr-develop](https://github.com/volschin/containers/pkgs/container/readarr-develop) | develop | ghcr.io/volschin/readarr-develop |![0](https://img.shields.io/badge/0-blue?style=flat-square) ![0.3](https://img.shields.io/badge/0.3-blue?style=flat-square) ![0.3.32](https://img.shields.io/badge/0.3.32-blue?style=flat-square) ![0.3.32.2587](https://img.shields.io/badge/0.3.32.2587-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[readarr-nightly](https://github.com/volschin/containers/pkgs/container/readarr-nightly) | nightly | ghcr.io/volschin/readarr-nightly |![0](https://img.shields.io/badge/0-blue?style=flat-square) ![0.4](https://img.shields.io/badge/0.4-blue?style=flat-square) ![0.4.0](https://img.shields.io/badge/0.4.0-blue?style=flat-square) ![0.4.0.2593](https://img.shields.io/badge/0.4.0.2593-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[sabnzbd](https://github.com/volschin/containers/pkgs/container/sabnzbd) | stable | ghcr.io/volschin/sabnzbd |![4](https://img.shields.io/badge/4-blue?style=flat-square) ![4.3](https://img.shields.io/badge/4.3-blue?style=flat-square) ![4.3.2](https://img.shields.io/badge/4.3.2-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[sonarr](https://github.com/volschin/containers/pkgs/container/sonarr) | main | ghcr.io/volschin/sonarr |![4](https://img.shields.io/badge/4-blue?style=flat-square) ![4.0](https://img.shields.io/badge/4.0-blue?style=flat-square) ![4.0.8](https://img.shields.io/badge/4.0.8-blue?style=flat-square) ![4.0.8.1874](https://img.shields.io/badge/4.0.8.1874-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[sonarr-develop](https://github.com/volschin/containers/pkgs/container/sonarr-develop) | develop | ghcr.io/volschin/sonarr-develop |![4](https://img.shields.io/badge/4-blue?style=flat-square) ![4.0](https://img.shields.io/badge/4.0-blue?style=flat-square) ![4.0.8](https://img.shields.io/badge/4.0.8-blue?style=flat-square) ![4.0.8.2158](https://img.shields.io/badge/4.0.8.2158-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[theme-park](https://github.com/volschin/containers/pkgs/container/theme-park) | stable | ghcr.io/volschin/theme-park |![1](https://img.shields.io/badge/1-blue?style=flat-square) ![1.17](https://img.shields.io/badge/1.17-blue?style=flat-square) ![1.17.0](https://img.shields.io/badge/1.17.0-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[volsync](https://github.com/volschin/containers/pkgs/container/volsync) | stable | ghcr.io/volschin/volsync |![0](https://img.shields.io/badge/0-blue?style=flat-square) ![0.10](https://img.shields.io/badge/0.10-blue?style=flat-square) ![0.10.0](https://img.shields.io/badge/0.10.0-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)
[whisparr-nightly](https://github.com/volschin/containers/pkgs/container/whisparr-nightly) | nightly | ghcr.io/volschin/whisparr-nightly |![2](https://img.shields.io/badge/2-blue?style=flat-square) ![2.0](https://img.shields.io/badge/2.0-blue?style=flat-square) ![2.0.0](https://img.shields.io/badge/2.0.0-blue?style=flat-square) ![2.0.0.548](https://img.shields.io/badge/2.0.0.548-blue?style=flat-square) ![rolling](https://img.shields.io/badge/rolling-green?style=flat-square)


## Deprecations

Containers here can be **deprecated** at any point, this could be for any reason described below.

1. The upstream application is **no longer actively developed**
2. The upstream application has an **official upstream container** that follows closely to the mission statement described here
3. The upstream application has been **replaced with a better alternative**
4. The **maintenance burden** of keeping the container here **is too bothersome**

**Note**: Deprecated containers will remained published to this repo for 6 months after which they will be pruned.

## Credits

A lot of inspiration and ideas are thanks to the hard work of [hotio.dev](https://hotio.dev/) and [linuxserver.io](https://www.linuxserver.io/) contributors.