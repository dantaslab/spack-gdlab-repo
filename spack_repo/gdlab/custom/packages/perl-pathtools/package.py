# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.perl import PerlPackage
from spack.package import *


class PerlPathtools(PerlPackage):
    """Tools for working with directory and file names."""

    homepage = "https://metacpan.org/dist/PathTools"
    url      = "https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/PathTools-3.75.tar.gz"

    version('3.75', sha256='a558503aa6b1f8c727c0073339081a77888606aa701ada1ad62dd9d8c3f945a2')
