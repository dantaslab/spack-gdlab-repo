# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.perl import PerlPackage
from spack.package import *


class PerlFindbin(PerlPackage):
    """Locates the full path to the script bin directory to allow
       the use of paths relative to the bin directory."""

    homepage = "https://metacpan.org/pod/FindBin"
    url      = "https://cpan.metacpan.org/authors/id/T/TO/TODDR/FindBin-1.52.tar.gz"

    version('1.52_01', sha256='a1129c6f72e418070131800b06c87505cb8298081bef8b31c006029e644283c0')
