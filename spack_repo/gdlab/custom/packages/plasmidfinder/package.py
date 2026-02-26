# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.generic import Package
from spack import *


class Plasmidfinder(Package):
    """PlasmidFinder: in silico detection of plasmids"""

    homepage = "https://bitbucket.org/genomicepidemiology/plasmidfinder/src/master/"
    url      = "https://bitbucket.org/genomicepidemiology/plasmidfinder/get/2.1.6.tar.gz"

    version('2.1.6', sha256='ce1535c2a227a7dfa798468e8c8e9ce8602e6b16f0cf33cd4802b8f40c8b61ec')
    version('2.1.5', sha256='05afa637ba65b39007bd51fcc87607642a0f51736e36e7be37d12c8e508297dd')
    version('2.1.4', sha256='1e0b65787bdf64d882b7cb78f3205aa434b7dba6ec0cf2c809464733ecc20616')
    version('2.1.3', sha256='14f33f3d0be6247e0df82f4094016935f1a31637acccb3c8fd5c03cee017d12f')
    version('2.1.2', sha256='75c63d0c8bd889192e75f39812e70878496622e09ad78b049ed47a6b9ba6dbc7')

    depends_on('python@3.5.0:', type=('build', 'run'))
    depends_on('py-tabulate@0.7.7', type=('build', 'run'))
    depends_on('py-cgecore@1.5.5:', type=('build', 'run'))
    depends_on('blast-plus@2.8.1:', type=('build', 'run'))
    depends_on('kma', type=('build', 'run'))

    def install(self, spec, prefix):
          mkdir(prefix.bin)
          install('plasmidfinder.py', prefix.bin)
