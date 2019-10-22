#!/usr/bin/python3

import os
import docker
import argparse
import datetime

cwd = os.getcwd()
dockerfile_path = os.path.dirname(os.path.realpath(__file__)) + "/../docker/"
print(dockerfile_path)

arg_parser = argparse.ArgumentParser(description="Builds FleCSI environments.")

# Set the Linux distro of the Docker image.
distro = arg_parser.add_mutually_exclusive_group()
distro.add_argument(
    '-os',
    "--os",
    choices=['fedora', 'ubuntu'],
    default='fedora',
    help="builds the docker image of the selected distro. Default: fedora.")

# Set the build/install type.
build_type = arg_parser.add_mutually_exclusive_group()
build_type.add_argument(
    '-b',
    "--build",
    choices=['debug', 'release'],
    default='debug',
    help=
    "builds flecsi and all it's dependencies in 'debug', or 'release' mode. Default: debug"
)
build_type.add_argument(
    '-i',
    "--install",
    choices=['debug', 'release'],
    help=
    "installs flecsi and all it's dependencies in 'debug', or 'release' mode. Default: debug"
)

args = arg_parser.parse_args()

docker_client = docker.from_env()

image_tag = args.os + '-' + args.build
image_name = "{image_name}:{tag}".format(image_name='flecsi', tag=image_tag)
docker_client.images.build(path=dockerfile_path, tag=image_name)
