# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Skesa(MakefilePackage):
    """SKESA is a de-novo sequence read assembler for microbial genomes"""

    homepage = "https://github.com/ncbi/SKESA"
    url      = "https://github.com/ncbi/SKESA/archive/refs/tags/2.4.0.tar.gz"

    version('2.4.0', sha256='c07b56dfa394c013e519d5a246b7dee03db41d8ac912ab9ca02cf4d20bf13b15')

    depends_on("cmake", type="build")
    depends_on("boost",type="build")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("skesa", prefix.bin)
