# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack import *


class SnpDists(MakefilePackage):
    """snp-dists: Convert a FASTA alignment to SNP distance matrix"""

    homepage = "https://github.com/tseemann/snp-dists"
    url      = "https://github.com/tseemann/snp-dists/archive/refs/tags/v0.8.2.tar.gz"

    version('0.8.2', sha256='88b8c3bdbaeebad7063889b3beb3124f2599489cee155038f1dcb7fb151af7f5')

    depends_on("zlib", type="build")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("snp-dists", prefix.bin)
