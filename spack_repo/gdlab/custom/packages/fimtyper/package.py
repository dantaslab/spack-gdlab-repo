# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
import stat

class Fimtyper(Package):
    """Identifies the FimH type in total or partial sequenced isolates of E. coli"""

    homepage = "https://bitbucket.org/genomicepidemiology/fimtyper/src/master/"
    url = "https://github.com/dantaslab/FimTyper/releases/download/v1.0.0/fimtyper-1.0.0.tar.gz"

    version('1.0.0', sha256='b56dd3533c19e8f3678e112b5d231760ac142120c5e137384baee3babed7b67e')

    depends_on("perl", type="run")
    depends_on("python", type="run")
    depends_on("perl-bioperl", type="run")
    depends_on("blast-plus", type="run")
    depends_on("perl-try-tiny-retry")

    def install(self, spec, prefix):
        install_tree("bin", prefix.bin)
        install_tree("data", prefix.data)
