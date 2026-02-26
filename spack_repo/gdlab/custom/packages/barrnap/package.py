# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack import *


class Barrnap(MakefilePackage):
    """Barrnap predicts the location of ribosomal RNA genes in genomes. It
       supports bacteria (5S,23S,16S), archaea (5S,5.8S,23S,16S), metazoan
       mitochondria (12S,16S) and eukaryotes (5S,5.8S,28S,18S)."""

    homepage = "https://github.com/tseemann/barrnap"    
    url      = "https://github.com/tseemann/barrnap/archive/refs/tags/0.9.tar.gz"


    version('0.9', sha256='36c27cd4350531d98b3b2fb7d294a2d35c15b7365771476456d7873ba33cce15')
    version('0.8', sha256='82004930767e92b61539c0de27ff837b8b7af01236e565f1473c63668cf0370f')
    version('0.7', sha256='ef2173e250f06cca7569c03404c9d4ab6a908ef7643e28901fbe9a732d20c09b')

    depends_on('perl@5:')
    depends_on('hmmer@3:')
    depends_on('bedtools2@2.27.0:')

    def install(self, spec, prefix):
        install_tree('bin', prefix.bin)
        install_tree('binaries', prefix.binaries)
        install_tree('build', prefix.build)
        install_tree('db', prefix.db)
        install_tree('examples', prefix.examples)
