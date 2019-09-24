# Copyright (c) 2019 R. Tohid
#
# Distributed under the Boost Software License, Version 1.0. (See a copy at
# http://www.boost.org/LICENSE_1_0.txt)

FROM fedora:latest

# List of packages to be installed
ADD ./scripts /scripts


# Install Packages
RUN dnf -y update

# needed foer xargs
RUN dnf install -y findutils
RUN cat /scripts/fedora-packages.txt | xargs dnf install -y

# Get external packages
RUN wget -O /usr/bin/doxy-coverage https://raw.githubusercontent.com/alobbs/doxy-coverage/master/doxy-coverage.py
RUN chmod +x /usr/bin/doxy-coverage

# Add user
RUN groupadd -r stellar
RUN useradd -r -m -g stellar -G wheel stellar
RUN echo '%wheel ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER stellar

RUN pip3 install --user codecov coverxygen gcovr Sphinx recommonmark sphinx_rtd_theme breathe

WORKDIR /home/stellar
CMD sleep infinity

