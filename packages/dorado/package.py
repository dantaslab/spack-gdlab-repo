# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Dorado(Package):
    """
    Dorado is a high-performance, easy-to-use, open source basecaller for Oxford Nanopore reads.
    """
    
    homepage = "https://github.com/nanoporetech/dorado"
    url      = "https://cdn.oxfordnanoportal.com/software/analysis/dorado-0.7.2-linux-x64.tar.gz"

    version('0.7.2', sha256='08ba055df86dca3fad35ab22c801536d22f1954fb080eb1b9b3e08ae0838755f')

    depends_on('cuda@11.7.0:', when='@6.5.7-cuda', type='run')
    def install(self, spec, prefix):
        install_tree("bin", prefix.bin)
        install_tree("lib", prefix.lib)