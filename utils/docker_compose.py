# Copyright (c) 2019 R. Tohid
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

import os
import json

from yaml import safe_load, dump
from collections import defaultdict


class ServiceConfigs:
    """
    Either a path to a directory containing a Dockerfile, or a url to a git repo.
    """
    def __init__(self,
                 context='.',
                 dockerfile='Dockerfile',
                 args=[],
                 volumes=None,
                 image=None,
                 name=None,
                 restart=None):

        self.context = context
        self.dockerfile = dockerfile
        self.args = args
        self.volumes = volumes
        self.image = image
        self.name = name
        self.restart = restart


class DockerBuilder:
    def __init__(self,
                 path=None,
                 tag=None,
                 quiet=False,
                 fileobj=None,
                 nocache=False,
                 rm=False,
                 timeout=None,
                 custom_context=False,
                 encoding=None,
                 pull=False,
                 forcerm=False,
                 dockerfile=None,
                 container_limits=None,
                 decode=False,
                 buildargs=None,
                 gzip=False,
                 shmsize=None,
                 labels=None,
                 cache_from=None,
                 target=None,
                 network_mode=None,
                 squash=None,
                 extra_hosts=None,
                 platform=None,
                 isolation=None):
        pass


class DockerCompose:
    def __init__(self, file=None):
        """Parser of `docker-compose.yml` files.
        """
        with open(file, 'r') as f:
            compose_file = safe_load(f)
            print(compose_file)
        self.compose(compose_file)

    def compose(self, docker_config):
        self.config = defaultdict(lambda: None)
        for k, v in docker_config.items():
            self.config[k] = v
        with open('out.json', 'w') as json_file:
            json.dump(docker_config, json_file, indent=2)

    def __repr__(self):
        for k, v in self.config.items():
            print(k, ':')
            print(v, '\n')
        return ''


current_dir = os.path.dirname(os.path.abspath(__file__))
file_relative_path = '/../docker/docker-compose.yml'
a = DockerCompose(current_dir + file_relative_path)
print(a)
