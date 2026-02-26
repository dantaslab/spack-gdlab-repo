# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Sambamba(Package):
    """Sambamba: process your BAM data faster (bioinformatics)"""

    homepage = "https://lomereiter.github.io/sambamba/"
    url      = "https://github.com/biod/sambamba/archive/refs/tags/v0.8.2.tar.gz"

    version('0.8.2', sha256='b4934f2bfdf07b12856e9c7a0634db0a4f6f4b05e2d4d9f0784bab26159590c1')
    #git = "https://github.com/lomereiter/sambamba.git"

    #version("0.8.2", tag="v0.8.2", submodules=True)
    #version("0.6.6", tag="v0.6.6", submodules=True)

    depends_on("ldc~shared", type=("build", "link"))
    depends_on("python", type="build")

    resource(
        name="undeaD",
        git="https://github.com/dlang/undeaD.git",
        tag="v1.0.7",
    )

    patch("Makefile.patch")
    parallel = False

    def install(self, spec, prefix):
        make("sambamba-ldmd2-64")
        mkdirp(prefix.bin)
        for filename in ("build/sambamba", "build/sambamba.debug"):
            install(filename, prefix.bin)
