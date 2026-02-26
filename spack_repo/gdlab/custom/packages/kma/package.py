# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Kma(MakefilePackage):
    """KMA is a mapping method designed to map raw reads directly against
       redundant databases, in an ultra-fast manner using seed and extend"""

    homepage = "https://bitbucket.org/genomicepidemiology/kma/src/master/"
    url      = "https://bitbucket.org/genomicepidemiology/kma/get/1.4.2.tar.gz"


    version('1.4.2', sha256='fae339a24ff05ac924b93df838f0a097bdcad1178e696bf70122d4b09bd649e1')

    depends_on('zlib', type=('build', 'link'))

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('kma', prefix.bin)
        install('kma_index', prefix.bin)
        install('kma_shm', prefix.bin)
        install('kma_update', prefix.bin)
