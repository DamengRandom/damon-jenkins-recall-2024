# Jenkins

Is a platform for build test and deploy apps

## Infrastructure:

1. Commit triggers pipeline
2. Agent selected based on labels (setup)
3. Agent runs the build

### Agent types:

- Permanent agent: dedicated server for running jobs
- Cloud agent: docker, K8s, AWS cloud techs (setup, trigger and run)

### Build types:

- Freestyle build: simple method to create build, like shell scripts
- Pipelines: use groovy syntax to create your custom build (divided by stages)

Able to run Jenkins inside docker container (locally trials)

### Declarative pipeline:

- followed pipeline as code principle
- represented by few sections, starts with pipeline { … }
- use groovy syntax

### Reference

101 Session: https://github.com/devopsjourney1/jenkins-101
