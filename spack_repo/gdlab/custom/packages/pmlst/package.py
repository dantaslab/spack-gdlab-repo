# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.generic import Package
from spack import *


class Pmlst(Package):
    """pMLST: Plasmid Multi-Locus Sequence Typing"""

    homepage = "https://bitbucket.org/genomicepidemiology/pmlst/src/master/"
    url      = "https://bitbucket.org/genomicepidemiology/pmlst/get/2.0.3.tar.gz"


    version('2.0.3', sha256='3da48017ded3fc8a97e4f7fdccab8dc7eacc160ff278de8a2ec26a3dd9f2a45c')

    depends_on('python@3.5.0:', type=('build', 'run'))
    depends_on('py-biopython@1.73', type=('build', 'run'))
    depends_on('py-tabulate@0.7.7', type=('build', 'run'))   
    depends_on('py-cgecore@1.3.2:', type=('build', 'run'))
    depends_on('blast-plus@2.8.1:', type=('build', 'run'))
    depends_on('kma', type=('build', 'run'))

    def install(self, spec, prefix):
         mkdir(prefix.bin)
         install('pmlst.py', prefix.bin)
