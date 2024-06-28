# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Snippy(Package):
    """Rapid haploid variant calling and core genome alignment"""

    homepage = "https://github.com/tseemann/snippy"
    url = "https://github.com/tseemann/snippy/archive/refs/tags/v4.6.0.tar.gz"

    license("GPL-2.0")

    version("4.6.0", sha256="7264e3819e249387effd3eba170ff49404b1cf7347dfa25944866f5aeb6b11c3")

    depends_on("perl@5.26:", type="run")
    depends_on("perl-bioperl", type="run")
    depends_on("samtools@1.17", type="run")
    
    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.binaries)
        mkdirp(prefix.perl5)
        install_tree("bin", prefix.bin)
        install_tree("binaries", prefix.binaries)
        install_tree("perl5", prefix.perl5)