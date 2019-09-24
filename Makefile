SPACK_BRANCH?=flecsi-hpx
all: help

help:
	@echo " \
	spack: \n\
		if [ ! -d "./spack" ]; then git clone https://github.com/rtohid/spack.git; fi \n\
		cd ./spack/ && git checkout $(SPACK_BRANCH) \n\
\n\
	build: spack \n\
		docker-compose up -d \n\
\n\
	run: build \n\
		docker exec -it flecsi-stellar /bin/bash \n\
\n\
	stop: \n\
		docker-compose down \n\
\n\
	prune: \n\
		docker system prune -f \n\
	"
spack:
	if [ ! -d "./spack" ]; then git clone https://github.com/rtohid/spack.git; fi
	cd ./spack/ && git checkout $(SPACK_BRANCH)

build: spack
	docker-compose up -d

run: build
	docker exec -it flecsi-stellar /bin/bash

stop:
	docker-compose down

prune:
	docker system prune -f

.PHONY:
