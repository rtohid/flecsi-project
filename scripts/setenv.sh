# Setup paths
. /scripts/setenv.sh
. /home/stellar/src/spack/share/spack/setup-env.sh
PATH=$PATH:/home/stellar/src/spack/bin:/home/stellar/.local/bin:/usr/lib64/ccache:
PATH=$PATH:/usr/lib64/openmpi/bin/${PATH:+:}$sstellar
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib/${LD_LIBRARY_PATH:+:}${LD_LIBRARY_PATH}
PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages${PYTHONPATH:+:}${PYTHONPATH}
OPENMPI=true

