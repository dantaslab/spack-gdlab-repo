# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Infernal(AutotoolsPackage):
    """Infernal (INFERence of RNA ALignment) is for searching DNA sequence
    databases for RNA structure and sequence similarities. It is an
    implementation of a special case of profile stochastic context-free
    grammars called covariance models (CMs)."""

    homepage = "http://eddylab.org/infernal/"
    url = "http://eddylab.org/infernal/infernal-1.1.2.tar.gz"

    version("1.1.4", sha256="f9493c7dee9fbf25f6405706818883d24b9f5e455121a0662c96c8f0307f95fc")
    version("1.1.3", sha256="3b98a6a3a0e7b01aa077a0caf1e958223c4d8f80a69a4eb602ca59a3475da85e")
    version("1.1.2", sha256="ac8c24f484205cfb7124c38d6dc638a28f2b9035b9433efec5dc753c7e84226b")

    variant("mpi", default=False, description="Enable MPI parallel support")

    depends_on("mpi", when="+mpi")

    def configure_args(self):
        args = []
        if "+mpi" in self.spec:
            args.append("--enable-mpi")
        else:
            args.append("--disable-mpi")
        return args
