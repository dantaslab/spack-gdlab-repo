# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Rosetta(Package):
    """The Rosetta software suite includes algorithms for computational modeling
    and analysis of protein structures. It has enabled notable scientific
    advances in computational biology, including de novo protein design, enzyme
    design, ligand docking, and structure prediction of biological
    macromolecules and macromolecular complexes."""

    homepage = "https://www.rosettacommons.org/"
    manual_download = True

    version("3.13", "3033624bb93f3fd2daed37c81d2e7640")
    version("3.12", "0b2462bee2d41053ec8fca7ee1fa632d")

    def url_for_version(self, version):
        return "file://{0}/rosetta_bin_linux_{1}_bundle.tgz".format(os.getcwd(), version)

    # compiling is turning into a nuge pain, so I'm just going to copy the
    # pre-compiled static binaries. Maybe when I have more time I'll take a
    # crack at it (I won't)
    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install_tree("./main/source/bin", prefix.bin, symlinks=False)
